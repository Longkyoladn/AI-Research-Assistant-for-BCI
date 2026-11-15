"""Cong cu cho skill bci-paper-reader: chuan bi nguon, cat hinh, kiem tra do phu ban dich.

Chay bang Python cua project:
    .venv\\Scripts\\python scripts\\paper_tools.py <lenh> ...

Lenh:
    prepare <pdf> <slug> [--part main]   Trich text theo khoi (block), render trang, tao 00-index.md
    crop <slug> <part> <page> <x0> <y0> <x1> <y1> <ten-file>
                                         Cat mot vung trang (toa do 0..1) thanh figures/<ten-file>.png
    status <slug>                        Liet ke trang nao da xu ly het khoi, trang nao chua
    check <slug> [--pages 1-4] [--part main]
                                         Kiem tra do phu; ma thoat 0 = dat, 1 = chua dat

Dinh danh khoi: <part>-p<trang>-<so thu tu>, vi du main-p03-07.
Trong ban dich:
    **¶ main-p03-07**            mo dau doan dich cua khoi do
    **¶ main-p03-08 + main-p04-02**   doan goc bi ngat qua cot/trang, dich lien mot doan
    <!-- skip main-p03-01: running header -->   khoi khong dich, phai ghi ly do
    <!-- skip main-p04-03, main-p04-04: chu trong Figure 1 -->   nhieu khoi cung ly do
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NOTES = ROOT / "knowledge" / "paper-notes"

BLOCK_ID = r"[a-z0-9]+-p\d{2,3}-\d{2,3}"
MARK_RE = re.compile(r"¶\s*(" + BLOCK_ID + r"(?:\s*\+\s*" + BLOCK_ID + r")*)")
SKIP_RE = re.compile(r"<!--\s*skip\s+(" + BLOCK_ID + r"(?:\s*,\s*" + BLOCK_ID + r")*)\s*:\s*(.*?)-->", re.S)
NUM_RE = re.compile(r"\d+(?:[.,]\d+)*")
GLOSS_RE = re.compile(r"⟦.*?⟧", re.S)
FIG_RE = re.compile(r"\b(Fig(?:ures?|s?\.)|Tables?)\s*(S?\d+)", re.I)
MIN_RATIO = 0.6  # do dai ban dich / do dai doan goc, duoi nguong nay bi coi la luoc


def paper_dir(slug: str) -> Path:
    return NOTES / slug


def norm_numbers(text: str) -> list[str]:
    """Cac chuoi chu so trong van ban. Tach o moi ky tu khong phai so de 9,800 / 9.800 / 9 800
    va '2019.3' (nam + so trich dan dinh lien) / '2019 [3]' deu cho cung ket qua."""
    return re.findall(r"\d+", text)


def load_blocks(slug: str) -> dict[str, dict]:
    path = paper_dir(slug) / "source" / "blocks.json"
    if not path.exists():
        sys.exit(f"Chua co {path}. Chay lenh prepare truoc.")
    return json.loads(path.read_text(encoding="utf-8"))


def cmd_prepare(args: argparse.Namespace) -> int:
    import pymupdf

    pdf = Path(args.pdf)
    if not pdf.exists():
        sys.exit(f"Khong tim thay PDF: {pdf}")
    out = paper_dir(args.slug)
    src = out / "source"
    blocks_path = src / "blocks.json"
    blocks: dict[str, dict] = {}
    if blocks_path.exists():
        blocks = json.loads(blocks_path.read_text(encoding="utf-8"))
        if any(b["part"] == args.part for b in blocks.values()):
            sys.exit(f"Part '{args.part}' da duoc prepare cho {args.slug}; khong ghi de.")
    elif out.exists() and any(out.iterdir()):
        sys.exit(f"Thu muc {out} da co noi dung; chon slug khac, khong ghi de.")

    (src / "pages").mkdir(parents=True, exist_ok=True)
    (out / "figures").mkdir(exist_ok=True)

    doc = pymupdf.open(pdf)
    lines = []
    for pno, page in enumerate(doc, start=1):
        page.get_pixmap(dpi=110).save(src / "pages" / f"{args.part}-p{pno:02d}.png")
        n = 0
        lines.append(f"\n===== {args.part} trang PDF {pno} =====\n")
        for b in page.get_text("blocks", sort=False):
            if b[6] != 0:  # khoi anh
                continue
            text = b[4].strip()
            if not text:
                continue
            n += 1
            bid = f"{args.part}-p{pno:02d}-{n:02d}"
            blocks[bid] = {
                "part": args.part,
                "page": pno,
                "bbox": [round(v / d, 3) for v, d in zip(b[:4], (page.rect.width, page.rect.height) * 2)],
                "text": text,
            }
            lines.append(f"[{bid}]\n{text}\n")
    blocks_path.write_text(json.dumps(blocks, ensure_ascii=False, indent=1), encoding="utf-8")
    (src / f"{args.part}.txt").write_text("\n".join(lines), encoding="utf-8")

    index = out / "00-index.md"
    if not index.exists():
        index.write_text(
            f"# {args.slug}\n\n"
            "| Truong | Gia tri |\n|---|---|\n"
            "| Title | |\n| Authors | |\n| Venue / nam | |\n| DOI / arXiv ID | |\n| Modality | |\n\n"
            "## Nguon\n\n| Part | File PDF | So trang | Trang thai |\n|---|---|---|---|\n\n"
            "## Tien do dich\n\n| File | Section | Trang PDF | Trang thai | check |\n|---|---|---|---|---|\n\n"
            "## Phu luc bai bao nhac toi\n\n| Phu luc | Trang thai |\n|---|---|\n",
            encoding="utf-8",
        )
    with index.open("a", encoding="utf-8") as f:
        f.write(f"\n<!-- prepare: part={args.part} pdf={pdf.as_posix()} pages={len(doc)} blocks="
                f"{sum(1 for b in blocks.values() if b['part'] == args.part)} -->\n")
    print(f"OK: {len(doc)} trang, {sum(1 for b in blocks.values() if b['part'] == args.part)} khoi -> {out}")
    print(f"Text goc: {src / (args.part + '.txt')}\nAnh trang: {src / 'pages'}")
    return 0


def cmd_crop(args: argparse.Namespace) -> int:
    import pymupdf

    out = paper_dir(args.slug) / "figures" / f"{args.name}.png"
    if out.exists():
        sys.exit(f"{out} da ton tai; doi ten hoac xoa thu cong.")
    pdf = None
    for line in (paper_dir(args.slug) / "00-index.md").read_text(encoding="utf-8").splitlines():
        m = re.search(r"prepare: part=(\S+) pdf=(.+?) pages=", line)
        if m and m.group(1) == args.part:
            pdf = Path(m.group(2))
    if pdf is None or not pdf.exists():
        sys.exit(f"Khong xac dinh duoc PDF cua part '{args.part}' tu 00-index.md.")
    page = pymupdf.open(pdf)[args.page - 1]
    w, h = page.rect.width, page.rect.height
    clip = pymupdf.Rect(args.x0 * w, args.y0 * h, args.x1 * w, args.y1 * h)
    page.get_pixmap(dpi=220, clip=clip).save(out)
    print(f"OK: {out}")
    return 0


def read_translation(slug: str) -> tuple[dict[str, int], list[tuple[list[str], str]], dict[str, str], str]:
    """Tra ve (khoi -> chi so nhom, danh sach nhom (cac khoi, doan dich), khoi -> ly do skip, markdown)."""
    translated: dict[str, int] = {}
    groups: list[tuple[list[str], str]] = []
    skipped: dict[str, str] = {}
    all_md = []
    for md in sorted(paper_dir(slug).glob("*.md")):
        if md.name in ("00-index.md", "glossary.md") or md.name.startswith("9"):
            continue
        text = md.read_text(encoding="utf-8")
        all_md.append(text)
        for m in SKIP_RE.finditer(text):
            for bid in re.findall(BLOCK_ID, m.group(1)):
                skipped[bid] = m.group(2).strip()
        marks = list(MARK_RE.finditer(text))
        for i, m in enumerate(marks):
            body = text[m.end(): marks[i + 1].start() if i + 1 < len(marks) else len(text)]
            ids = re.findall(BLOCK_ID, m.group(1))
            groups.append((ids, SKIP_RE.sub("", body)))
            for bid in ids:
                translated[bid] = len(groups) - 1
    return translated, groups, skipped, "\n".join(all_md)


def parse_pages(spec: str | None) -> set[int] | None:
    if not spec:
        return None
    pages: set[int] = set()
    for part in spec.split(","):
        a, _, b = part.partition("-")
        pages.update(range(int(a), int(b or a) + 1))
    return pages


def cmd_status(args: argparse.Namespace) -> int:
    blocks = load_blocks(args.slug)
    translated, _, skipped, _ = read_translation(args.slug)
    per_page: dict[tuple[str, int], list[int]] = {}
    for bid, b in blocks.items():
        done, total = per_page.setdefault((b["part"], b["page"]), [0, 0])
        per_page[(b["part"], b["page"])] = [done + (bid in translated or bid in skipped), total + 1]
    for (part, page), (done, total) in sorted(per_page.items()):
        state = "xong" if done == total else ("chua" if done == 0 else "do dang")
        print(f"{part} trang {page:>3}: {done:>3}/{total:<3} {state}")
    return 0


def cmd_check(args: argparse.Namespace) -> int:
    blocks = load_blocks(args.slug)
    translated, groups, skipped, all_md = read_translation(args.slug)
    pages = parse_pages(args.pages)
    scope = {
        bid: b for bid, b in blocks.items()
        if (args.part is None or b["part"] == args.part) and (pages is None or b["page"] in pages)
    }
    errors: list[str] = []
    warnings: list[str] = []

    for bid in set(translated) | set(skipped):
        if bid not in blocks:
            errors.append(f"{bid}: dinh danh khong ton tai trong nguon")

    for bid in scope:
        if bid in translated:
            continue
        if bid in skipped:
            if not skipped[bid]:
                errors.append(f"{bid}: skip khong ghi ly do")
        else:
            errors.append(f"{bid}: CHUA DICH (trang {scope[bid]['page']}): {scope[bid]['text'][:70]!r}")

    # So va do dai duoc so theo nhom (mot doan dich co the gop nhieu khoi goc bi ngat cot/trang).
    for gi in sorted({translated[b] for b in scope if b in translated}):
        members, body = groups[gi]
        members = [b for b in members if b in blocks]
        src_text = " ".join(blocks[b]["text"] for b in members)
        have = norm_numbers(body)
        missing = []
        for n in norm_numbers(src_text):
            if n in have:
                have.remove(n)
            else:
                missing.append(n)
        label = " + ".join(members)
        if missing:
            errors.append(f"{label}: thieu so {missing}")
        plain = re.sub(r"!\[.*?\]\(.*?\)", "", GLOSS_RE.sub("", body)).strip()
        ratio = len(plain) / max(len(src_text), 1)
        if len(src_text) >= 200 and ratio < MIN_RATIO:
            errors.append(f"{label}: ban dich ngan bat thuong ({ratio:.2f} lan doan goc) - nghi luoc cau")

    # Figure / Table duoc nhac toi trong nguon phai co anh va duoc chen vao ban dich.
    fig_dir = paper_dir(args.slug) / "figures"
    wanted: set[str] = set()
    for b in scope.values():
        for kind, num in FIG_RE.findall(b["text"]):
            wanted.add(("table" if kind.lower().startswith("table") else "fig") + "-" + num.lower())
    have_parts = {b["part"] for b in blocks.values()}
    for name in sorted(wanted):
        is_supp = re.search(r"-s\d", name) is not None
        ok = (fig_dir / f"{name}.png").exists() and f"figures/{name}.png" in all_md
        if ok:
            continue
        msg = f"{name}: chua co figures/{name}.png hoac chua chen vao ban dich"
        if is_supp and len(have_parts) == 1:
            warnings.append(msg + " (thuoc phu luc chua co)")
        else:
            errors.append(msg)

    n_tr = sum(1 for b in scope if b in translated)
    n_sk = sum(1 for b in scope if b in skipped)
    print(f"Pham vi: {len(scope)} khoi | da dich {n_tr} | skip {n_sk} | loi {len(errors)} | canh bao {len(warnings)}")
    for w in warnings:
        print("CANH BAO:", w)
    for e in errors:
        print("LOI:", e)
    print("KET QUA:", "DAT" if not errors else "CHUA DAT")
    return 0 if not errors else 1


def main() -> int:
    for stream in (sys.stdout, sys.stderr):
        stream.reconfigure(encoding="utf-8")
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    a = sub.add_parser("prepare")
    a.add_argument("pdf")
    a.add_argument("slug")
    a.add_argument("--part", default="main", help="main, supp, supp2 ... (chu thuong va so)")
    a.set_defaults(fn=cmd_prepare)

    a = sub.add_parser("crop")
    a.add_argument("slug")
    a.add_argument("part")
    a.add_argument("page", type=int)
    for k in ("x0", "y0", "x1", "y1"):
        a.add_argument(k, type=float)
    a.add_argument("name", help="fig-1, fig-2, table-1, fig-s3 ...")
    a.set_defaults(fn=cmd_crop)

    a = sub.add_parser("status")
    a.add_argument("slug")
    a.set_defaults(fn=cmd_status)

    a = sub.add_parser("check")
    a.add_argument("slug")
    a.add_argument("--pages")
    a.add_argument("--part")
    a.set_defaults(fn=cmd_check)

    args = p.parse_args()
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
