# Target-Journal Scorecard

Use this reference when the user asks how far a manuscript or submission package is from a named target journal, Codex supplies an external Goal context, the user asks for a score, wants a publishability gap estimate, or needs a repair plan before submission.

## Navigation

- Purpose and limits
- Mandatory triggers
- Evidence basis and confidence
- Artifact update policy
- Scoring axes
- Target bars and gap classes
- Blocking caps
- Codex Goal compatibility
- Output contract

## Purpose and limits

The scorecard converts a manuscript-readiness assessment into a structured target-journal gap artifact. It should help the user decide what to fix next, whether to retarget, and how much work remains before the package is credible for the stated venue.

This score is not an acceptance probability, a prediction of editorial decisions, or a substitute for official author guidelines. Treat it as a structured editorial and evidence-readiness rubric.

Do not use the score to hide uncertainty. If the manuscript, figures, references, SI, or target-journal rules are incomplete, mark score confidence as low or provisional and apply the relevant cap.

## Mandatory triggers

Run this scorecard when any of the following is true:

- the user asks for a score, scoring system, rating, distance, gap, readiness index, or publication gap
- the user asks whether a generated paper or submission package can reach a target journal
- Codex supplies an external Goal context, target score, stop condition, or target-journal objective
- the task is a full submission-package audit with a named journal or journal tier
- the user asks what needs to change to reach a higher journal tier

## Evidence basis and confidence

Classify what was actually inspected:

- `complete_package`: manuscript, figures/tables, references, SI, cover letter or package statements, and target-journal constraints were available.
- `manuscript_only`: main text and references were available, but package files or SI were missing.
- `partial_artifact`: only abstract, selected sections, figures, or a summary were available.
- `verbal_summary`: no inspectable manuscript artifact was available.

Then set score confidence:

- `high`: complete package or manuscript plus enough target-journal constraints were inspected.
- `medium`: manuscript is available, but some package or guideline checks are missing.
- `low`: only partial artifacts or verbal summaries were available.

## Artifact update policy

Use one canonical scorecard file per active manuscript package or project:

- Default filename: `target_journal_scorecard.md`.
- If a scorecard already exists, edit that file in place. Do not create `target_journal_scorecard_v1.md`, `target_journal_scorecard_v2.md`, or similar iterative files.
- If older numbered scorecards already exist, read the highest trustworthy version as prior state, then migrate the current score into `target_journal_scorecard.md` and continue there.
- Preserve history inside the same file with a compact `Score history` table: date, score, cap, top blocker, and changed dimensions. Keep full evidence ledgers, source audits, and long work logs in their own artifacts, then link or name them from the scorecard.
- Create an archival snapshot only when the user explicitly asks, the target journal changes, or the artifact basis changes so much that comparison would be misleading. Put snapshots under an `archive/` or `scorecard_archive/` folder with date-based filenames rather than cluttering the package root.

The scorecard should be a live measurement artifact, not a running transcript. Keep `Target and evidence basis` to the current inspectable basis and the meaningful delta since the last score. Prefer 5-10 evidence bullets plus links to supporting audits over hundreds of lines of accumulated history.

## Scoring axes

Use a 100-point score. Award points only for inspectable evidence. If a dimension is unknown, assign a provisional score and mark the missing input. Score figure scientific alignment separately from figure visual quality: a figure can be scientifically consistent but still lose points for unreadable labels, poor layout, excessive whitespace, or weak visual hierarchy.

| Axis | Points | What to check |
|---|---:|---|
| Problem significance and journal audience fit | 11 | Importance, audience breadth, target-journal discourse bridge, field relevance |
| Novelty and contribution clarity | 11 | Clear advance over closest prior work, contribution type, non-incremental framing |
| Evidence depth and result strength | 15 | Data completeness, controls, validation, uncertainty, robustness, causal or mechanistic support where relevant |
| Methods, statistics, reproducibility and parameter provenance | 13 | Method transparency, equations, statistical logic, code/data availability, sourced parameters and sensitivity ranges |
| Claim calibration and limitations | 10 | Claims match evidence, causal wording is bounded, limitations are specific and not defensive |
| Literature positioning and reference adequacy | 9 | Citation coverage, direct support quality, closest prior work, formatting and sequence |
| Figures, tables, source data and SI alignment | 8 | Figure-accounting consistency, legends, source data, SI pointers, table/equation consistency |
| Figure quality and visual communication | 8 | Panel design, text readability, label wrapping, whitespace balance, visual hierarchy, color/legend clarity, render checks |
| Manuscript architecture and writing quality | 8 | Abstract, introduction, results/discussion logic, paragraph flow, non-AI manuscript expression |
| Submission package cleanliness and journal format | 7 | Internal-trace removal, cover letter, availability statements, journal headings, display formats, file/package readiness |

