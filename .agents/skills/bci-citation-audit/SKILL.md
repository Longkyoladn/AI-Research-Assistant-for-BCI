---
name: bci-citation-audit
description: Kiểm tra nguồn, độ chính xác của trích dẫn và mức hỗ trợ bằng chứng cho các phát biểu trong báo cáo khoa học về BCI, EEG và neuroscience. Dùng khi người dùng yêu cầu citation audit, kiểm chứng tài liệu tham khảo, phát hiện unsupported claims hoặc đánh giá claim–evidence alignment; không dùng thay cho literature review tổng quát.
---

# BCI Citation Audit

Audit từng phát biểu khoa học trong tài liệu đích dựa trên các nguồn thực sự truy cập được. Xuất báo cáo tiếng Việt dạng Markdown vào `reports/`, giữ thuật ngữ kỹ thuật tiếng Anh khi cần.

## Input và routing

- Input tối thiểu là tài liệu đích cần audit và các nguồn/citation mà tài liệu viện dẫn. Ghi rõ nguồn được cung cấp, nguồn truy xuất bên ngoài và phần không truy cập được.
- Nếu mục tiêu là phân tích khoa học toàn văn của một paper, dùng `bci-paper-auditor`. Nếu mục tiêu là tổng hợp nhiều paper thành narrative và matrix, dùng `bci-literature-review`.
- Với nguồn arXiv, arXiv Plugin chịu trách nhiệm metadata/source retrieval; skill này chịu trách nhiệm kiểm tra entailment giữa claim và evidence.

## Phạm vi xác minh

- Lập danh mục mọi nguồn được trích dẫn và chuẩn hóa metadata từ chính nguồn đã kiểm tra: title, authors, year, venue, DOI và arXiv ID nếu có. Giữ nguyên trường chưa xác định là `UNVERIFIED`; không suy đoán hoặc tự tạo DOI, title, author, số liệu, URL hay reference.
- Ghi rõ nguồn nào chỉ được người dùng cung cấp, nguồn nào đã được xác minh bên ngoài và công cụ/địa điểm xác minh. Nếu không có Internet, MCP hoặc quyền truy cập phù hợp, không tuyên bố đã kiểm tra DOI, landing page, indexing record hay metadata bên ngoài.
- Với PDF cục bộ, kiểm tra full text có liên quan và chỉ rõ PDF page cùng printed page nếu khác nhau; thêm section, paragraph context, Figure, Table, Equation hoặc Methods/Results locator khi có.
- Nếu không đọc được trang, hình, bảng, supplementary material hoặc lớp text, nêu giới hạn cụ thể và không xem phần đó là đã xác minh.
- Với arXiv, ghi versioned ID. `get_abstract` chỉ xác minh metadata và nội dung abstract; dùng full text hoặc section liên quan trước khi xác minh claim về Methods/Results. `export_citations` không tự xác minh DOI nếu DOI không có trong metadata trả về, và `citation_graph` không chứng minh claim được hỗ trợ.
- Nếu arXiv Plugin không hoạt động, đánh dấu phần liên quan là `UNVERIFIED`; không tự cài package, fallback runtime hoặc MCP.

## Audit ở cấp phát biểu

Tách câu phức thành các atomic claims có thể kiểm tra. Với mỗi claim, ghi citation được dùng, bằng chứng tìm thấy, locator và hai chiều phân loại độc lập.

**Evidence type:**

- **Experimental evidence** — kết quả đo/ước lượng được nguồn báo cáo.
- **Author interpretation** — diễn giải hoặc kết luận của tác giả nguồn.
- **Hypothesis** — giả thuyết hoặc speculation chưa được kiểm chứng đầy đủ.
- **AI inference** — suy luận của người audit; nêu chuỗi suy luận, căn cứ, mức độ chắc chắn và không quy nó cho nguồn.

**Verification status:**

