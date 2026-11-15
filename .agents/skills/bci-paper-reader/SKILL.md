---
name: bci-paper-reader
description: Dịch toàn văn trung thành một paper (PDF trong papers/raw hoặc tải qua arXiv Plugin) sang tiếng Việt theo từng đoạn, giữ thuật ngữ English kèm chú giải ngay bên cạnh, lưu hình, bảng, công thức đầy đủ; sau khi bản dịch qua kiểm tra độ phủ thì viết phần phân tích. Dùng khi người dùng muốn đọc, đọc sâu, dịch, bóc tách hoặc tìm hiểu nội dung một bài báo. Đây là skill mặc định cho một paper đơn lẻ.
---

# BCI Paper Reader

Mục tiêu: người dùng đọc thư mục kết quả thay cho PDF mà không mất câu nào, số nào, hình nào của bài báo. Đây không phải tóm tắt. Skill chạy theo nhiều lượt; mỗi lượt làm một phần rồi dừng, trạng thái nằm trên đĩa.

Công cụ: `.venv\Scripts\python scripts\paper_tools.py <lệnh>` (lệnh: `prepare`, `crop`, `status`, `check`). Nếu `.venv` chưa có: `uv venv .venv` rồi `uv pip install --python .venv -r requirements.txt`.

Thư mục kết quả `knowledge/paper-notes/<slug>/`, với `<slug>` dạng `<tác-giả-đầu>-<năm>-<vài-từ-khóa>`:

```text
00-index.md       metadata, nguồn, tiến độ dịch, danh sách phụ lục
NN-<section>.md   bản dịch, mỗi section của bài báo một file, đúng thứ tự gốc
figures/          fig-1.png, table-1.png, fig-s3.png ...
glossary.md       mọi thuật ngữ đã chú giải
90-phan-tich.md   chỉ tạo ở giai đoạn 2
source/           text gốc theo khối và ảnh từng trang (do prepare tạo, không sửa tay)
```

## Mỗi lượt bắt đầu thế nào

1. Nếu thư mục paper chưa có: làm **Lượt chuẩn bị**.
2. Nếu đã có: chạy `status <slug>`, đọc `00-index.md` và `glossary.md`, rồi làm **Lượt dịch** cho phần chưa xong kế tiếp.
3. Nếu `check <slug>` (không kèm `--pages`) trả `KET QUA: DAT`: làm **Giai đoạn 2**, trừ khi `90-phan-tich.md` đã tồn tại.

## Lượt chuẩn bị

1. Xác định PDF. Paper arXiv thì tải bằng arXiv Plugin vào `papers/raw/`; paper khác thì dùng file có sẵn trong `papers/raw/`. Không có PDF thì dừng và yêu cầu người dùng cung cấp.
2. `prepare <pdf> <slug>`. Lệnh từ chối ghi đè; nếu slug đã tồn tại thì dùng slug đó để tiếp tục, không tạo bản mới.
3. Xem ảnh các trang trong `source/pages/` để nắm bố cục, rồi điền `00-index.md`: metadata đọc từ chính PDF, bảng Nguồn, và bảng Tiến độ dịch với mọi section theo đúng thứ tự bài báo (file, tên section, trang PDF, trạng thái `chưa dịch`).
4. Điền bảng **Phụ lục bài báo nhắc tới**: mọi Supplementary Appendix, Supplementary Information, Extended Data, Protocol, Appendix, video, dataset mà bài báo nêu. Trạng thái mỗi mục: `có trong papers/raw` hoặc `chưa có`. Mục nào có file PDF thì chạy `prepare <pdf> <slug> --part supp` (phụ lục thứ hai: `supp2`) và thêm các section của nó vào bảng Tiến độ dịch. Không tự vượt cơ chế chặn tải của nhà xuất bản.
5. Dừng. Báo người dùng: số trang, số section, phụ lục nào còn thiếu cần tải tay.

## Lượt dịch

Mỗi lượt dịch tối đa khoảng 4 trang PDF, kết thúc ở ranh giới section nếu được.

1. Đọc text gốc của các trang đó trong `source/<part>.txt` và **xem ảnh trang tương ứng** trong `source/pages/` để thấy bố cục, hình, bảng, công thức, chỉ số trên/dưới mà text không thể hiện.
2. Viết bản dịch vào file section tương ứng theo quy tắc bên dưới.
3. Chạy `check <slug> --pages <các trang vừa làm>`. Sửa đến khi `DAT`. Mỗi lỗi là một khối chưa dịch, một con số bị thiếu, một đoạn bị lược hoặc một hình chưa lưu; sửa đúng chỗ đó, không sửa bằng cách thêm số vào cho qua.
4. Cập nhật `glossary.md` và bảng Tiến độ dịch trong `00-index.md`.
5. Dừng và báo: đã xong trang nào, còn lại gì.

### Quy tắc dịch

