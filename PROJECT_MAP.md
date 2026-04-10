# Project Map

This file maps the original workspace into a research pipeline. It does not move or rename any original files. Roles are inferred from filenames, script comments, and partial inspection. Items marked as likely should be verified before formal release.

## Stage 1: Corpus Preparation and Forced Alignment

This stage prepares speech and transcripts for forced alignment, runs Montreal Forced Aligner, and indexes the resulting TextGrid files. It establishes the time-aligned word structure needed for all downstream boundary analysis.

| Original file or directory | Role |
|---|---|
| `prepare_libritts_subset.py` | Selects a LibriTTS subset by speaker count and target hours; exports manifests for later alignment and extraction. |
| `01_stage_for_alignment.py` | Stages English LibriTTS audio and cleaned transcripts into an MFA-compatible corpus layout. |
| `02_run_mfa_align.py` | Runs MFA alignment using a specified pronunciation dictionary and acoustic model. |
| `03_index_textgrids.py` | Builds an index of MFA TextGrid outputs and merges alignment status back into the manifest. |
| `04_list_failed.py` | Lists utterances whose TextGrid alignment is missing. |
| `日语jvs/jvs_flatten_v2.py` | Likely prepares or flattens JVS speaker directories for downstream processing. |
| `日语jvs_mfa_corpus/` | Likely staged Japanese MFA corpus directory. |
| `日语jvs_mfa_out/` | Likely Japanese MFA TextGrid output directory. |
| `英语语料库/LibriTTS_tc100_100spk_22h/mfa_corpus/` | English MFA input corpus. |
| `英语语料库/LibriTTS_tc100_100spk_22h/alignments/` | English MFA alignment outputs. |

## Stage 2: Boundary Candidate Extraction

This stage converts aligned words into candidate boundary rows. A boundary candidate is generally a junction between two consecutive labeled word intervals.

| Original file | Role |
|---|---|
| `05_make_en_fuzzy.py` | Builds an English boundary table from MFA TextGrids and maps original transcript punctuation onto aligned word intervals. |
| `build_boundary_times_and_merge.py` | Extracts Japanese boundary times from TextGrids and merges them with existing boundary information. |
| `build_boundary_spans_and_merge.py` | Similar to boundary-time merging, likely using span-based representations. |
| `prosody_span_pipeline.py` | Likely an earlier or broader Japanese span-based boundary pipeline using TextGrid and WAV inputs. |
| `bsi_extract_pipeline_cleanwords.py` | Extracts boundary rows from labeled word intervals while filtering empty TextGrid intervals. |
| `英语数据/bsi_extract_pipeline.py` | English boundary-strength-index extraction pipeline. |
| `中文/zh_bsi_extract.py` | Chinese boundary extraction script, likely for an auxiliary multilingual extension. |

## Stage 3: Acoustic Cue Extraction

This stage measures acoustic evidence around each boundary candidate. The main cues are pause duration, pitch reset, voicing coverage, and intensity change.

| Original file | Role |
|---|---|
| `06_make_en_acoustics_B1_B2.py` | Computes English acoustic features around boundary candidates and derives B1/B2-related columns. |
| `bsi_extract_pipeline_cleanwords.py` | Computes pause, pitch, intensity, and voicing features from TextGrid and WAV files. |
| `英语数据/fast_bsi_extract.py` | Faster acoustic boundary feature extraction from TextGrid and WAV files. |
| `英语数据/fix_pause_from_tg.py` | Recomputes or repairs pause duration values from TextGrid word gaps. |
| `中文数据/fix_pms_by_wordgap.py` | Likely repairs Chinese pause duration values using word-gap timing. |
| `ja_final_bsi_with_feats*.csv` | Generated Japanese acoustic feature tables. |

## Stage 4: Anchor Construction

This stage defines weak positive examples from interpretable acoustic rules. B1 is broad and pause-based; B2 is stricter and multi-cue.

| Original file | Role |
|---|---|
| `b1_check_and_label.py` | Language-agnostic B1 labeling and sanity checking based on pause threshold. |
| `06_make_en_B2.py` | Creates English B2_base and B2_strict anchors from acoustic columns. |
| `make_b2.py` | Creates Japanese B2_base anchors, likely using voiced-gated pitch-reset criteria. |
| `merge_fuzzy_by_pms.py` | Merges Japanese fuzzy boundary information, likely using pause-duration matching. |
| `viz_b2.py` | Visualizes B2 thresholding and anchor distributions. |
| `ja_final_bsi_with_time_SPAN_FUZZY_with_B1*.csv` | Generated Japanese B1/B2-enriched boundary tables. |

## Stage 5: PU / nnPU Modeling

