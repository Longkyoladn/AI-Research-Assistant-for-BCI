# Paper arXiv về neural interface hỗ trợ người có vấn đề thần kinh

Ngày tìm kiếm: 2026-11-16  
Nguồn: arXiv MCP Server (`search_papers`, sau đó `get_abstract`)  
Phạm vi đánh giá ở bước này: metadata và abstract; chưa dùng full text để kết luận hiệu quả lâm sàng.

## Danh sách đã xác minh

| arXiv ID | Paper | Tác giả | Năm | Modality / phạm vi liên quan |
|---|---|---|---:|---|
| [2306.03159](https://arxiv.org/abs/2306.03159) | The feasibility of combining communication BCIs with FES for individuals with locked-in syndrome | Evan Canny; Mariska J. Vansteensel; Sandra M. A. van der Salm; Gernot R. Müller-Putz; Julia Berezutskaya | 2023 | Review về communication BCI và FES cho locked-in syndrome; bao phủ attempted hand/speech movement, vận động chi/mặt và giao tiếp. |
| [2310.00266](https://arxiv.org/abs/2310.00266) | Is controlling a brain-computer interface just a matter of presence of mind? The limits of cognitive-motor dissociation | Perrine Seguin; Emmanuel Maby; Fabien Perrin; Alessandro Farnè; Jérémie Mattout | 2023 | Review/hypothesis về ảnh hưởng của tổn thương motor structures lên attention và khả năng điều khiển BCI ở complete locked-in syndrome. |
| [1908.10773](https://arxiv.org/abs/1908.10773) | The N400 for Brain Computer Interfacing: complexities and opportunities | Karen Dijkstra; Jason Farquhar; Peter Desain | 2019 | N400/EEG cho semantic processing; nêu ứng dụng phát hiện xử lý ngôn ngữ ở disorders of consciousness và thăm dò nội dung tâm trí. |
| [2506.12817](https://arxiv.org/abs/2506.12817) | Magnetoencephalography (MEG) Based Non-Invasive Chinese Speech Decoding | Zhihong Jia; Hongbin Wang; Yuanzhong Shen; Feng Hu; Jiayu An; Kai Shu; Dongrui Wu | 2025 | MEG không xâm lấn, speech decoding tiếng Trung; abstract định vị ứng dụng cho aphasia. Đây là MEG, không được suy rộng sang scalp EEG/ECoG. |
| [2505.00219](https://arxiv.org/abs/2505.00219) | Real-Time Brain-Computer Interface Control of Walking Exoskeleton with Bilateral Sensory Feedback | Jeffrey Lim; Po T. Wang; Won Joon Sohn; Derrick Lin; Shravan Thaploo; Luke Bashford; David Bjanes; Angelica Nguyen; Hui Gong; Michelle Armacost; Susan J. Shaw; Spencer Kellis; Brian Lee; Darrin Lee; Payam Heydari; Richard A. Andersen; Zoran Nenadic; Charles Y. Liu; An H. Do | 2025 | Bidirectional invasive BCI dùng subdural ECoG để điều khiển exoskeleton và tạo sensory feedback hai chân; nghiên cứu proof-of-concept trên một người đang được đánh giá phẫu thuật epilepsy, không phải thử nghiệm trên cohort SCI. |
| [2104.07062](https://arxiv.org/abs/2104.07062) | Decoding of the Walking States and Step Rates from Cortical Electrocorticogram Signals | Po T. Wang; Colin M. McCrimmon; Susan J. Shaw; Hui Gong; Luis A. Chui; Payam Heydari; Charles Y. Liu; An H. Do; Zoran Nenadic | 2021 | ECoG, offline, within-subject ở hai người có khả năng đi; giải mã walking state và step rate nhằm hướng tới prosthesis cho SCI. Không phải minh chứng online ở người SCI. |
| [1209.1859](https://arxiv.org/abs/1209.1859) | Operation of a Brain-Computer Interface Walking Simulator by Users with Spinal Cord Injury | Christine E. King; Po T. Wang; Luis A. Chui; An H. Do; Zoran Nenadic | 2012 | Scalp EEG và kinesthetic motor imagery; online control avatar đi bộ trong virtual environment ở 5 người SCI. Đây là simulator, chưa phải phục hồi đi bộ vật lý. |
| [2205.06090](https://arxiv.org/abs/2205.06090) | NeuralTree: A 256-Channel 0.227-μJ/Class Versatile Neural Activity Classification and Closed-Loop Neuromodulation SoC | Uisub Shin; Cong Ding; Bingzhao Zhu; Yashwanth Vyza; Alix Trouillet; Emilie C. M. Revol; Stéphanie P. Lacour; Mahsa Shoaran | 2022 | Closed-loop neural interface SoC; đánh giá trên EEG/iEEG epilepsy datasets, μECoG ở rat và LFP tremor Parkinson. Không phải communication BCI. |

## Ghi chú diễn giải

- `Nhận thức/tư duy` không phải một modality. Các paper 2310.00266 và 1908.10773 liên quan gần nhất đến attention, semantic processing và disorders of consciousness, nhưng chủ yếu là review/hypothesis chứ không phải thử nghiệm phục hồi nhận thức.
- `Ngôn ngữ/giao tiếp`: 2306.03159 và 2506.12817 phù hợp trực tiếp hơn; cần giữ riêng kết luận của MEG, EEG và invasive recordings.
- `Vận động`: 2505.00219, 2104.07062 và 1209.1859 khác nhau rõ về invasive/non-invasive, online/offline và đối tượng; không gộp các kết quả như thể cùng một mức bằng chứng.
- `Neuromodulation`: 2205.06090 nhắm tới phát hiện trạng thái bệnh và kích thích closed-loop, khác với hệ decoding ý định để giao tiếp hoặc điều khiển thiết bị.

## Paper được chuyển sang quy trình đọc sâu

Chọn `2306.03159` vì đây là paper bao phủ trực tiếp nhất mối nối giữa communication/language và motor restoration ở locked-in syndrome. PDF arXiv v2 đã được lưu mới vào `papers/raw/` và khởi tạo tại `knowledge/paper-notes/canny-2023-communication-bci-fes/`. Theo `bci-paper-reader`, phân tích chỉ được tạo sau khi bản dịch toàn văn đạt kiểm tra độ phủ.
