# Modeling Stage

This stage trains and applies Positive-Unlabeled models to score boundary strength across candidate word junctures.

Run `python stage_overview.py` from this directory for a short terminal summary of the stage.

## Original Scripts

| Original script | Role |
|---|---|
| `07_run_nnpu_en.py` | English nnPU training and scoring. |
| `run_nnpu.py` | General or Japanese nnPU training and scoring. |
| `pi_sensitivity.py` | Evaluates sensitivity to the assumed positive prior. |
| `postprocess_pu.py` | Postprocesses PU scores and creates cue-space diagnostics. |
| `11_en_pu_sanity.py` | Produces English score diagnostics and summary tables. |

## Research Role

PU learning is used because only positive anchors are reliable. The remaining candidate boundaries are unlabeled, not true negatives. The resulting model score is interpreted as a continuous boundary-strength estimate.
