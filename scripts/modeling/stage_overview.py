#!/usr/bin/env python3
"""Print a research-facing overview of the PU modeling stage.

This placeholder does not train a model. It explains which original scripts
perform nnPU scoring and sensitivity checks.
"""

STAGE = "PU / nnPU Modeling"

ORIGINAL_SCRIPTS = [
    ("07_run_nnpu_en.py", "train and score English nnPU models"),
    ("run_nnpu.py", "general or Japanese nnPU training/scoring"),
    ("pi_sensitivity.py", "evaluate sensitivity to the class prior"),
    ("postprocess_pu.py", "postprocess scores and cue-space plots"),
    ("11_en_pu_sanity.py", "produce English PU diagnostics"),
]


def main() -> None:
    print(f"{STAGE} stage")
    print("Purpose: learn boundary-strength scores from positives and unlabeled data.")
    print("\nOriginal scripts:")
    for script, role in ORIGINAL_SCRIPTS:
        print(f"- {script}: {role}")


if __name__ == "__main__":
    main()

