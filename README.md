# Cross-Linguistic Prosodic Boundary Modeling with Acoustic Cues and PU Learning

## At a Glance

- **Problem:** modeling prosodic boundary strength without dense manual labels  
- **Data:** Japanese (JVS) and English (LibriTTS)  
- **Method:** acoustic cues + B1/B2 anchors + PU/nnPU learning  
- **Output:** continuous boundary-strength scoring over word junctures  

---

## Overview

This project studies how prosodic boundary strength can be modeled from speech acoustics when dense manual boundary labels are unavailable. It focuses on Japanese speech from JVS and English speech from LibriTTS, using forced alignment, acoustic feature extraction, weak anchor construction, and Positive-Unlabeled (PU / nnPU) learning.

The repository is organized as a research pipeline rather than a production software package. It is designed to present the structure and logic of the study clearly, allowing readers to understand the methodology before inspecting individual scripts.

---

## Research Question

Can prosodic boundary strength be modeled from acoustic evidence across languages when reliable manual labels are sparse or unavailable?

More specifically, this project investigates whether pause duration, pitch reset, and intensity change can be used to construct high-confidence positive anchors, and support a broader boundary-scoring model over unlabeled word junctures in Japanese and English speech.

---

## Motivation

Prosodic boundaries are central to speech perception, phrasing, intelligibility, and the relationship between syntax and spoken language. However, boundary annotation is expensive, language-specific, and difficult to scale. Many speech corpora provide audio and transcripts, but not dense labels for prosodic phrasing.

This makes prosodic boundary modeling a natural weak-supervision problem. Instead of requiring full manual labels, the pipeline uses interpretable acoustic cues to identify reliable boundary examples, then learns from the larger set of unlabeled candidate junctures.

The cross-linguistic setting is important because Japanese and English differ in rhythm, phrasing, lexical/prosodic structure, and punctuation conventions. Applying the same conceptual workflow to both languages helps distinguish language-specific patterns from more general acoustic evidence for boundary strength.

---

## Key Ideas

### Acoustic Evidence for Boundary Strength

The pipeline focuses on three acoustic cues commonly associated with prosodic boundaries:

- `P_ms`: pause duration between adjacent word intervals  
- `|ΔF0|`: pitch reset or discontinuity around a candidate boundary  
- `ΔRMS`: change in acoustic intensity around the boundary  

These cues are intentionally interpretable. The goal is not only to produce a score, but also to preserve a link between model behavior and phonetic evidence.

---

### B1 and B2 Anchors

The project defines weak anchor sets to identify likely positive examples.

- **B1:** pause-based anchors capturing broad boundary candidates  
- **B2:** stricter multi-cue anchors incorporating voicing, pitch reset, and optionally intensity  

B2 is designed to provide higher-confidence positive examples for weakly supervised learning.

---

### PU / nnPU Learning

Positive-Unlabeled learning is suitable because reliable negatives are unavailable. High-confidence anchors (e.g., B2) are treated as positive, while remaining word junctures are treated as unlabeled.

The model learns a boundary-scoring function from this partially labeled data, producing a **continuous estimate of boundary strength** rather than a binary classification.

---

## Core Contribution

This project proposes a transparent weak-supervision framework for prosodic boundary modeling. It combines interpretable acoustic anchoring with Positive–Unlabeled learning to estimate boundary strength without requiring dense manual annotations.

The key contribution lies in integrating:

- interpretable acoustic cues  
- multi-level anchor construction (B1/B2)  
- PU-based boundary scoring  

within a unified cross-linguistic pipeline.

---

## Pipeline Overview

The pipeline is designed as a sequence of interpretable stages, each corresponding to a clear phonetic or modeling assumption:

1. **Alignment**  
   Speech data is aligned using Montreal Forced Aligner (MFA), producing word-level TextGrid files.

2. **Boundary Candidate Extraction**  
   Candidate boundaries are defined at word junctures based on aligned intervals.

3. **Acoustic Cue Extraction**  
   Pause duration, pitch behavior, voicing, and intensity are computed for each candidate.

4. **Anchor Construction**  
   B1 and B2 anchors are constructed using acoustic rules.

5. **PU / nnPU Modeling**  
   A boundary-scoring model is trained using positive anchors and unlabeled data.

6. **Evaluation**  
   Evaluation is conducted via punctuation proxies, syntax proxies, enrichment analysis, and human audit.

7. **Visualization**  
   Waveform and F0 plots are used for qualitative inspection.

---

## Repository Structure

```text
.
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
