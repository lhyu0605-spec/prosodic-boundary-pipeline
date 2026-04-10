#!/usr/bin/env python3
"""Print a research-facing overview of the alignment stage.

This placeholder does not run the original alignment scripts. It documents the
intended order and points readers to the original workspace files.
"""

STAGE = "Alignment"

ORIGINAL_SCRIPTS = [
    ("prepare_libritts_subset.py", "select a LibriTTS subset and write manifests"),
    ("01_stage_for_alignment.py", "stage English audio/transcripts for MFA"),
    ("02_run_mfa_align.py", "run MFA alignment"),
    ("03_index_textgrids.py", "index aligned TextGrid files"),
    ("04_list_failed.py", "list utterances without successful alignment"),
]


def main() -> None:
    print(f"{STAGE} stage")
    print("Purpose: create word-level timing from speech and transcripts.")
    print("\nOriginal scripts:")
    for script, role in ORIGINAL_SCRIPTS:
        print(f"- {script}: {role}")


if __name__ == "__main__":
    main()

