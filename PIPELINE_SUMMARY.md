# Two-Minute Pipeline Summary

This project models prosodic boundary strength in Japanese and English speech without relying on dense manual boundary labels. It treats prosodic boundary detection as a weak-supervision problem: some boundaries can be identified with high confidence from acoustic evidence, but most word junctures remain unlabeled.

The central idea is to combine interpretable phonetic cues with Positive-Unlabeled learning. The pipeline measures pause duration (`P_ms`), pitch reset (`|Delta F0|`), and intensity change (`Delta RMS`) around word junctures extracted from forced alignments. Broad pause-based candidates form B1 anchors, while stricter multi-cue candidates form B2 anchors. B2 examples are used as reliable positives for PU / nnPU modeling, while the remaining junctures are treated as unlabeled rather than negative.

The workflow is:

1. Prepare Japanese and English speech corpora.
2. Run MFA-style forced alignment to obtain word timings.
3. Extract candidate boundaries at word junctures.
4. Measure acoustic cues around each boundary.
5. Construct B1 and B2 weak anchors.
6. Train PU / nnPU models to score boundary strength.
7. Evaluate scores with punctuation proxy, syntax proxy, top-ranked enrichment, and human-audit workflows.
8. Visualize selected cases with waveform and F0 plots.

The research value of the project is methodological and empirical. Methodologically, it shows how prosodic boundary modeling can be framed without full labels by combining acoustic anchors with PU learning. Empirically, the Japanese-English comparison makes it possible to ask which acoustic boundary cues appear robust across languages and which patterns may be language-specific.

For a quick review, start with `README.md` for the research framing, then `PROJECT_MAP.md` for how the original scripts map onto the research pipeline.