## Target bars and gap classes

Use journal-specific guidance when available. Otherwise use these heuristic target bars:

- `flagship_general`: 90+
- `selective_field`: 85+
- `broad_selective`: 80+
- `strong_specialist`: 75+

Gap to target = target bar minus current score. Interpret the gap:

- `0-4`: at the heuristic bar, but still not a publication guarantee
- `5-9`: close; fix the top blockers before submission
- `10-19`: promising but needs focused repair before that target
- `20+`: major evidence, positioning, package, or target-choice gap

If the user gives a custom target score, use it and state that it is user-defined.

## High-score gates

A package cannot score at or above 90/100, or 9/10, merely because it has the expected files, acceptable word counts, no visible internal paths, and complete figure/source-data names. High scores require a scientific reproducibility gate:

- Methods and SI let a reader reproduce the workflow step by step from data inputs to figures, tables and headline claims.
- Formal equations or logical predicates exist for scores, ordinal classes, ranking rules, adequacy matrices, sensitivity readouts and validation checks.
- Parameter provenance, thresholds, weights, class boundaries and missing-data rules are tabulated.
- Sensitivity and validation outputs are inspectable, not only described as a "logic check".
- If the target files are `.docx`, methods/SI formulas are Word Office Math objects where formulas are part of the work; a formula-bearing package with zero `m:oMath` objects cannot pass the high-score gate.

If this gate is not checked, mark score confidence no higher than medium. If it fails, apply the relevant cap before reporting the score.

## Blocking caps

Apply caps after summing the axis scores. Explain every cap.

- No concrete manuscript or package artifact: cap at 50.
- No named target journal or tier: cap target-specific confidence at low and cap at 70.
- Unsupported core result, fabricated reference/data/parameter, or unresolved parameter provenance gap in a central claim: cap at 40 until fixed.
- Main claim stronger than available evidence: cap at 60.
- Serious methods opacity, missing validation, missing uncertainty treatment, or non-reproducible analysis basis: cap at 70.
- Methods and SI are too thin for step-by-step reviewer reproduction, even if package files are present: cap at 70.
- A quantitative, ordinal, screening, ranking or sensitivity-based package lacks formal equations/predicates and threshold/coefficient tables: cap at 75.
- A formula-bearing Word `.docx` submission has equations rendered only as plain text, or zero verified Office Math objects in the relevant main/SI files: cap at 80.
- Readiness score is based mainly on package-cleanliness checks such as word counts, file presence and path scans rather than scientific reproducibility: cap at 75 until a full scorecard is run.
- Figure, table, source-data or SI accounting drift affecting headline claims: cap at 65.
- Serious figure readability or production-layout failure in main display items: cap at 75 until labels, legends, whitespace, and rendered previews are fixed.
- Missing or clearly inadequate reference coverage for a selective target: cap at 75.
- Internal trace leakage, local filenames, draft-management residue, or package-format blockers in editor-facing text: cap at 80.
- Missing cover letter, data/code availability, ethics/competing-interest statements, or required package statements: cap at 85.

Caps do not imply the paper is weak overall; they identify why it is not yet credible for the target submission state.

## Codex Goal compatibility

When Codex supplies an external Goal context or target score, treat the scorecard as the measurement layer for that external goal. Do not define a separate internal mode.

1. Record the external goal: target journal, target bar, current evidence basis, and stop condition.
2. Score the current artifact and list blocking caps.
3. Compute the gap to target and identify the smallest set of repairs with the largest score gain.
4. Convert repairs into a short action plan with expected score impact, required evidence, and owner input.
5. Update the canonical `target_journal_scorecard.md` in place, including the current score, target score, top blockers, changed dimensions, and next verification step.
6. After revisions, rescore only the changed dimensions unless the manuscript architecture changed globally.

Do not let Codex Goal context turn into blind optimization. If a higher score would require unsupported claims, fabricated support, or journal overreach, recommend retargeting or narrowing the claim instead.

## Output contract

When this scorecard is triggered, return:

- `Artifact update`
- `Target and evidence basis`
- `Overall score`
- `Score history`
- `Methods/SI reproducibility gate`
- `Gap to target`
- `Score by dimension`
- `Blocking caps`
- `Highest-leverage repairs`
- `Codex Goal next actions` when external goal context is active
- `Rescore conditions`

For generated papers, also include whether the generated text contains unsupported claims, parameter gaps, invented references, internal traces, or package residue before assigning a high score.
