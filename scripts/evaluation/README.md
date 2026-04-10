# Evaluation Stage

This stage checks whether high-scoring boundaries align with plausible external evidence. The evaluations are proxy-based and audit-based, not dense gold-label evaluation.

Run `python stage_overview.py` from this directory for a short terminal summary of the stage.

## Original Scripts

| Original script | Role |
|---|---|
| `08_topk_enrichment_en.py` | Computes enrichment among top-ranked English candidates. |
| `punct_proxy_eval.py` | General or Japanese punctuation-proxy evaluation. |
| `punct_proxy_eval_en.py` | English punctuation-proxy evaluation. |
| `run_syntax_proxy_from_bsi.py` | Likely syntax-proxy evaluation from boundary score tables. |
| `run_syntax_proxy_from_bsi_en.py` | English syntax-proxy analysis and figures. |
| `12_eval_human_audit_en.py` | Evaluates English human perceptual audit labels. |
| `make_human_audit_clips.py` | Generates listening-audit clips, likely for Japanese or general use. |
| `make_human_audit_clips_en.py` | Generates English listening-audit clips. |

## Research Role

Proxy and human-audit analyses help assess whether model scores correspond to linguistically and perceptually meaningful boundaries. They should be interpreted as validation evidence, not as fully supervised benchmark results.
