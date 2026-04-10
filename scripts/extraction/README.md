# Extraction Stage

This stage converts aligned TextGrid files into boundary candidate tables and extracts interpretable acoustic cues around each candidate boundary.

Run `python stage_overview.py` from this directory for a short terminal summary of the stage.

## Original Scripts

| Original script | Role |
|---|---|
| `05_make_en_fuzzy.py` | Builds English boundary candidates from MFA TextGrids and maps punctuation from original transcripts. |
| `06_make_en_acoustics_B1_B2.py` | Computes acoustic cues for English candidate boundaries. |
| `bsi_extract_pipeline_cleanwords.py` | Extracts boundary features while filtering empty word intervals. |
| `prosody_span_pipeline.py` | Likely an earlier or broader span-based prosody pipeline for Japanese. |
| `英语数据/fast_bsi_extract.py` | Fast TextGrid/WAV acoustic feature extraction. |
| `英语数据/fix_pause_from_tg.py` | Recomputes pause duration from TextGrid word gaps. |

## Research Role

The extraction stage turns raw aligned speech into a table of word-juncture observations. Each row contains acoustic evidence such as pause duration, pitch reset, voicing coverage, and intensity change.
