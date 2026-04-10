# Cross-Linguistic Prosodic Boundary Modeling with Acoustic Cues and PU Learning

## Overview

This project studies how prosodic boundary strength can be modeled from speech acoustics when dense manual boundary labels are unavailable. It focuses on Japanese speech from JVS and English speech from LibriTTS, using forced alignment, acoustic feature extraction, weak anchor construction, and Positive-Unlabeled (PU / nnPU) learning.

The repository is organized as a research pipeline rather than a production software package. The original workspace contains scripts, data products, figures, and manuscript material. This `clean_pipeline/` directory provides a research-facing map of the project for readers who want to understand the design of the study before inspecting individual scripts.

## Research Question

Can prosodic boundary strength be modeled from acoustic evidence across languages when reliable manual labels are sparse or unavailable?

More specifically, this project asks whether pause duration, pitch reset, and intensity change can be used to construct high-confidence positive anchors, then support a broader boundary-scoring model over unlabeled word junctures in Japanese and English speech.

## Motivation

Prosodic boundaries are central to speech perception, phrasing, intelligibility, and the relationship between syntax and spoken language. However, boundary annotation is expensive, language-specific, and difficult to scale. Many speech corpora provide audio and transcripts, but not dense labels for prosodic phrasing.

This makes prosodic boundary modeling a natural weak-supervision problem. Instead of requiring full manual labels, the pipeline uses interpretable acoustic cues to identify reliable boundary examples, then learns from the larger set of unlabeled candidate junctures.

The cross-linguistic setting matters because Japanese and English differ in rhythm, phrasing, lexical/prosodic structure, and punctuation conventions. Applying the same conceptual workflow to both languages helps separate language-specific surface patterns from more general acoustic evidence for boundary strength.

## Key Ideas

### Acoustic Evidence for Boundary Strength

The pipeline focuses on three acoustic cues that are commonly associated with prosodic boundaries:

- `P_ms`: pause duration between adjacent word intervals, measured in milliseconds.
- `|Delta F0|`: pitch reset or pitch discontinuity around a candidate boundary.
- `Delta RMS`: change in acoustic intensity around the boundary.

These cues are intentionally interpretable. The goal is not only to produce a score, but also to preserve a link between model behavior and phonetic evidence.

### B1 and B2 Anchors

The project uses weak anchor sets to define likely positive examples.

`B1` represents broad pause-based anchors. These are candidate boundaries selected primarily from pause duration, for example word junctures whose pause exceeds a fixed threshold. B1 is useful because pauses are relatively easy to detect, but pause alone may over-select boundaries or miss non-pausal phrasing.

`B2` represents a stricter multi-cue anchor set. Conceptually, B2 starts from plausible boundary candidates and adds stronger acoustic evidence, such as sufficient voicing around the boundary and a large pitch reset, with stricter variants also considering intensity change. B2 is designed to provide higher-confidence positive examples for weakly supervised learning.

### PU / nnPU Learning

Positive-Unlabeled learning is appropriate because the data naturally contains reliable positives but not reliable negatives. A high-confidence anchor such as B2 can be treated as positive, but the remaining unlabeled junctures are mixed: some are true boundaries, some are weak boundaries, and some are non-boundaries.

PU / nnPU learning addresses this setting by estimating a boundary-scoring function from positive and unlabeled data without assuming that all unlabeled examples are negative. In this project, the learned score is interpreted as a continuous estimate of boundary strength rather than a simple binary label.

## Core Contribution

The contribution of this repository is a transparent weak-supervision pipeline for prosodic boundary modeling. The pipeline connects:

- corpus preparation and forced alignment,
- word-juncture extraction,
- acoustic cue measurement,
- interpretable B1/B2 anchor construction,
- PU / nnPU boundary scoring,
- proxy evaluation and human-audit support,
- qualitative waveform and F0 visualization.

