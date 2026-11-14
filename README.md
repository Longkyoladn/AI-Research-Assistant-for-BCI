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

## Quy ước nghiên cứu

- Quy tắc làm việc chung nằm trong [`AGENTS.md`](AGENTS.md).
- Mẫu đầu ra tái sử dụng nằm trong [`reports/RESEARCH_REPORT_TEMPLATE.md`](reports/RESEARCH_REPORT_TEMPLATE.md).
- Mỗi paper nên có một định danh ổn định trong tên file, ưu tiên arXiv ID hoặc DOI đã chuẩn hóa khi đã kiểm chứng.
- Ghi `không được báo cáo` hoặc `chưa kiểm tra được` thay vì suy đoán dữ kiện thiếu.
- Không ghi đè paper, metadata, note, matrix, experiment hoặc report hiện có nếu chưa xác nhận phạm vi thay đổi.

## Custom skills hiện có

- `bci-paper-auditor`: audit chuyên sâu một paper PDF.
- `bci-literature-review`: tổng hợp và so sánh một tập hợp paper.
- `bci-citation-audit`: kiểm tra claim–evidence alignment và metadata trích dẫn.

Không sửa các skill này khi thực hiện tác vụ nghiên cứu thông thường, trừ khi người dùng yêu cầu cập nhật skill.
