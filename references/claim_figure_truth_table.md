# Claim-Figure-Source-Data Truth Table

Use this audit before any high-impact journal score, figure polish, abstract rewrite, title rewrite, cover-letter claim, or submission-package readiness claim.

For every title, abstract, Results subheading, figure title, figure caption conclusion, and cover-letter claim, create one row:

| claim_id | exact claim | location | required figure panel | observed visual evidence | source-data file/column | effect size | n/denominator | uncertainty | allowed wording | forbidden wording | verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|

Verdict values:

- `proven_visibly`
- `supported_but_not_visible`
- `source_data_only`
- `ambiguous`
- `contradicted_by_figure`
- `unsupported`

## Hard Caps

- Any abstract-level claim marked `contradicted_by_figure`: Article cap 55.
- Any abstract-level claim marked `source_data_only` without a matching main figure: Article cap 70.
- Any central conclusion that depends on a distinction not visible in the main figure: Article cap 75.
- Any claim using "shift", "reversal", "dominates", "ranks higher", "probability", or "loss" must report the metric, denominator, uncertainty, and source-data basis.

## Operating Rules

- Treat the rendered figure as the first source of editorial truth. If prose says one thing and the visual implies another, the claim must be softened or the figure redesigned before score increases.
- Do not use extensive source-data tables to rescue a title or abstract claim that no main figure visibly supports.
- Do not mark a claim `proven_visibly` unless a skeptical editor can identify the supporting panel and read the qualitative direction without reconstructing Methods logic.
- If multiple panels are required to support one abstract claim, list each panel and state which link is the weakest.
- If the truth table is absent, incomplete, or stale, no high-impact journal score may reach 90/100.
