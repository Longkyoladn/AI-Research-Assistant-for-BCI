# Khả năng ứng dụng BCI cho rối loạn ngôn ngữ và nhận thức do bệnh thần kinh

| Trường | Giá trị |
|---|---|
| Ngày tạo/cập nhật | 2026-11-14 |
| Research question | BCI có thể hỗ trợ hoặc phục hồi giao tiếp/ngôn ngữ và nhận thức ở người có bệnh/tổn thương thần kinh tới mức nào? |
| Phạm vi corpus | Scoping review định hướng gồm 10 bài nghiên cứu và 2 review/clinical-trial overview; ưu tiên nghiên cứu trên người và ứng dụng phục hồi chức năng |
| Recording modality | scalp EEG, ECoG, intracortical recordings; một số hệ closed-loop dùng intracranial recordings + stimulation |
| Trạng thái nguồn | Metadata và abstract/full article webpage đã kiểm tra; chưa audit toàn văn từng PDF |

## Executive summary

BCI hiện có tiềm năng rõ nhất trong **khôi phục giao tiếp** cho người bị liệt nặng nhưng còn bảo tồn phần lớn năng lực ngôn ngữ và nhận thức. Các speech neuroprosthesis dùng ECoG hoặc intracortical recordings đã giải mã attempted speech thành text, audio và avatar trong thời gian thực, nhưng phần lớn mới là early-feasibility, thường chỉ 1 người tham gia và cần phẫu thuật cấy ghép.

Đối với **phục hồi ngôn ngữ sau stroke/aphasia**, scalp-EEG BCI neurofeedback có tín hiệu khả quan nhưng bằng chứng còn nhỏ và thiếu đối chứng mạnh. Một proof-of-concept 10 người báo cáo cải thiện trên nhiều thang ngôn ngữ; một nghiên cứu P300 khác chỉ còn 7 người hoàn thành và không loại trừ được hiệu ứng không đặc hiệu.

Đối với **nhận thức/memory**, closed-loop intracranial stimulation đã cải thiện encoding/recall trong các nghiên cứu proof-of-concept ở bệnh nhân epilepsy đang được đặt điện cực vì chỉ định lâm sàng. EEG neurofeedback ở mild cognitive impairment (MCI) cũng có kết quả dương tính trong một RCT nhỏ, nhưng chưa đủ để kết luận hiệu quả điều trị dementia hay phục hồi nhận thức nói chung.

Kết luận thực hành: đây là hướng rất triển vọng, nhưng chưa nên diễn giải là BCI đã “chữa” rối loạn ngôn ngữ hoặc nhận thức. Bằng chứng hiện tại mạnh hơn cho **assistive compensation** (bù chức năng giao tiếp) so với **restorative recovery** (phục hồi chính chức năng thần kinh).

## Scope and sources

### Tiêu chí đưa vào

- Nghiên cứu trên người hoặc review trực tiếp về BCI/neuroprosthesis cho communication, aphasia, memory hoặc cognitive impairment.
- Có population thần kinh rõ ràng (ALS, brainstem stroke, aphasia, MCI, epilepsy) hoặc có giá trị trực tiếp cho feasibility lâm sàng.
- Ưu tiên primary study; review được giữ để định hướng toàn lĩnh vực và clinical translation.

### Tiêu chí loại/trì hoãn

- Decoding speech/cognition chỉ ở người khỏe mạnh, không có cầu nối rõ tới rehabilitation.
- BCI chỉ phục hồi vận động, không đo language/cognition.
- Nghiên cứu chỉ là protocol chưa có kết quả được tách khỏi evidence of efficacy.
- Không gộp scalp EEG, ECoG và intracortical recordings thành một mức xâm lấn hoặc một mức performance.

Nguồn discovery gồm arXiv và tìm kiếm web học thuật; metadata/abstract được đối chiếu trên trang journal hoặc PubMed. Đây không phải systematic review và không bảo đảm bao phủ toàn bộ lĩnh vực.

## Methods / Approach

Corpus được phân nhóm theo mục tiêu chức năng: (1) assistive communication/speech neuroprosthesis; (2) aphasia/language rehabilitation; (3) cognitive rehabilitation và memory prosthesis. Mỗi nghiên cứu được ghi modality, population, thiết kế, outcome và giới hạn. Performance không được xếp hạng trực tiếp khi vocabulary, task, participant, signal modality hoặc evaluation protocol khác nhau.

