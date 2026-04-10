#!/usr/bin/env python3
"""Print a research-facing overview of the evaluation stage.

This placeholder documents proxy and audit workflows. It does not compute
metrics or create figures.
"""

STAGE = "Evaluation"

ORIGINAL_SCRIPTS = [
    ("08_topk_enrichment_en.py", "top-ranked English enrichment analysis"),
    ("punct_proxy_eval_en.py", "English punctuation-proxy evaluation"),
    ("run_syntax_proxy_from_bsi_en.py", "English syntax-proxy evaluation"),
    ("12_eval_human_audit_en.py", "English human-audit evaluation"),
    ("make_human_audit_clips_en.py", "generate English audit clips"),
]


def main() -> None:
    print(f"{STAGE} stage")
    print("Purpose: compare boundary scores with proxy and perceptual evidence.")
    print("\nOriginal scripts:")
    for script, role in ORIGINAL_SCRIPTS:
        print(f"- {script}: {role}")


if __name__ == "__main__":
    main()

