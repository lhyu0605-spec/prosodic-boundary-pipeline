# Anchor Construction Stage

This stage defines weak positive examples for boundary modeling. The anchor rules are intended to be interpretable rather than fully supervised labels.

Run `python stage_overview.py` from this directory for a short terminal summary of the stage.

## Original Scripts

| Original script | Role |
|---|---|
| `b1_check_and_label.py` | Creates and checks B1 pause-based labels. |
| `06_make_en_B2.py` | Constructs English B2_base and B2_strict anchor labels. |
| `make_b2.py` | Constructs Japanese B2 anchors, likely using voiced-gated pitch-reset criteria. |
| `merge_fuzzy_by_pms.py` | Likely merges fuzzy Japanese boundary information using pause-duration alignment. |
| `viz_b2.py` | Visualizes B2 thresholding and anchor-set sizes. |

## Research Role

B1 provides broad pause-based boundary candidates. B2 provides a smaller, higher-confidence positive set from multiple acoustic cues. B2 anchors are used as positive examples for PU learning.
