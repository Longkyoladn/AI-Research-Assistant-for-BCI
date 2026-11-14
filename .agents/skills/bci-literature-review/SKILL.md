---
name: bci-literature-review
description: Thực hiện literature review có cấu trúc từ một tập hợp paper về neuroscience, BCI, EEG và neural decoding; xây dựng literature matrix, tổng hợp bằng chứng, so sánh phương pháp và xác định research gaps. Dùng khi người dùng yêu cầu tổng quan hoặc đối chiếu nhiều bài báo; chỉ gọi là systematic review khi có protocol phù hợp, và không dùng thay cho audit chuyên sâu một paper đơn lẻ.
---

# BCI Literature Review

Tổng hợp tập hợp paper mà người dùng cung cấp thành literature review khoa học bằng tiếng Việt và comparison matrix trong `reports/`. Giữ thuật ngữ kỹ thuật tiếng Anh khi cần độ chính xác.

## Input và routing

- Input tối thiểu là research question hoặc chủ đề cùng một corpus gồm nhiều paper. Ghi riêng paper do người dùng cung cấp, paper tìm từ nguồn ngoài và trạng thái truy cập của từng paper.
- Nếu chỉ phân tích toàn văn một paper, dùng `bci-paper-auditor`. Nếu mục tiêu chính là kiểm tra claim–citation alignment hoặc bibliography, dùng `bci-citation-audit`.
- Khi external search được phép, dùng arXiv Plugin cho discovery, metadata, abstract và source retrieval; skill này chịu trách nhiệm scope, literature matrix, compatibility analysis và synthesis.

## Phạm vi và bằng chứng

- Xác định research question, population, task, modality, outcomes, khoảng thời gian và tiêu chí inclusion/exclusion từ yêu cầu; nếu còn thiếu, nêu rõ phạm vi làm việc đã chọn.
- Mặc định chỉ dùng corpus được cung cấp và tài liệu thực sự truy cập được. Chỉ mở rộng ra nguồn ngoài khi người dùng yêu cầu hoặc cho phép và công cụ hiện có kiểm tra được nguồn đó.
- Ghi rõ cách hình thành corpus, số tài liệu nhận được, số tài liệu đọc được, tài liệu bị loại và lý do. Nếu không tìm kiếm bên ngoài, tuyên bố rõ review chỉ bao phủ corpus được cung cấp; không gọi đó là exhaustive, systematic hoặc đại diện cho toàn lĩnh vực.
- Không suy đoán metadata hay kết quả bị thiếu. Mọi kết luận quan trọng phải liên kết tới paper cụ thể, DOI hoặc định danh đã kiểm tra và vị trí bằng chứng như trang, section, figure hoặc table khi có.
- Nêu rõ giới hạn nếu không thể truy cập full text, supplementary materials, figures, tables hoặc một phần tài liệu. Không dùng abstract-only evidence như thể đã kiểm tra toàn văn.
- Với paper arXiv, lưu versioned ID và trạng thái truy xuất. Search hit hoặc abstract chỉ hỗ trợ screening và kết luận trong phạm vi abstract; `citation_graph` chỉ thể hiện quan hệ trích dẫn, không chứng minh paper hỗ trợ một claim.
- Nếu arXiv Plugin không hoạt động, giữ review trong phạm vi corpus truy cập được và báo giới hạn; không tự cài package, fallback runtime hoặc MCP.

## Workflow

1. Chuẩn hóa danh mục paper: title, authors, year, venue, DOI/identifier, loại nghiên cứu, recording modality, trạng thái full text và phạm vi đã đọc.
2. Trích xuất theo cùng một schema: research aim, participants, experimental design/task, neural signals, acquisition, preprocessing, features, model/method, dataset, baselines, split/evaluation protocol, metrics, statistics, results, limitations và data/code availability.
3. Xây dựng literature matrix trước khi tổng hợp narrative. Dùng `không được báo cáo` hoặc `chưa kiểm tra được` cho ô thiếu; không ép các paper không tương thích vào cùng một trường kết luận.
4. Phân nhóm theo câu hỏi nghiên cứu và evidence thực tế, gồm EEG-based BCI, invasive BCI, neural decoding, cognition, brain connectivity hoặc nhóm khác phù hợp. Cho phép một paper thuộc nhiều nhóm và giải thích tiêu chí phân nhóm.
5. Phân tích tiến triển của phương pháp theo thời gian, điểm đồng thuận, kết quả mâu thuẫn, limitations và thay đổi về datasets, baselines hoặc evaluation practice.
6. Xác định research gaps từ matrix và đề xuất giả thuyết có khả năng kiểm chứng, kèm population, manipulation/comparison, measurable outcome và thiết kế kiểm định khả thi.

## Quy tắc so sánh

- Chỉ so sánh trực tiếp performance khi task, dataset/cohort, target definition, split unit, metric và evaluation protocol đủ tương đồng. Kiểm tra subject-dependent với subject-independent, within-session với cross-session và offline với online/closed-loop.
- Nếu không tương đồng, chỉ mô tả kết quả song song và giải thích confounders; không xếp hạng model hoặc tính chênh lệch gộp.
- Phân biệt statistical significance, effect size, predictive performance và practical/clinical significance.
- Không chuyển tương quan thành nhân quả. Trong narrative và evidence ledger, dùng nhất quán các loại **Experimental evidence**, **Author interpretation**, **Hypothesis** và **AI inference**; có thể ghi replicated/single-study như thuộc tính bổ sung của experimental evidence.
- Gán mức bằng chứng cho kết luận tổng hợp: **cao** khi nhiều nghiên cứu độc lập, phù hợp và trực tiếp hỗ trợ; **trung bình** khi bằng chứng trực tiếp nhưng ít hoặc có khác biệt; **thấp** khi chỉ một nghiên cứu, gián tiếp, abstract-only hoặc có confounders lớn. Luôn giải thích lý do, không dùng nhãn như một phép chấm điểm tự động.

## Đầu ra

Tạo hai file, không ghi đè file có sẵn nếu chưa được phép:

- `reports/<topic-slug>-literature-review.md`: research question và scope, corpus/method, thematic synthesis, method evolution, consensus, contradictions, limitations, research gaps, testable hypotheses và scope limitations.
- `reports/<topic-slug>-comparison-matrix.md`: một hàng cho mỗi paper và các trường metadata, modality, design, signals, methods, datasets, baselines, evaluation, metrics, results, limitations, reproducibility và evidence locations.

Có thể duy trì working matrix tại `knowledge/literature-matrix/<topic-slug>.md`; bản trong `reports/` là snapshot hoàn chỉnh đi kèm literature review. Không tự động ghi đè hoặc làm hai bản phân kỳ mà không ghi ngày/provenance.

Trong review, kèm evidence ledger ánh xạ từng kết luận quan trọng tới paper và vị trí bằng chứng, cùng confidence/evidence level. Trước khi hoàn tất, đối chiếu narrative với matrix, kiểm tra mọi so sánh trực tiếp theo compatibility rules và xác nhận không có tuyên bố vượt quá corpus đã kiểm tra.