This stage trains a boundary scoring model using positive anchors and unlabeled examples. The output is a continuous score intended to reflect boundary strength.

| Original file or directory | Role |
|---|---|
| `07_run_nnpu_en.py` | English nnPU training and scoring script. |
| `run_nnpu.py` | General or Japanese nnPU training and scoring script. |
| `postprocess_pu.py` | Postprocesses PU scores and creates joint cue-space plots. |
| `pi_sensitivity.py` | Tests sensitivity to the assumed positive class prior. |
| `11_en_pu_sanity.py` | Produces English PU score sanity checks, summary tables, and score-cue diagnostic plots. |
| `results_nnpu/` | Generated nnPU scores and diagnostic figures. |
| `scored_pi*.csv` | Generated score files under different class-prior assumptions. |

## Stage 6: Evaluation and Validation

This stage evaluates model behavior using indirect textual proxies, syntactic proxies, top-ranked enrichment, and human perceptual audit workflows. These evaluations do not replace gold labels, but they help assess whether high-scoring candidates align with plausible boundary evidence.

| Original file or directory | Role |
|---|---|
| `08_topk_enrichment_en.py` | Computes top-ranked English enrichment for punctuation and B1 rates. |
| `punct_proxy_eval.py` | General or Japanese punctuation-proxy evaluation. |
| `punct_proxy_eval_en.py` | English punctuation-proxy evaluation using `is_punct`. |
| `plot_punct_proxy_en.py` | Likely visualizes English punctuation-proxy results. |
| `run_syntax_proxy_from_bsi.py` | Likely syntax-proxy evaluation from boundary score tables. |
| `run_syntax_proxy_from_bsi_en.py` | English syntax-proxy analysis and figures. |
| `12_eval_human_audit_en.py` | Evaluates English human perceptual audit labels from three raters. |
| `make_human_audit_clips.py` | Generates listening-audit clips, likely for Japanese or general cases. |
| `make_human_audit_clips_en.py` | Generates English listening-audit clips. |
| `audit_*.csv`, `audit_summary_stats.txt` | Generated human-audit tables and summaries. |
| `punct_proxy_*.csv` | Generated punctuation-proxy outputs. |
| `syntax-chapters/`, `chapters/` | Generated proxy-analysis figures and tables, likely prepared for manuscript chapters. |

## Stage 7: Visualization and Qualitative Analysis

This stage supports interpretation by selecting representative cases and plotting acoustic evidence around candidate boundaries.

| Original file or directory | Role |
|---|---|
| `09_select_case_study_en.py` | Selects English case-study examples by PU score, punctuation, pause, and acoustic gates. |
| `10_plot_case_wave_f0_en.py` | Plots English waveform and F0 around selected boundary cases. |
| `select_case_study.py` | General or Japanese case-study selection. |
| `plot_case_wave_f0.py` | General or Japanese waveform and F0 case visualization. |
| `plot_pu_diagnostics_en.py` | Likely English PU diagnostic plotting. |
| `plot_b1_diagnostics.py` | Plots B1 pause and acoustic diagnostics. |
| `make_joint_anchor_plot.py` | Plots joint acoustic cue space with anchor labels. |
| `make_interspeech_figs.py` | Likely creates manuscript or conference figures. |
| `figures/`, `figures_b1/`, `figs_b2/`, `fig/`, `fig_step1/` | Generated figure directories. |
| `select case/`, `plot select case/` | Generated case-study tables or plots. |

## Stage 8: Multilingual and Statistical Extensions

These files appear to extend the English-Japanese core toward broader multilingual comparison or statistical modeling.

| Original file or directory | Role |
|---|---|
| `三语总数据/merge_normalize_bsi.py` | Likely merges and normalizes boundary-strength features across three languages. |
| `三语总数据/tri_lme_raw_and_figs.py` | Likely runs linear mixed-effects-style summaries and creates cross-language figures. |
| `三语总数据/tri_all_bsi_ready.csv` | Generated cross-language analysis table. |
| `中文数据/`, `中文/` | Chinese data and processing scripts, likely exploratory extension beyond the core Japanese-English setup. |

## Stage 9: Manuscript, Reference, and Workspace Artifacts

These files are useful for research development but are not part of the executable pipeline.

| Original file or directory | Role |
|---|---|
| `*.doc`, `*.docx`, `*.pdf` | Manuscript drafts, application materials, or reference papers. |
| `interspeech.bib`, `MFA.bib` | Bibliography files. |
| `ISCA Archive.html`, `ISCA Archive_files/` | Saved reference webpage artifacts. |
| `~$*` files | Temporary office-document lock files; should not be part of a public repository. |
| `snake.html`, `snake-app.js`, `snake-logic.js` | Likely unrelated web/game files. |

