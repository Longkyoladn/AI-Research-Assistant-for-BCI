# Comparison matrix: BCI cho ngôn ngữ và nhận thức trong bệnh thần kinh

| Paper | Population | Modality | Mục tiêu/thiết kế | Kết quả chính đã kiểm tra | Giới hạn chính | Trạng thái nguồn |
|---|---|---|---|---|---|---|
| Moses 2021 | 1 người, brainstem stroke, anarthria, quadriparesis | high-density subdural ECoG | Online word/sentence decoding | 15.2 words/min; median WER 25.6%; 50-word vocabulary | n=1; invasive; restricted vocabulary | Full journal webpage/abstract |
| Willett 2023 | 1 người ALS, speech unintelligible | intracortical microelectrode arrays | Attempted speech-to-text | WER 9.1% (50 words), 23.8% (125,000 words) | n=1; invasive; protocol khác các study ECoG | Full journal webpage/abstract |
| Metzger 2023 | 1 người, severe paralysis sau brainstem stroke | 253-channel high-density ECoG | Text + audio + facial avatar | 78 words/min; median WER 25% cho text | n=1; invasive; clinical-feasibility | Full journal webpage/abstract |
| Metzger 2022 | 1 người severe limb/vocal paralysis | ECoG | Silent attempted-speech spelling | Real-time sentence spelling, mở rộng vocabulary qua letters | n=1; chậm hơn whole-word/speech approach | Full journal webpage/abstract |
| Card 2026 | 1 người ALS | intracortical BCI | Longitudinal home use cho speech/cursor | Cho thấy independent long-term deployment khả thi | n=1; durability/generalizability chưa rõ | Journal webpage |
| Musso 2022 | 10 người chronic post-stroke aphasia | scalp EEG + BCI feedback | 30 h language training, proof-of-concept | AAT SMD 0.63; cải thiện nhiều language measures | Không đủ control để cô lập BCI effect | PubMed abstract |
| Visual P300 aphasia 2024 | 12 tuyển, 7 hoàn thành | scalp EEG P300 | ≥14 BCI spelling sessions | Spontaneous speech tăng; 3 người giảm aphasia severity | Dropout/missing data; specificity chưa xác định | PubMed abstract |
| Ezzyat 2018 | Epilepsy patients có intracranial electrodes | intracranial recording + closed-loop stimulation | Detect poor encoding rồi stimulate lateral temporal cortex | Cải thiện later recall trong task | Không phải dementia/MCI cohort; task-specific | Journal webpage/abstract |
| Hampson 2018 | Epilepsy patients có hippocampal electrodes | CA3/CA1 spiking + patterned stimulation | MIMO hippocampal memory prosthesis | Proof-of-concept cải thiện encoding/recall | Invasive; placement theo clinical indication; cohort nhỏ | PubMed/PMC abstract + article webpage |
| Lavy 2021 | Người mild cognitive impairment | scalp EEG neurofeedback | Randomized sham-controlled upper-alpha training | Memory cải thiện so với sham, duy trì ≥1 tháng | Cần full-text risk-of-bias và replication | PubMed abstract |

## Compatibility notes

- Không so sánh trực tiếp WER giữa Moses, Willett và Metzger vì vocabulary, sentence set, language model, participant và neural modality khác nhau.
- Aphasia rehabilitation là mục tiêu **restorative**; speech decoding ở paralysis là **assistive/compensatory**. Hai nhóm không trả lời cùng một clinical question.
- Ezzyat/Hampson dùng intracranial recordings ở epilepsy; kết quả không được chuyển thẳng sang MCI/Alzheimer’s disease.
- Scalp EEG có surgical risk thấp hơn nhưng signal bandwidth/spatial resolution khác rõ ECoG và intracortical arrays.

## Không thể kiểm tra / Không được báo cáo

- Chưa trích đầy đủ participant demographics, adverse events, preprocessing, split unit, calibration time, code/data availability và long-term follow-up cho mọi paper.
- Matrix là snapshot phục vụ discovery, không phải evidence grading hoàn chỉnh hoặc clinical guideline.
