# Comparison matrix: Speech/communication BCI

| Study | Participant | Modality | Decoding unit/output | Evaluation | Kết quả chính | Clinical stage |
|---|---|---|---|---|---|---|
| Moses 2021 | 1 nam, chronic pontine stroke, anarthria | 128-channel subdural ECoG | Whole word → text | Online; 50-word vocabulary; prompted sentences | 15.2 WPM; WER 25.6%; 80/150 câu không lỗi | Early feasibility, researcher-assisted |
| Metzger 2022 | Cùng participant Moses 2021 | 128-channel ECoG | NATO code word → letter → spelling | Online 1,152-word vocabulary; larger vocab offline | CER 6.13%; WER 10.53%; 6.86 WPM; 9,170-word simulation WER 13.3% | Early feasibility, researcher-assisted |
| Willett 2023 | 1 participant, bulbar ALS, unintelligible speech | 4 intracortical arrays, area 6v + area 44 | Phoneme → text | Online; 50- and 125,000-word language models; vocal/silent | 62 WPM; WER 23.8% large vocab vocal, 24.7% silent | Early feasibility; substantial daily calibration/training |
| Metzger 2023 | 1 nữ, chronic pontine stroke, anarthria | 253-channel subdural ECoG | Phone/text; speech units/audio; gestures/avatar | Online and offline; 1,024-word general set + AAC sets | Text 78 WPM, WER 25%; intelligible audio and avatar control | Early feasibility, multimodal output |
| Card 2026 | 1 nam, ALS, severe dysarthria | Intracortical, 256 electrodes | Phoneme → text; cursor/gesture | Near-daily independent home use, nearly 2 years | >3,800 h; 183,060 sentences; 56 WPM; 92% self-rated ≥mostly correct | Longitudinal independent home deployment |

## Compatibility checks

| Yếu tố | Vì sao không được so sánh thẳng |
|---|---|
| Vocabulary | 50 words, 1,152 words, 1,024 words và 125,000-word language model là các task khác nhau |
| Unit giải mã | Whole-word, NATO letter, phoneme, discrete acoustic unit và gesture unit có error structure khác nhau |
| Speaking strategy | Vocal attempt, silent attempt, paced letter spelling và paused-between-word speech không tương đương |
| Ground truth | Prompted sentence có target rõ; open-ended home use phần lớn dựa vào user self-rating |
| Participant | ALS và pontine stroke khác bệnh sinh; residual movement/speech cũng khác nhau |
| Modality | ECoG surface field potentials khác intracortical spiking/threshold-crossing features |

## Không thể kiểm tra / Không được báo cáo

- Chưa có multi-participant head-to-head benchmark thống nhất.
- Chi phí, surgical complication rate, fully implanted operation và long-term hardware failure chưa thể suy ra từ matrix này.