## Evidence and findings

### Experimental evidence

#### 1. Khôi phục giao tiếp ở paralysis/anarthria

- Moses et al. (2021) dùng high-density subdural ECoG ở **một** người bị brainstem stroke, anarthria và spastic quadriparesis. Hệ giải mã câu real-time đạt median 15.2 words/min và median word error rate (WER) 25.6% với vocabulary 50 từ. Đây là feasibility của communication restoration, không phải phục hồi mô não hay language network ([NEJM, Abstract/Methods/Results](https://www.nejm.org/doi/full/10.1056/NEJMoa2027540)).
- Willett et al. (2023) dùng bốn intracortical microelectrode arrays ở **một** người ALS, đạt 9.1% WER với 50 từ và 23.8% WER với vocabulary 125,000 từ. Bài báo cho thấy attempted-speech decoding có thể tiến gần conversational rate, nhưng external validity còn rất hạn chế ([Nature, Abstract](https://www.nature.com/articles/s41586-023-06377-x)).
- Metzger et al. (2023) dùng 253-channel high-density ECoG ở **một** người liệt nặng sau brainstem stroke; hệ tạo text, synthesized speech và facial avatar, với median 78 words/min và median WER 25% cho text. Đây là multimodal communication prosthesis, không phải điều trị aphasia ([Nature, Abstract](https://www.nature.com/articles/s41586-023-06443-4)).
- Metzger et al. (2022) cho thấy cùng hướng ECoG có thể spelling bằng attempted silent speech, mở rộng vocabulary theo kiểu letter-by-letter; vẫn là single-participant clinical-trial evidence ([Nature Communications, Abstract/Discussion](https://www.nature.com/articles/s41467-022-33611-3)).
- Card et al. (2026) báo cáo long-term independent use của intracortical BCI cho speech và cursor ở một người ALS, quan trọng cho chuyển dịch từ lab sang sử dụng tại nhà; tính khái quát và độ bền thiết bị vẫn cần nhiều người tham gia hơn ([Nature Medicine, article webpage](https://www.nature.com/articles/s41591-026-04414-6)).

#### 2. Phục hồi aphasia/language sau stroke

- Musso et al. (2022) triển khai scalp-EEG BCI feedback trong language training cường độ cao ở 10 người chronic post-stroke aphasia. Tác giả báo cáo cải thiện từ trung bình đến lớn trên nhiều thang ngôn ngữ (Aachen Aphasia Test standardized mean difference 0.63), nhưng thiết kế proof-of-concept nhỏ không đủ để tách chắc chắn hiệu ứng BCI khỏi intensity, practice và các yếu tố không đặc hiệu ([PubMed/Brain Communications abstract](https://pubmed.ncbi.nlm.nih.gov/35178518/)).
- Nghiên cứu visual P300 BCI năm 2024 tuyển 12 người chronic post-stroke aphasia nhưng chỉ 7 hoàn thành; spontaneous speech tăng, song tác giả nêu rõ specificity chưa xác định và không loại trừ hiệu ứng không đặc hiệu ([PubMed abstract](https://pubmed.ncbi.nlm.nih.gov/38873652/)).

#### 3. Memory/cognitive restoration

- Ezzyat et al. (2018) dùng closed-loop direct brain stimulation ở bệnh nhân epilepsy có intracranial electrodes: decoder nhận biết trạng thái encoding kém và stimulation lateral temporal cortex cải thiện later recall. Đây là causal intervention ngắn hạn trong task, chưa phải bằng chứng điều trị dementia hoặc cognitive impairment rộng ([Nature Communications, Abstract](https://www.nature.com/articles/s41467-017-02753-0)).
- Hampson et al. (2018) xây dựng hippocampal MIMO model từ CA3–CA1 spiking và dùng pattern-based stimulation để hỗ trợ encoding/recall ở bệnh nhân epilepsy được cấy điện cực. Đây là human proof-of-concept cho memory prosthesis nhưng population không phải Alzheimer’s disease và electrode placement phụ thuộc chỉ định lâm sàng ([PubMed/PMC](https://pubmed.ncbi.nlm.nih.gov/29589592/)).
- Lavy et al. (2021) thực hiện randomized sham-controlled EEG neurofeedback ở người MCI và báo cáo cải thiện memory duy trì ít nhất một tháng. Cần đọc toàn văn để kiểm tra sample size, multiplicity, effect size và risk of bias trước khi dùng cho quyết định lâm sàng ([PubMed abstract](https://pubmed.ncbi.nlm.nih.gov/34194315/)).

### Author interpretation

Các nhóm speech neuroprosthesis cho rằng độ phân giải cao của invasive recordings và mô hình language/speech hiện đại có thể tạo communication gần tự nhiên. Các nhóm aphasia và MCI cho rằng brain-state-contingent feedback có thể thúc đẩy plasticity. Đây là diễn giải hợp lý nhưng chưa được xác nhận bằng multi-center trials đủ lớn.

### Hypothesis

- Closed-loop feedback đúng thời điểm có thể hiệu quả hơn open-loop training vì reinforcement gắn với trạng thái thần kinh mục tiêu.
- Hybrid systems kết hợp BCI với speech-language therapy có thể tạo generalization tốt hơn so với BCI hoặc therapy đơn độc.
- Personalized decoders và co-adaptation có thể giảm thời gian calibration, nhưng cũng làm tăng nguy cơ overfitting theo từng người.

### AI inference

- **Độ chắc chắn trung bình:** BCI có khả năng tạo lợi ích chức năng thực tế cho communication trong một số trường hợp paralysis/anarthria, vì nhiều nhóm độc lập đã cho real-time online decoding; tuy nhiên số người tham gia còn cực nhỏ và modality xâm lấn.
- **Độ chắc chắn thấp–trung bình:** scalp-EEG BCI có thể hỗ trợ aphasia rehabilitation, nhưng hiện chưa rõ phần hiệu quả riêng của closed-loop neural feedback so với training intensity và expectancy.
- **Độ chắc chắn thấp:** memory prosthesis có thể chuyển sang MCI/AD; bằng chứng hiện có chủ yếu từ epilepsy patients trong bối cảnh monitoring xâm lấn và task memory ngắn hạn.

## Evidence ledger

| Claim | Loại | Source | Locator | Status/confidence |
|---|---|---|---|---|
| Invasive BCI có thể giải mã attempted speech real-time thành câu ở paralysis/anarthria | Experimental evidence | Moses 2021; Willett 2023; Metzger 2023 | Abstract/Results trên journal webpage | Trung bình; lặp lại giữa nhiều nhóm nhưng chủ yếu n=1 mỗi study |
| Speech BCI hiện chủ yếu bù giao tiếp, không chứng minh phục hồi language network | AI inference | Các study speech neuroprosthesis | Population và intervention | Cao |
| EEG-BCI language training có tín hiệu cải thiện chronic aphasia | Experimental evidence | Musso 2022; P300 study 2024 | Abstract | Thấp–trung bình; sample nhỏ, control hạn chế |
| Closed-loop intracranial stimulation có thể cải thiện memory-task performance | Experimental evidence | Ezzyat 2018; Hampson 2018 | Abstract/full article webpage | Trung bình cho task ngắn hạn; thấp cho general clinical restoration |
| EEG neurofeedback có thể cải thiện memory ở MCI | Experimental evidence | Lavy 2021 | Abstract | Thấp; một RCT nhỏ, cần replication |

## Limitations and threats to validity

- Communication studies thường là single-participant early-feasibility trials; không suy rộng được cho mọi ALS, stroke hoặc locked-in syndrome.
- Aphasia có heterogeneity lớn về lesion, severity, chronicity và residual comprehension; outcome giữa các study không tương thích hoàn toàn.
- Memory studies trên epilepsy patients không đại diện trực tiếp cho MCI/AD, traumatic brain injury hoặc post-stroke cognitive impairment.
- WER và words/min không so sánh trực tiếp nếu vocabulary, sentence set, language model và online protocol khác nhau.
- Invasive signal quality cao hơn scalp EEG nhưng kèm surgical/device risks; không nên chuyển performance giữa modalities.

## Reproducibility

Metzger et al. (2023) công bố code và source data; participant-level neural data bị restricted vì clinical-trial privacy. Nhiều study khác cần kiểm tra toàn văn/supplement để đánh giá code, preprocessing, splits, calibration và adverse events. Corpus này chưa thực hiện risk-of-bias tool chính thức.

## Open questions

- Liệu speech neuroprosthesis giữ accuracy và calibration ổn định nhiều năm, khi dùng độc lập ngoài lab?
- Với aphasia, sham-feedback hoặc active-control trial có cho thấy lợi ích riêng của neural contingency không?
- Kết quả language có generalize từ test sang conversation, participation và quality of life không?
- Với cognition, closed-loop EEG/neurostimulation có tạo lợi ích dài hạn trên everyday function, không chỉ laboratory task?
- Có thể phát triển non-invasive systems đủ chính xác cho người có cognitive impairment nặng mà vẫn giảm burden và fatigue không?

## References

1. Moses DA et al. Neuroprosthesis for Decoding Speech in a Paralyzed Person with Anarthria. *N Engl J Med*. 2021;385:217–227. DOI: [10.1056/NEJMoa2027540](https://doi.org/10.1056/NEJMoa2027540).
2. Willett FR et al. A high-performance speech neuroprosthesis. *Nature*. 2023;620:1031–1036. DOI: [10.1038/s41586-023-06377-x](https://doi.org/10.1038/s41586-023-06377-x).
3. Metzger SL et al. A high-performance neuroprosthesis for speech decoding and avatar control. *Nature*. 2023;620:1037–1046. DOI: [10.1038/s41586-023-06443-4](https://doi.org/10.1038/s41586-023-06443-4).
4. Metzger SL et al. Generalizable spelling using a speech neuroprosthesis in an individual with severe limb and vocal paralysis. *Nat Commun*. 2022;13:6510. DOI: [10.1038/s41467-022-33611-3](https://doi.org/10.1038/s41467-022-33611-3).
5. Card NS et al. Long-term independent use of an intracortical brain–computer interface for speech and cursor control. *Nat Med*. 2026. [Journal page](https://www.nature.com/articles/s41591-026-04414-6).
6. Musso M et al. Aphasia recovery by language training using a brain-computer interface: a proof-of-concept study. *Brain Commun*. 2022;4(1):fcac008. DOI: [10.1093/braincomms/fcac008](https://doi.org/10.1093/braincomms/fcac008).
7. Post-stroke aphasia rehabilitation using an adapted visual P300 brain-computer interface training: improvement over time, but specificity remains undetermined. 2024. DOI: [10.3389/fnhum.2024.1400336](https://doi.org/10.3389/fnhum.2024.1400336).
8. Ezzyat Y et al. Closed-loop stimulation of temporal cortex rescues functional networks and improves memory. *Nat Commun*. 2018;9:365. DOI: [10.1038/s41467-017-02753-0](https://doi.org/10.1038/s41467-017-02753-0).
9. Hampson RE et al. Developing a hippocampal neural prosthetic to facilitate human memory encoding and recall. *J Neural Eng*. 2018;15(3):036014. DOI: [10.1088/1741-2552/aaaed7](https://doi.org/10.1088/1741-2552/aaaed7).
10. Lavy Y et al. Mild Cognitive Impairment and Neurofeedback: A Randomized Controlled Trial. *Front Aging Neurosci*. 2021;13:657646. DOI: [10.3389/fnagi.2021.657646](https://doi.org/10.3389/fnagi.2021.657646).
11. Silva AB et al. The speech neuroprosthesis. *Nat Rev Neurosci*. 2024;25:473–492. [Journal page](https://www.nature.com/articles/s41583-024-00819-9).
12. Patrick-Krueger KM, Burkhart I, Contreras-Vidal JL. The state of clinical trials of implantable brain–computer interfaces. *Nat Rev Bioeng*. 2025;3:50–67. [Journal page](https://www.nature.com/articles/s44222-024-00239-5).

## Không thể kiểm tra / Không được báo cáo

- Chưa audit toàn văn và supplementary materials của toàn bộ 12 bài; page/figure/table locators vì vậy chưa được xác nhận đầy đủ.
- Chưa thực hiện exhaustive database search, duplicate screening, formal risk-of-bias assessment hoặc meta-analysis.
- Adverse events, long-term device reliability, calibration burden và patient-reported outcomes không được báo cáo đồng nhất trong abstract/webpage đã kiểm tra.
- Không đủ dữ liệu để xác định BCI nào tối ưu cho một bệnh nhân cụ thể hoặc để đưa ra khuyến nghị điều trị.
