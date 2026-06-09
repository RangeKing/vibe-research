# Figure storytelling and integrity

Use this reference when **figures, panels, or captions** must support the manuscript’s argument without overclaiming, and when reviewers or collaborators flag **misalignment** between visuals and text.

## Main message

- Each figure should have **one primary message** the reader can state in one sentence.
- Panels (a–d) should be **ordered** to match the argument, not lab notebook order.
- The **title** (if used) and **caption** should state what is shown and what conclusion is **not** implied.

## Figure contract

Before polishing a figure set or caption package, define:

- the one-sentence conclusion the figure must defend
- the evidence chain from each panel to that conclusion
- the unique scientific job of each panel
- source data, `n`, error bars, statistical tests, and image-integrity notes
- export or production needs, including editable text and journal format constraints when known

Panels that repeat the same scientific question should be combined, moved to supplementary material, or dropped.

## Production layout contract

When creating or editing figure files, treat visual legibility as part of the scientific contract. A figure that clips labels, overlaps text, or wastes most of its canvas is not ready even if the data are correct.

Use this workflow before delivery:

1. Sketch the panel grid first: figure size, panel bounds, reserved margins, legend zones, and caption/footnote zones.
2. Give every text element a container. Titles, panel labels, legends, axis labels, annotations, and footnotes should have a known maximum width and line count before coordinates are finalized.
3. Prefer plotting libraries with layout engines (`constrained_layout`, `tight_layout`, `GridSpec`, faceting, or equivalent) for standard charts. If hand-writing SVG, build reusable helpers such as `wrap_text`, `text_box`, `panel_frame`, and `legend_rows` instead of emitting long single-line `<text>` nodes.
4. Treat each panel rectangle as a hard text boundary. Except for the global figure title, every text node should belong to a panel, plot area, legend box, or footnote box. Do not place text by fixed x increments when the label width is unknown; compute the label's container width first, wrap or shorten it, then place it.
5. Keep text-density budgets explicit: figure title <= 70 characters, panel titles <= 45 characters, legend labels <= 32 characters or wrapped, footnotes <= 2 lines per panel, and no single rendered text line wider than its panel.
6. Balance whitespace by resizing panels or simplifying content. Do not solve overflow by shrinking all fonts below legible size; shorten labels, wrap them, move detail to captions, or split the figure.
7. Render the final figure to a raster preview and inspect it at the target aspect ratio. Verify that no right/bottom edge is clipped, panel titles fit, axis tick labels do not collide, legends remain inside their zones, source-data caveats are readable, and the plotted content is not stranded on one side of the canvas.
8. Run smoke checks on the delivered visual format before delivery. For SVGs with direct text nodes, run `scripts/svg_layout_smoke_check.py`. For PNG previews or final raster figures, run `scripts/figure_whitespace_smoke_check.py` to detect large side margins, content bounding-box imbalance, and wasted canvas. Treat the scripts as smoke tests: passing them does not replace visual inspection, but failing them means layout risk remains.

## Captions

- **What**: experimental setup, sample, n, units, scale bars, statistical test names (not just “p < 0.05” without context).
- **How to read**: color keys, abbreviations, and any cropping or normalization.
- **Boundary**: what the figure **cannot** prove (e.g. correlation vs causation, representative vs quantified across all samples).

## Alignment with main-text claims

- Every **strong claim** in the Results that references a figure should have a **matching panel** and **no contradictory** error bars or labels.
- Summary plots (bar charts, heatmaps) should match **supplementary** or **raw** descriptions where applicable; avoid “cherry-picked” exemplars without a defined rule.
- Statistics in the figure (tests, multiple comparisons, exclusion counts) should match **Methods** and **Results** wording.
- When a figure mixes **map, histogram, table, and captioned totals**, verify that every panel uses the **same accounting basis** unless the caption explicitly justifies a different one.
- If marginal plots are meant to correspond to a map or image panel, check that the **bin edges, shared axes, and source-data totals** truly align with the visual panel rather than only sounding aligned in the legend.

## Integrity and common pitfalls

- **Image manipulation**: only adjustments allowed by the target venue (e.g. linear brightness/contrast on full images); no splicing of unrelated lanes without explicit notation.
- **Duplication**: accidental reuse of panels across figures; verify before submission.
- **Selective y-axes**: scales that exaggerate small differences; justify range or show full data.
- **Representative**: if “representative of n experiments” is used, **n** and **independence** (biological vs technical) should be clear in Methods or caption.
- **AI-generated or heavily processed** images: disclose per journal policy; do not pass synthetic data as empirical.

## When to escalate routes

- If the issue is **whether the claim matches the evidence**, use `claim` after a tight `assess` of the figure set.
- If the issue is **rewriting captions or restructuring figures** for clarity, use `draft` with this reference.
- If a **reviewer** raised specific figure issues, use `revise` with a comment-to-action mapping.