- **Mọi khối trong nguồn phải được xử lý.** Mỗi đoạn dịch mở đầu bằng định danh khối: `**¶ main-p03-07**`. Đoạn gốc bị ngắt qua cột hoặc trang thì dịch liền và ghi `**¶ main-p03-08 + main-p04-02**`.
- **Dịch đủ từng câu** theo đúng thứ tự. Không gộp câu, không lược mệnh đề, không diễn đạt lại cho gọn, không thêm ý. Câu khó hiểu trong bản gốc thì dịch sát, không tự làm rõ thay tác giả.
- **Thuật ngữ chuyên ngành giữ nguyên English**, chú giải tiếng Việt ngay sau nó trong `⟦…⟧` ở lần đầu xuất hiện trong mỗi file section. Ví dụ: `high-gamma activity ⟦hoạt động ở dải tần 70–150 Hz của tín hiệu điện vỏ não, phản ánh hoạt động của quần thể neuron ngay dưới điện cực⟧`. Chú giải là giải thích kiến thức nền ngắn gọn; không nhận xét về bài báo. Dùng cùng một cách chú giải cho cùng một thuật ngữ, theo `glossary.md`.
- **Số liệu, đơn vị, ký hiệu, tên riêng, tên model, tên dataset** giữ nguyên như bản gốc. Số trích dẫn giữ nguyên dạng `[18]`.
- **Tiêu đề section và subsection** giữ English, kèm bản dịch trong ngoặc.
- **Khối không phải nội dung** (running header, footer, số trang, dòng bản quyền, chữ nằm trong hình): không dịch nhưng phải khai báo kèm lý do: `<!-- skip main-p03-01, main-p03-10: running header và footer -->`. Thông tin tác giả, affiliation, funding, acknowledgments, data availability là nội dung, phải dịch.
- **Hình:** với mỗi Figure, dùng `crop <slug> <part> <trang> x0 y0 x1 y1 fig-N` (tọa độ 0..1 theo chiều rộng và cao của trang; ước lượng từ ảnh trang, xem lại file kết quả và cắt lại nếu lẹm). Chèn `![Figure N](figures/fig-N.png)` tại vị trí hình trong bài, ngay sau đó là caption dịch đủ. Hình phụ lục đặt tên `fig-sN`.
- **Bảng:** cắt ảnh `table-N` như hình và chèn vào, rồi đánh lại toàn bộ bảng bằng Markdown, đủ mọi hàng, cột, chú thích chân bảng.
- **Công thức:** đánh lại bằng LaTeX (`$$…$$`), giữ số thứ tự công thức, đối chiếu với ảnh trang chứ không chỉ text trích. Giải thích ký hiệu chỉ khi bài báo có giải thích.
- **References:** chép nguyên văn, không dịch; mỗi khối vẫn mang định danh.
- Ngoài phần trong `⟦…⟧`, bản dịch không chứa lời nào của AI: không tóm tắt, không nhận xét, không nhãn phân loại, không mục "limitations" tự thêm.
- Chỗ không đọc được (ảnh mờ, ký hiệu lỗi font) ghi `[không đọc được: …]` tại chỗ và trong `00-index.md`; không đoán.

## Giai đoạn 2: Phân tích

Chỉ làm khi `check <slug>` toàn bộ trả `DAT`. Nếu chưa đạt, quay lại dịch và nói rõ còn thiếu gì. Phụ lục `chưa có` không chặn giai đoạn 2, nhưng phải ghi ở đầu file rằng phân tích chỉ dựa trên phần đã dịch.

Viết `90-phan-tich.md`, làm việc từ bản dịch. Mỗi ý phải ghi một trong ba loại nguồn:

- `(¶ main-p05-03)` — bài báo nói điều này; trỏ tới khối cụ thể.
- `(nguồn ngoài: <định danh>)` — paper khác đã thực sự mở được qua arXiv Plugin hoặc có trong `papers/raw/`.
- `[Nhận định AI]` — suy luận của model; không gán cho tác giả.

Các mục cố định:

1. **Câu hỏi nghiên cứu và đóng góp chính** mà tác giả tuyên bố.
2. **Cải thiện so với công nghệ trước đó**: bài này làm được gì mà công trình trước chưa làm được.
3. **Pipeline dạng các bước triển khai**, từ tín hiệu thô tới output; bảng tham số đã có giá trị và tham số còn thiếu để tái lập.
4. **Dataset và code**: dữ liệu gì, bao nhiêu, có công khai không, lấy ở đâu.
5. **Kết quả chính kèm điều kiện đánh giá**: metric, online hay offline, within-subject hay cross-subject, so với baseline nào.
6. **Độ mạnh của bằng chứng**: cỡ mẫu, thống kê; tuyên bố nào được số liệu đỡ trực tiếp, tuyên bố nào là ngoại suy.
7. **Ứng dụng**: có thể dùng vào đâu.
8. **Các hướng nghiên cứu tương tự.**
9. **Hạn chế và phần chưa nghiên cứu**: tách phần tác giả tự nêu với phần model nhận thấy.

Chỉ làm khi người dùng yêu cầu: kiến thức nền cần có; bài nên đọc tiếp từ References; so sánh với paper khác trong corpus (chỉ khi task, modality và cách đánh giá đủ tương đồng); ý tưởng thí nghiệm tiếp theo; liên hệ với câu hỏi nghiên cứu riêng của người dùng; an toàn, đạo đức, triển khai lâm sàng.

Mục nào bài báo không có thông tin thì ghi `không được báo cáo`, không lấp bằng kiến thức chung.
