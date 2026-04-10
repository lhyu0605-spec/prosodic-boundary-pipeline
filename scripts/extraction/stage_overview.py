#!/usr/bin/env python3
"""Print a research-facing overview of the extraction stage.

This placeholder does not extract features. It documents which original scripts
create boundary candidate tables and acoustic cue columns.
"""

STAGE = "Boundary and Acoustic Extraction"

ORIGINAL_SCRIPTS = [
    ("05_make_en_fuzzy.py", "build English boundary candidates from TextGrids"),
    ("06_make_en_acoustics_B1_B2.py", "measure English acoustic cues"),
    ("bsi_extract_pipeline_cleanwords.py", "extract clean word-juncture features"),
    ("prosody_span_pipeline.py", "likely span-based Japanese prosody pipeline"),
    ("英语数据/fast_bsi_extract.py", "fast TextGrid/WAV cue extraction"),
]


def main() -> None:
    print(f"{STAGE} stage")
    print("Purpose: convert aligned speech into boundary rows with acoustic cues.")
    print("\nOriginal scripts:")
    for script, role in ORIGINAL_SCRIPTS:
        print(f"- {script}: {role}")


if __name__ == "__main__":
    main()

