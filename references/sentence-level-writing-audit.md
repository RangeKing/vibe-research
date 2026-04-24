# Sentence-Level Writing Audit

Use this reference when the user asks for writing-quality review, sentence-level cleanup, passive-voice cleanup, clutter reduction, terminology consistency, or a structured prose audit.

This reference is for delivery quality, not scientific truth claims. Use it after route selection has already decided that the task is primarily editorial rather than conceptual.

Load `references/high-journal-expression.md` alongside this file when the user wants the prose to sound more like a mature journal manuscript and less like AI output, translation residue, or explanatory over-scaffolding.

## Navigation

- Review modes
- The five editorial passes
- Severity guidance
- Output pattern
- Boundary

## Review modes

Choose the lightest mode that matches the request:

- `full-review`: full manuscript or long section; run all five passes and report the highest-impact issues.
- `section-review`: one named section such as Abstract, Introduction, Results, or Discussion; run all five passes on that slice only.
- `targeted-pass`: the user asks for one writing dimension such as passive voice, clutter, or terminology consistency; run only the relevant pass or pair of passes.
- `interactive-pass`: the user wants a paragraph-by-paragraph walkthrough with before/after examples and brief rationale.

Default to `section-review` when the user provides only one section. Default to `targeted-pass` when the user names a specific writing problem.

## The five editorial passes

### 1. Clutter extraction

Strip sentences to their load-bearing meaning.

Flag:

- dead-weight openings such as "it is important to note that"
- meta openers such as "in other words" or "this means that"
- wordy causal bridges such as "due to the fact that"
- vague filler such as "in terms of"
- redundant modifiers such as "completely eliminate" or "future plans"

Prefer direct nouns and verbs over padding.

### 2. Voice and verb vitality

Check whether the sentence makes accountability and action visible.

Flag:

- passive voice that hides the actor when the actor matters
- nominalizations or smothered verbs such as "conducted an analysis of"
- weak verb choices when a specific verb would shorten and clarify the sentence

Do not rewrite every passive sentence. Passive is acceptable when the actor is unknown, irrelevant, or conventional for a Methods-style statement.

### 3. Sentence architecture

Check whether the sentence lets the reader find the predicate and the point quickly.

Flag:

- buried predicates
- long prepositional stacks before the main verb
- run-ons or overloaded coordination
- paragraphs with flat rhythm where every sentence has the same length and energy
- negation-based contrastive setup where the sentence could state the positive claim directly

Prefer short declarative sentences for emphasis and longer sentences only when they carry real explanation.

### 4. Keyword consistency and terminology

Technical writing should reuse its defined terms faithfully.

Flag:

- synonyms introduced for already-defined technical entities
- inconsistent group names, variable names, assay names, or abbreviations
- acronyms defined in one location but not at first use elsewhere

Apply the banana rule: do not rename a banana just to avoid repetition.

### 5. Numerical and citation integrity

Check sentence-level consistency around reported facts.

Flag:

- sample sizes that disagree across abstract, results, figures, or tables
- percentages that do not match raw numbers already present in the material
- inconsistent precision or unit formatting
- claims stated as established facts but only supported through secondary citations

Do not invent corrections. Mark them as verification items when the primary artifact is missing.

## Severity guidance

Use lightweight severity tags to keep the review actionable:

- `critical`: distorts meaning, hides accountability, or creates a likely reader misunderstanding
- `major`: materially hurts clarity, flow, or consistency
- `minor`: awkward, wordy, or locally improvable without changing interpretation

## Output pattern

For review-style requests, prefer this structure:

1. `Writing review mode`
2. `Summary`
3. `Findings by pass`
4. `Top priority revisions`
5. `Revised text` or `Example rewrites` when the user asked for edits

When the user explicitly wants high-journal expression, add:

6. `Expression upgrades`

For interactive requests, go paragraph by paragraph and keep each round small:

- original
- revised
- why this change helps

## Boundary

- Do not let sentence-level cleanup silently strengthen unsupported claims.
- If the main problem is conceptual overclaim, route through `claim` before or alongside this audit.
- If the user asks for prose review but the material contains unresolved numerical or citation mismatches, surface them as verification items rather than polishing over them.
