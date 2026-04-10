# Alignment Stage

This stage prepares speech data and transcripts for forced alignment, then indexes the TextGrid outputs needed for boundary extraction.

Run `python stage_overview.py` from this directory for a short terminal summary of the stage.

## Original Scripts

| Original script | Role |
|---|---|
| `prepare_libritts_subset.py` | Selects a LibriTTS subset and writes manifest files. |
| `01_stage_for_alignment.py` | Creates an MFA-compatible English corpus with cleaned transcripts. |
| `02_run_mfa_align.py` | Runs Montreal Forced Aligner using a specified dictionary and acoustic model. |
| `03_index_textgrids.py` | Indexes aligned TextGrid files and updates the manifest with alignment status. |
| `04_list_failed.py` | Writes a list of utterances without successful alignment. |

## Research Role

Forced alignment supplies word-level timing. These timings define candidate word junctures, which are the basic units for downstream acoustic feature extraction and boundary scoring.
