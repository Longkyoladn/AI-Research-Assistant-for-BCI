# Quy tắc làm việc cho project

## Ngôn ngữ và phạm vi

- Mặc định trả lời và viết báo cáo bằng tiếng Việt; giữ thuật ngữ English khi cần độ chính xác.
- Phân biệt rõ scalp EEG, ECoG, intracortical recordings, fMRI và MEG; không chuyển kết luận giữa các modality nếu không có căn cứ.
- Không ghi đè skill, paper, metadata, note, dataset, experiment hoặc report hiện có nếu người dùng chưa cho phép.

## Tính toàn vẹn khoa học

- Không bịa thông tin, số liệu, citation, DOI, URL hoặc metadata. Đánh dấu dữ kiện thiếu là `không được báo cáo`, `chưa xác định` hoặc `chưa kiểm tra được`.
- Mỗi khẳng định khoa học quan trọng phải dẫn tới nguồn thực sự đã kiểm tra.
- Nếu chỉ có abstract, chỉ kết luận trong phạm vi abstract; không suy đoán chi tiết Methods, Results, figures, tables hoặc supplementary materials.
- Với PDF đã đọc, dẫn số trang PDF và số trang in nếu khác nhau; thêm section, Figure, Table hoặc Equation khi có.
- Phân loại rõ nội dung thành **Experimental evidence**, **Author interpretation**, **Hypothesis** và **AI inference**. Với AI inference, nêu căn cứ và mức độ chắc chắn.
- Phân biệt online với offline evaluation, within-subject với cross-subject/subject-independent evaluation, và correlation với causation.
- Trước khi so sánh performance, kiểm tra task, cohort/dataset, target, split unit, metric và evaluation protocol có đủ tương đồng hay không.

## Dữ liệu và quyền riêng tư

- Không sử dụng dữ liệu riêng tư hoặc dữ liệu có thể định danh người tham gia để truy vấn dịch vụ bên ngoài khi chưa được người dùng cho phép.
- Không upload raw EEG, clinical records, participant metadata hoặc credentials ra ngoài project nếu chưa có chấp thuận rõ ràng.
- Khi xử lý dữ liệu, ưu tiên bản đã de-identify và ghi lại provenance, preprocessing cùng các biến đổi có thể ảnh hưởng kết quả.

## Chuẩn đầu ra Markdown

- Lưu báo cáo trong `reports/` với tên dạng `<topic-or-paper-slug>-<report-type>.md`; không ghi đè file đã tồn tại nếu chưa được phép.
- Bắt đầu bằng metadata: tiêu đề, ngày tạo/cập nhật, research question, phạm vi corpus, modality và trạng thái truy cập nguồn.
- Dùng các mục tối thiểu: **Executive summary**, **Scope and sources**, **Methods/Approach**, **Evidence and findings**, **Limitations**, **Reproducibility**, **Open questions** và **References**.
- Dùng bảng cho literature matrix, experimental setup, claim audit hoặc evidence ledger. Mỗi hàng evidence cần có claim, evidence type, source, locator và confidence/status.
- Dẫn nguồn ngay sau claim và dùng định danh nhất quán. Không đưa nguồn chưa kiểm tra vào bibliography như thể đã xác minh.
- Kết thúc bằng mục **Không thể kiểm tra / Không được báo cáo** để công khai khoảng trống và giới hạn công cụ.
- Dùng `reports/RESEARCH_REPORT_TEMPLATE.md` làm khung mặc định, điều chỉnh theo loại báo cáo thay vì tạo các heading không liên quan.