The methodological contribution is the combination of interpretable acoustic anchoring with PU learning in a cross-linguistic setting. The project does not assume dense manual boundary labels; instead, it treats boundary modeling as a problem of learning from reliable positive evidence and unlabeled speech structure.

## Pipeline Overview

1. Alignment

   Speech files and transcripts are prepared for Montreal Forced Aligner (MFA). The output is a set of TextGrid files that align words, and sometimes phones, to the audio timeline.

2. Boundary Candidate Extraction

   Candidate boundaries are defined at word junctures. The pipeline reads TextGrid word intervals, filters empty intervals, and records the timing relationship between adjacent words.

3. Acoustic Cue Extraction

   For each candidate boundary, the pipeline estimates pause duration, local pitch behavior, voicing coverage, and intensity change. These measurements form the interpretable feature space for boundary modeling.

4. Anchor Construction

   B1 and B2 anchors are constructed from acoustic rules. B1 captures broad pause-based evidence, while B2 captures stricter multi-cue evidence intended to serve as reliable positives.

5. PU / nnPU Modeling

   A PU model is trained using B2 as positive examples and the remaining candidate boundaries as unlabeled data. The model outputs a continuous score for boundary strength.

6. Evaluation

   The project evaluates the score through indirect and direct evidence, including punctuation proxy analysis, syntax proxy analysis, enrichment among top-ranked candidates, and human perceptual audit workflows.

7. Visualization

   Selected cases are visualized with waveform and F0 plots. These figures help inspect whether high-scoring and low-scoring boundaries differ in acoustically interpretable ways.

## Repository Structure

```text
clean_pipeline/
├── README.md
├── PROJECT_MAP.md
├── PIPELINE_SUMMARY.md
├── scripts/
│   ├── alignment/
│   ├── extraction/
│   ├── anchors/
│   ├── modeling/
│   ├── evaluation/
│   └── visualization/
├── examples/
└── docs/
```

The original scripts and generated data remain in the parent repository. This directory is a clean academic guide to the project structure and research logic.

## Main Features

- Cross-linguistic design using Japanese (JVS) and English (LibriTTS).
- MFA-compatible forced-alignment workflow.
- Acoustic cue extraction for pause, pitch reset, voicing, and intensity change.
- Interpretable B1/B2 anchor construction.
- PU / nnPU scoring for unlabeled candidate boundaries.
- Proxy evaluation using punctuation and syntax-related signals.
- Human-audit support for perceptual validation.
- Case-study visualization with waveform and F0.

## Example Case Study

A strong boundary is expected to show converging acoustic evidence. For example, a word juncture may include a noticeable pause, a clear pitch reset when voicing is available on both sides, and an intensity pattern consistent with phrase-final weakening or renewed phrase onset. Such cases are likely to receive high boundary scores, especially when they resemble B2-style anchors.

A weak boundary may show little or no pause, limited pitch discontinuity, and no clear intensity change. These cases may still be grammatically adjacent or separated by punctuation in text, but the acoustic evidence for a prosodic boundary is weaker.

The case-study scripts are intended to support qualitative inspection of these contrasts. They should be used to illustrate model behavior, not to claim results without regenerated figures and documented selection criteria.

## Current Status

This is an active research repository. The parent workspace contains original scripts, intermediate CSVs, generated figures, human-audit materials, and manuscript drafts. Some scripts include hard-coded local paths and were written during exploratory research.

The `clean_pipeline/` directory provides a stable academic-facing description of the project and a guide for future cleanup. It does not replace the original scripts and does not copy large corpora or generated outputs.

## Limitations and Notes

- Some original scripts use local absolute paths and should be parameterized before public release.
- Large datasets and MFA outputs should not be committed unless licensing and storage constraints are addressed.
- Existing figures and CSV outputs should be treated as generated artifacts; formal results should be regenerated from a documented run.
- File-role mappings in `PROJECT_MAP.md` are based on script names, comments, and partial inspection. Uncertain mappings are marked as likely.

