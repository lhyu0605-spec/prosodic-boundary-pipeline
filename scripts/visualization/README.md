# Visualization Stage

This stage supports qualitative interpretation of the model by plotting selected boundaries with waveform, F0, and boundary markers.

Run `python stage_overview.py` from this directory for a short terminal summary of the stage.

## Original Scripts

| Original script | Role |
|---|---|
| `09_select_case_study_en.py` | Selects English case-study examples by score and acoustic/textual criteria. |
| `10_plot_case_wave_f0_en.py` | Plots English waveform and F0 around selected boundaries. |
| `select_case_study.py` | General or Japanese case-study selection. |
| `plot_case_wave_f0.py` | General or Japanese waveform and F0 visualization. |
| `plot_pu_diagnostics_en.py` | Likely plots English PU diagnostics. |
| `plot_b1_diagnostics.py` | Plots B1-related pause and cue diagnostics. |
| `make_joint_anchor_plot.py` | Visualizes joint acoustic cue space with anchors. |
| `make_interspeech_figs.py` | Likely creates publication-oriented figures. |

## Research Role

Visualization makes the boundary score inspectable. A reviewer can compare high-scoring and low-scoring cases by looking at the actual acoustic context rather than only aggregate metrics.
