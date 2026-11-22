# Quy tắc làm việc cho project

Project hỗ trợ nghiên cứu BCI và tín hiệu thần kinh: tìm paper, đọc toàn văn, lưu kiến thức, rồi tái lập thực nghiệm.

## Thư mục

- `papers/raw/`: PDF bài báo và phụ lục.
- `knowledge/paper-notes/<slug>/`: bản dịch toàn văn và phân tích của từng paper.
- `reports/`: báo cáo tổng hợp nhiều paper.
- `datasets/`, `experiments/`: dữ liệu và code thực nghiệm.
- `scripts/`: công cụ của project.

## Chọn skill

- Đọc, dịch, tìm hiểu một paper: `bci-paper-reader` (mặc định).
- Tổng hợp, so sánh nhiều paper: `bci-literature-review`.
- `bci-paper-auditor` và `bci-citation-audit`: chỉ khi người dùng gọi đích danh.

## Quy tắc chung

- Trả lời và viết bằng tiếng Việt; giữ thuật ngữ English.
- Khi yêu cầu hiện tại liên quan đến một paper đã được lưu trong `knowledge/paper-notes/<slug>/`, phải nạp file `90-phan-tich.md` tương ứng làm kiến thức nền cho cuộc trò chuyện trước khi trả lời hoặc thực hiện công việc tiếp theo.
- Nếu `90-phan-tich.md` chưa tồn tại, dùng `00-index.md` và các file bản dịch section hiện có làm context. Khi cần số liệu, citation hoặc phát biểu chính xác, phải đối chiếu lại khối nguồn `¶ main-p...`, trang, Figure hoặc Table trong bản dịch/PDF; không coi phần nhận định AI trong `90-phan-tich.md` là lời của tác giả.
- Nếu có nhiều paper liên quan, chỉ nạp các file phân tích phù hợp trực tiếp với câu hỏi; dùng `bci-literature-review` khi nhiệm vụ yêu cầu tổng hợp hoặc so sánh nhiều paper.
- Không bịa thông tin, số liệu, citation, DOI, URL. Dữ kiện thiếu ghi `không được báo cáo` hoặc `chưa kiểm tra được`.
- Nội dung lấy từ paper phải trỏ được về vị trí trong nguồn (khối, trang, Figure, Table). Lời của AI phải tách bạch với lời tác giả.
- Chỉ có abstract thì chỉ nói trong phạm vi abstract.
- Phân biệt scalp EEG, ECoG, intracortical recordings, fMRI, MEG; không chuyển kết luận giữa các modality. Phân biệt online với offline, within-subject với cross-subject.
- Không ghi đè paper, note, report, dataset, experiment hiện có khi chưa được phép.
- Không gửi raw data, thông tin người tham gia hoặc credentials ra dịch vụ bên ngoài khi chưa được phép.
