# Supplementary Information Adequacy Audit

Use this reference when a task creates, edits, checks, or cites Supplementary Information, especially during revision or near-submission work.

## Failure Pattern

A short narrative supplement can look polished while failing the reviewer-facing job. If the main text promises dataset provenance, thresholds, formulas, sensitivity tests, validation tables, or variable definitions, the SI must contain those materials in a concrete, inspectable form. Do not solve an SI gap by making the prose smoother while leaving the promised evidence absent.

## Minimum Contract

For technical manuscripts, the SI should usually include:

- Source/provenance table: dataset, source or DOI/URL label, version or download date, native resolution, preprocessing, and role in the analysis.
- Variable dictionary: every symbol used in main-text or SI formulas, its unit or spatial unit, source variable, transformation, normalization, and interpretation.
- Formal equations: displayed equations for screening scores, benefit or penalty terms, pathway-entry scores, uncertainty or adequacy classes, project-level scores, and sensitivity variants. In `.docx`, formulas should be Word equation objects; in Markdown/LaTeX, they should render as equations rather than plain-text arithmetic.
- Coefficient and threshold tables: all pathway/stage thresholds, weights, exclusion criteria, ranking/zoning labels, and any mode-specific overrides.
- Sensitivity and validation tables: weight perturbations, threshold sweeps, bootstrap summaries, project-cell validation, source-data checks, and residual caveats when relevant.
- Crosswalk to the main manuscript: every "Supplementary Note", "Supplementary Table", "Supplementary Figure", formula, threshold, and validation pointer in the main text resolves to an actual SI item with the same number and terminology.
- Figure/table consistency: figure order, captions, panel labels, source-data table references, and numerical labels match the main text.
- Reproducibility boundary: distinguish comparative screening, robustness checks, and policy-ready site design limits.

## Reviewer-Reproducible Methods Gate

For journal-targeted packages, especially Analysis or framework papers that use scoring, screening, classes, rankings, adequacy matrices, sensitivity readouts, or source-data audits, do not treat a short narrative Methods/SI as sufficient. The package should let a critical reader reconstruct the workflow without access to the author chat history.

Minimum reviewer-reproducible structure:

1. `Data inputs`: each dataset, table, version/date, access route, selection rule, and exclusion rule.
2. `Preprocessing`: transformations, joins, filters, category harmonization, unit conversions, spatial/temporal aggregation, and missing-data handling.
3. `Notation`: a symbol table covering every variable in equations and every class label used in figures or tables.
4. `Equations`: formal displayed equations for each score, class assignment, ranking rule, adequacy metric, uncertainty penalty, and sensitivity variant. If the manuscript deliberately avoids a composite index, include the equations or logical predicates used for inclusion/exclusion and ordinal class assignment.
5. `Thresholds and coefficients`: every threshold, weight, ordinal class boundary, penalty, override, or "screening-only" rule with provenance and sensitivity status.
6. `Validation and sensitivity`: what was varied, what stayed fixed, how robustness was judged, and what would invalidate the claim.
7. `Output crosswalk`: map each figure panel, source-data file, supplementary table, and headline claim to the exact method step that produced or justified it.

High readiness scores require this gate to pass. If Methods are only a few narrative paragraphs, SI only points to source files, or formulas are absent despite value-bearing scoring/ranking claims, cap the score until the missing structure is built.

## Workflow

1. Extract every SI-facing promise from the main text, Methods, figure captions, and reviewer comments.
2. Inventory the current SI by note/table/figure/formula and mark missing, vague, or renamed items.
3. Compare against prior detailed supplements, checkpoints, response packages, or source-data tables when available. Restore lost detail instead of replacing it with generic prose.
4. Build the missing material as formal tables and equations before sentence-level polish.
5. Cross-check numbering, variables, thresholds, figure names, citation numbering, and dataset labels after any reference or figure-order change.
6. Render or validate the final delivery format. For `.docx`, confirm equations are real Office Math objects and tables are Word tables, not pasted plain text. Use `scripts/docx_equation_smoke_check.py` for a quick Office Math/table count when `.docx` files are present.

## Do Not

- Do not cite absent SI content in the main manuscript.
- Do not replace required tables with prose summaries unless the main text is also revised to avoid promising tables.
- Do not expose local file paths, script names, or workspace logistics in reviewer-facing SI.
- Do not leave older detailed SI material behind if it is still substantively correct and needed for the manuscript story.
