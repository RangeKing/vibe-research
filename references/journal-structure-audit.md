# Journal Structure Audit

Use this audit for near-submission, journal-targeted, package-readiness, editor/reviewer-style, Word/PDF package, heading/subheading, equation, table and figure-format work.

## Purpose

Journal-facing manuscripts must satisfy both scientific argument and format expectations. A draft can have the right evidence but still read as mis-targeted if headings are too long, sections violate journal policy, equations look like raw text, or display items are not presented in the expected format.

## Target-Journal Check

When a target journal is named:

1. Prefer the journal's current official author or content-type pages.
2. Record the relevant content type, such as Article, Analysis or Resource.
3. Check section order, abstract length, main-text length, display-item limits, reference guidance and heading policy.
4. Treat official guidance as stronger than generic style heuristics.

## Heading And Subheading Audit

For every manuscript-facing heading:

- Check whether the section is allowed to have subheadings.
- For Nature-family Article/Analysis formats, Results and Methods commonly allow topical subheadings; Discussion commonly should not contain subheadings unless the target journal explicitly permits them.
- Prefer short topical labels over full-sentence mini-conclusions when the heading feels long, procedural or report-like.
- Flag subheadings that are sentence-like, overloaded with multiple clauses, or longer than about 6-8 content words unless there is a strong journal-style reason.
- Scan all sibling headings together; if one heading is too long, similar drift often appears elsewhere.

## Equation And Display-Format Audit

For Word/PDF submission packages:

- Equations should be inserted as formal equation objects where feasible, such as Word Office Math in `.docx`, not only plain-text arithmetic lines.
- Equation numbering should be consistent across main text and Supplementary Information.
- Variables in explanatory prose should match the displayed equations.
- If the manuscript or SI contains value-bearing methods, scoring rules, screening classes, thresholds, sensitivity tests, or validation formulas, a `.docx` package with zero Office Math objects is a display-format warning and can be a readiness blocker.
- Tables and figure legends should not be regenerated from stale strings that bypass the cleaned manuscript text.
- After building the final file, inspect the delivered package, not only the source Markdown, because build scripts can reintroduce formatting drift.

Quick check for `.docx` packages:

```bash
python3 scripts/docx_equation_smoke_check.py path/to/main.docx path/to/supplementary_information.docx
```

This smoke check reports Office Math object counts and Word table counts. It does not prove the equations are scientifically correct, but it prevents accidentally shipping formula-bearing Methods/SI as plain paragraphs.

## Output Contract

When reporting this audit, include:

- `Journal structure status`: clear / blockers found / not checked
- `Heading fixes`: headings shortened, removed or retained with rationale
- `Equation/display fixes`: whether equations are formal objects in the delivered file
- `Official guidance checked`: source used or reason not checked
- `Follow-up package scan`: whether the final Word/PDF was inspected after rebuild
