# AI Research Assistant for BCI

Workspace phục vụ nghiên cứu về Brain-Computer Interface (BCI), EEG Signal Processing, Neural Decoding, Cognitive Neuroscience, Machine Learning và Explainable AI.

## Cấu trúc

```text
.
├── .agents/skills/                Custom skills của project
├── papers/
│   ├── raw/                       PDF và supplementary files gốc
│   └── metadata/                  Metadata đã kiểm tra (DOI, arXiv ID, BibTeX...)
├── knowledge/
│   ├── paper-notes/               Ghi chú có dẫn trang cho từng paper
│   ├── literature-matrix/         Working/canonical matrix trong quá trình tổng hợp
│   └── research-gaps/             Research gaps và giả thuyết kiểm chứng được
├── datasets/                      Dataset hoặc tài liệu mô tả dataset
├── experiments/                   Cấu hình, log và kết quả thí nghiệm
├── scripts/                       Script tái lập hoặc xử lý dữ liệu
└── reports/                       Báo cáo Markdown và final matrix/evidence snapshots
```

Các thư mục dữ liệu có thể chứa nội dung lớn hoặc nhạy cảm. Không gửi dữ liệu người tham gia tới dịch vụ bên ngoài khi chưa được cho phép. Giữ dữ liệu gốc bất biến; lưu biến đổi, tham số và kết quả vào vị trí tách biệt để hỗ trợ reproducibility.

## Cách dùng

- Quy tắc chung: [`AGENTS.md`](AGENTS.md).
- Đọc một paper: gọi skill `bci-paper-reader` với tên file trong `papers/raw/` hoặc arXiv ID, rồi gõ "tiếp tục" cho tới khi dịch xong. Kết quả nằm ở `knowledge/paper-notes/<slug>/`; phần phân tích chỉ được tạo sau khi bản dịch qua kiểm tra độ phủ.
- Công cụ: `.venv\Scripts\python scripts\paper_tools.py --help`. Cài lần đầu: `uv venv .venv` rồi `uv pip install --python .venv -r requirements.txt`.

## Custom skills

- `bci-paper-reader`: dịch toàn văn trung thành một paper, chú giải thuật ngữ, rồi phân tích.
- `bci-literature-review`: tổng hợp và so sánh nhiều paper.
- `bci-paper-auditor`, `bci-citation-audit`: audit phê bình, chỉ chạy khi gọi đích danh.