- **VERIFIED FROM PROVIDED SOURCE** — nguồn do người dùng cung cấp trực tiếp hỗ trợ đầy đủ claim.
- **EXTERNALLY VERIFIED** — nguồn bên ngoài đã được truy cập và kiểm tra trực tiếp hỗ trợ đầy đủ claim; ghi nguồn xác minh.
- **PARTIALLY SUPPORTED** — nguồn chỉ hỗ trợ một phần hoặc phạm vi hẹp hơn claim.
- **CONTRADICTED** — nguồn được kiểm tra mâu thuẫn với claim.
- **UNVERIFIED** — chưa có nguồn truy cập được, không tìm thấy bằng chứng, metadata chưa xác nhận hoặc bằng chứng không đủ.
- **NOT APPLICABLE** — nội dung không phải claim cần nguồn, chẳng hạn ghi chú quy trình; không dùng nhãn này để né tránh kiểm chứng một phát biểu khoa học.

Không đánh dấu `VERIFIED` chỉ vì citation tồn tại hoặc metadata khớp. Xác định rõ các trường hợp:

- đúng paper nhưng đoạn được trích không hỗ trợ claim;
- chỉ hỗ trợ một phần, khác population/task/dataset/outcome hoặc mạnh hơn ngôn ngữ trong nguồn;
- secondary source được dùng thay cho primary evidence;
- citation đặt sai vị trí, citation thiếu hoặc nhiều citation nhưng không rõ nguồn nào hỗ trợ phần nào;
- số liệu, direction, unit, denominator, confidence interval hoặc statistical result bị chép sai.

## Kiểm tra chuyên môn BCI/neuroscience

- Xác minh recording modality và không đánh đồng scalp EEG, fMRI, ECoG và intracortical recordings/BCI. Kiểm tra mức invasiveness, measured signal và giới hạn suy luận phù hợp với modality.
- Phân biệt association/correlation với causal evidence; đánh dấu causal wording không được thiết kế thí nghiệm hỗ trợ.
- Phân biệt offline decoding với online hoặc closed-loop BCI; không dùng offline performance làm bằng chứng trực tiếp cho real-time utility.
- Phân biệt within-subject, cross-session, cross-subject và subject-independent evaluation; kiểm tra split unit, leakage risk và phạm vi generalization.
- Kiểm tra task, cohort, dataset, target definition, baseline, metric và evaluation protocol trước khi chấp nhận claim so sánh performance.

## Workflow

1. Xác định tài liệu đích, corpus nguồn và phạm vi claim cần audit.
2. Chuẩn hóa bibliography mà không bổ sung metadata chưa kiểm chứng.
3. Lập claim ledger; ánh xạ từng atomic claim tới citation và exact evidence locator.
4. Đánh giá entailment: bằng chứng hỗ trợ đầy đủ, một phần, mâu thuẫn hay không liên quan.
5. Gắn evidence type và verification status riêng biệt, ghi severity/impact của vấn đề và đề xuất wording thận trọng hơn khi hữu ích.
6. Đối chiếu toàn bộ bibliography với in-text citations để phát hiện nguồn thừa, thiếu hoặc không truy cập được.

## Đầu ra

Tạo ba file và không ghi đè file có sẵn nếu chưa được phép:

- `reports/<document-slug>-citation-audit.md`: phạm vi, nguồn/công cụ đã dùng, summary, claim ledger với evidence type và verification status, modality/methodology checks và limitations.
- `reports/<document-slug>-unsupported-claims.md`: claim, vị trí trong tài liệu đích, citation liên quan, evidence type, verification status, lý do, severity và corrective action.
- `reports/<document-slug>-bibliography.md`: metadata đã chuẩn hóa, verification status, nguồn xác minh và các trường còn thiếu/xung đột.

Trước khi hoàn tất, kiểm tra rằng mỗi status `VERIFIED` có exact evidence locator, mỗi `EXTERNALLY VERIFIED` có nguồn ngoài thực sự đã mở, các claim được hỗ trợ một phần hoặc bị mâu thuẫn không bị gộp vào `UNVERIFIED`, và mọi khoảng trống truy cập đều được giữ là `UNVERIFIED`.
