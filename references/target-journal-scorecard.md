# Target-Journal Scorecard

Use this reference when the user asks how far a manuscript or submission package is from a named target journal, Codex supplies an external Goal context, the user asks for a score, wants a publishability gap estimate, or needs a repair plan before submission.

## Navigation

- Purpose and limits
- Mandatory triggers
- Evidence basis and confidence
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

## Scoring axes

Use a 100-point score. Award points only for inspectable evidence. If a dimension is unknown, assign a provisional score and mark the missing input.

| Axis | Points | What to check |
|---|---:|---|
| Problem significance and journal audience fit | 12 | Importance, audience breadth, target-journal discourse bridge, field relevance |
| Novelty and contribution clarity | 12 | Clear advance over closest prior work, contribution type, non-incremental framing |
| Evidence depth and result strength | 16 | Data completeness, controls, validation, uncertainty, robustness, causal or mechanistic support where relevant |
| Methods, statistics, reproducibility and parameter provenance | 14 | Method transparency, equations, statistical logic, code/data availability, sourced parameters and sensitivity ranges |
| Claim calibration and limitations | 10 | Claims match evidence, causal wording is bounded, limitations are specific and not defensive |
| Literature positioning and reference adequacy | 10 | Citation coverage, direct support quality, closest prior work, formatting and sequence |
| Figures, tables, source data and SI alignment | 10 | Figure-accounting consistency, legends, source data, SI pointers, table/equation consistency |
| Manuscript architecture and writing quality | 8 | Abstract, introduction, results/discussion logic, paragraph flow, non-AI manuscript expression |
| Submission package cleanliness and journal format | 8 | Internal-trace removal, cover letter, availability statements, journal headings, display formats, file/package readiness |

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

## Blocking caps

Apply caps after summing the axis scores. Explain every cap.

- No concrete manuscript or package artifact: cap at 50.
- No named target journal or tier: cap target-specific confidence at low and cap at 70.
- Unsupported core result, fabricated reference/data/parameter, or unresolved parameter provenance gap in a central claim: cap at 40 until fixed.
- Main claim stronger than available evidence: cap at 60.
- Serious methods opacity, missing validation, missing uncertainty treatment, or non-reproducible analysis basis: cap at 70.
- Figure, table, source-data or SI accounting drift affecting headline claims: cap at 65.
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
5. Checkpoint the current score, target score, top blockers, and next verification step.
6. After revisions, rescore only the changed dimensions unless the manuscript architecture changed globally.

Do not let Codex Goal context turn into blind optimization. If a higher score would require unsupported claims, fabricated support, or journal overreach, recommend retargeting or narrowing the claim instead.

## Output contract

When this scorecard is triggered, return:

- `Target and evidence basis`
- `Overall score`
- `Gap to target`
- `Score by dimension`
- `Blocking caps`
- `Highest-leverage repairs`
- `Codex Goal next actions` when external goal context is active
- `Rescore conditions`

For generated papers, also include whether the generated text contains unsupported claims, parameter gaps, invented references, internal traces, or package residue before assigning a high score.
