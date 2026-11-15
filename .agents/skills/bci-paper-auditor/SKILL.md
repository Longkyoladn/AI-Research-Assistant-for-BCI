---
name: bci-paper-auditor
description: Audit phê bình một paper (validity, leakage, reproducibility, evidence ledger). Chỉ dùng khi người dùng gọi đích danh skill này hoặc yêu cầu rõ "audit"; để đọc, dịch hoặc tìm hiểu nội dung một paper thì dùng bci-paper-reader.
---

# BCI Paper Auditor

Đọc và audit toàn bộ paper cùng supplementary materials được cung cấp, rồi viết báo cáo tiếng Việt dạng Markdown vào `reports/`. Giữ thuật ngữ kỹ thuật tiếng Anh khi dịch làm mất độ chính xác.

## Input và routing

- Input chính là một paper toàn văn, ưu tiên PDF, cùng supplementary materials và DOI/arXiv ID nếu có. Ghi rõ version của tài liệu thực sự được đọc.
- Nếu yêu cầu tổng hợp hoặc so sánh nhiều paper, dùng `bci-literature-review`. Nếu trọng tâm là kiểm chứng claim–citation alignment hoặc bibliography của một tài liệu, dùng `bci-citation-audit`.
- Paper trên arXiv có thể được truy xuất bằng arXiv Plugin khi công cụ sẵn có và việc truy xuất nguồn ngoài nằm trong phạm vi được phép; plugin chịu trách nhiệm retrieval, skill này chịu trách nhiệm audit khoa học.

## Nguyên tắc bằng chứng

- Kiểm tra lần lượt mọi trang, không chỉ abstract hoặc phần text trích xuất được. Ghi nhận phạm vi trang đã đọc và các trang/phần không thể kiểm tra.
- Kiểm tra trực quan figures, panels, tables, captions, equations và model/experimental diagrams. Không suy diễn từ caption, OCR hoặc surrounding text rằng đã xem nội dung hình.
- Mọi khẳng định quan trọng phải gắn với số trang PDF và, khi có, `Figure`, `Table`, `Equation`, supplementary item, DOI hoặc nguồn ngoài thực sự đã kiểm tra. Phân biệt số trang PDF với số trang in trên paper nếu chúng khác nhau.
- Không điền dữ kiện còn thiếu bằng kiến thức nền. Dùng `không được báo cáo`, `không xác định được`, hoặc `chưa kiểm tra được` và nêu lý do.
- Nếu công cụ không đọc được trang, hình, công thức, lớp OCR, attachment hoặc supplementary file, thông báo giới hạn cụ thể; không tuyên bố đã đọc phần đó.
- Với arXiv, ghi versioned ID và cách truy xuất (`abstract`, LaTeX section, HTML/PDF full text). Search result hoặc abstract không đủ để xác minh Methods/Results; LaTeX source không thay thế visual inspection của rendered PDF khi kết luận phụ thuộc vào figure, table, layout hoặc số trang.
- Nếu arXiv Plugin hoặc công cụ đọc PDF không hoạt động, báo giới hạn và dùng nguồn truy cập được; không tự cài package, fallback runtime hoặc MCP.

## Phạm vi audit

Phân tích các phần hiện diện trong tài liệu: Abstract, Introduction, Related Work, Methods, Results, Discussion, Conclusion và Supplementary Materials. Với mỗi phần, tóm tắt lập luận chính, bằng chứng, giả định và điểm chưa rõ kèm dẫn chứng trang.

Trích xuất có cấu trúc, nếu paper báo cáo:

- research question, hypotheses, task và experimental paradigm;
- participants, inclusion/exclusion, demographics, ethics và power/sample-size rationale;
- recording modality, device, electrode/sensor locations, montage/reference, channel count, sampling rate và acquisition protocol;
- preprocessing, filtering, epoching, baseline, resampling, artifact detection/rejection/correction, leakage risks và retained trials;
- frequency bands, temporal/spatial features, feature extraction/selection và neurophysiological rationale;
- model architecture, inputs/outputs, objective/loss, training, validation, hyperparameters, baselines, ablations và compute/software khi có;
- evaluation unit, data splits, subject-dependent/independent setting, cross-validation, metrics, uncertainty, statistical tests, effect sizes, multiple-comparison correction và assumptions;
- primary/secondary results, negative findings và correspondence between reported claims and evidence.

## Kiểm tra theo chuyên môn

- Xác định đúng modality: scalp EEG, ECoG, intracortical recordings, fMRI hoặc MEG; không dùng lẫn thuật ngữ hay ngoại suy trực tiếp giữa chúng.
- Đánh giá các giới hạn vật lý liên quan: invasiveness, spatial/temporal resolution, source localization/inverse problem, volume conduction, hemodynamic delay, magnetic-field measurement, SNR, motion/artifact sensitivity và mức độ khái quát hóa. Chỉ áp dụng giới hạn phù hợp với modality và thiết kế đang xét.
- Với mỗi phương trình quan trọng, giải thích ký hiệu, inputs/outputs, phép biến đổi hoặc objective theo góc nhìn toán học; sau đó giải thích mối liên hệ với tín hiệu, giả thuyết hoặc cơ chế neuroscience. Không gán ý nghĩa sinh học vượt quá bằng chứng của paper.
- Đối chiếu figures/tables với prose và statistics; nêu rõ inconsistency, denominator mơ hồ, missing variance, suspicious split, data leakage, circular analysis hoặc unsupported causal language nếu quan sát được.

## Phân tầng nhận định

Giữ bốn loại nội dung tách biệt và gắn nhãn rõ:

1. **Experimental evidence** — kết quả đo/ước lượng được paper báo cáo.
2. **Author interpretation** — diễn giải hoặc kết luận của tác giả.
3. **Hypothesis** — giả thuyết hoặc speculation chưa được kiểm chứng đầy đủ.
4. **AI inference** — suy luận của người audit, nêu căn cứ và mức độ chắc chắn.

## Validity và reproducibility

Đánh giá limitations được tác giả thừa nhận và các threats to internal, external, construct và statistical-conclusion validity. Kiểm tra reproducibility dựa trên mức đầy đủ của data/code availability, preprocessing, parameters, seeds, splits, hardware/software, protocol và reporting. Kết thúc bằng open research questions cụ thể, không trình bày suy đoán như kết quả.

## Đầu ra

Tạo `reports/<paper-slug>-audit.md`; không ghi đè báo cáo có sẵn nếu người dùng chưa cho phép. Báo cáo cần có:

- citation/DOI và phạm vi tài liệu đã kiểm tra;
- executive summary;
- phân tích theo section và bảng Methods/Experimental Setup;
- audit figures, tables, equations và model architecture;
- findings được phân tầng theo bốn nhãn trên;
- limitations, threats to validity, reproducibility và open questions;
- evidence ledger ánh xạ các khẳng định chính tới page/figure/table/equation/source;
- mục `Không thể kiểm tra / Không được báo cáo` để công khai mọi khoảng trống.

Trước khi hoàn tất, đối chiếu từng khẳng định chính với evidence ledger và xác nhận không có phần tài liệu nào được tuyên bố là đã đọc khi chưa kiểm tra được.
