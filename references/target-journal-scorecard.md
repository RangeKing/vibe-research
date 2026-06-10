# Target-Journal Scorecard

Use this reference when the user asks how far a manuscript or submission package is from a named target journal, Codex supplies an external Goal context, the user asks for a score, wants a publishability gap estimate, or needs a repair plan before submission.

## Navigation

- Purpose and limits
- Score bands and calibration
- Mandatory triggers
- Evidence basis and confidence
- Artifact update policy
- Scoring axes
- Conservative scoring defaults
- Anti-inflation guardrails
- Target bars and gap classes
- High-score gates
- Blocking caps
- Calibration anchors
- Codex Goal compatibility
- Output contract

## Purpose and limits

The scorecard converts a manuscript-readiness assessment into a structured target-journal gap artifact. It should help the user decide what to fix next, whether to retarget, and how much work remains before the package is credible for the stated venue.

This score is not an acceptance probability, a prediction of editorial decisions, or a substitute for official author guidelines. Treat it as a structured editorial and evidence-readiness rubric.

The score is an optimization target for iterative repair loops, not a grade for encouragement. A useful score is one that a hostile reviewer would not laugh at. When the honest score is 48, report 48; reporting 90 for an unfinished package destroys the measurement value of the whole loop.

Do not use the score to hide uncertainty. If the manuscript, figures, references, SI, or target-journal rules are incomplete, mark score confidence as low or provisional and apply the relevant cap.

## Score bands and calibration

Calibrate every score against these bands. The bands describe expected editorial and reviewer behavior at the stated target journal, judged strictly.

| Band | Meaning |
|---|---|
| 0-59 | Not submission-ready. Major conceptual, methodological, evidentiary, structural, writing, or positioning problems remain. Do not submit. |
| 60-69 | Barely submission-ready. 60 means just good enough to submit, but the manuscript is weak and will likely draw serious editorial or reviewer criticism. |
| 70-79 | Some chance of editorial handling. The editor may send it out for review, but desk rejection remains plausible. Substantial improvement is still needed. |
| 80-89 | Likely to be sent for review. Reviewers are expected to raise many substantive comments. |
| 90-99 | Very strong manuscript. The editor would almost certainly send it out, and reviewers would likely have only a small number of substantive comments. Scores in this band should be rare. |
| 100 | Near-perfect manuscript. Expert reviewers would struggle to find a meaningful criticism. Almost unreachable; assign only when the manuscript is exceptionally polished, novel, rigorous, well-evidenced, clearly positioned, and publication-ready at the target-journal level. |

Calibration rules:

- Most real drafts, including fluent AI-generated drafts, honestly land in the 0-59 or 60-69 bands on first scoring. Treat that as the normal starting state, not a failure of the rubric.
- A score of 90+ asserts that a demanding reviewer would find only a handful of minor issues. Before reporting 90+, list the remaining reviewer-level issues explicitly; if the list contains any major item, the score is wrong.
- 95+ is reserved for an exceptionally rigorous, nearly publication-ready manuscript. 100 is effectively reserved for a manuscript where expert reviewers would struggle to find meaningful criticism.
- When uncertain between two adjacent scores or bands, always report the lower one.
- Always report the band meaning next to the number so downstream loops do not misread the score.

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

## Conservative scoring defaults

The burden of proof is on the manuscript, not on the reviewer. Score each axis as a skeptical referee, not as a supportive coauthor.

- Every axis starts at zero. Award points only for strengths you actually inspected and verified, never for strengths that are merely plausible, claimed, or implied by fluent prose.
- A dimension that could not be inspected scores at most 40% of its axis maximum, is marked provisional, and pulls overall score confidence down.
- Penalize, do not merely withhold points for: unresolved weaknesses, vague claims, missing evidence, weak novelty, unclear methods, poor literature positioning, overclaiming, internal inconsistency, incomplete figures or tables, weak discussion, and journal-fit problems. Each identified problem must visibly cost points on its axis and appear in the diagnostic output.
- An axis with an unresolved major flaw scores at most half of its maximum, regardless of how strong the rest of that axis looks.
- When uncertain between two scores on an axis, assign the lower one.
- Sum the axes, then apply the lowest applicable blocking cap. Never round up across a band boundary.

## Anti-inflation guardrails

These guardrails are mandatory. A score that violates any of them is invalid and must be recomputed.

- Fluent writing alone never raises the score. Polished, confident, well-organized prose with weak evidence is still a 0-59 band manuscript. Writing quality affects only the writing axis, which is 8 points.
- Plausible-sounding but unsupported claims earn zero credit on the evidence and claim axes and trigger the overclaim or unsupported-result caps when they touch central claims.
- Strong sections do not compensate for fatal flaws elsewhere. The total is capped by the worst unresolved problem, not lifted by the best section.
- Any fatal flaw caps the total below 60 until it is clearly fixed and re-verified.
- Any major unresolved flaw caps the total below 80 unless there is a documented, verified reason it does not block editorial handling.
- A score above 90 requires zero fatal flaws, zero major unresolved flaws, a passed Methods/SI reproducibility gate, and an explicit list showing that only a small number of minor reviewer-level issues remain.
- Completeness is not quality. Having all expected files, sections, figures, and word counts is the entry ticket, not a score driver.
- Do not raise a score between iterations unless a specific blocker was fixed and re-verified. "The text reads better now" is not a rescore justification.
- Never choose a score to encourage the author or to make an iteration loop look like progress. Score stagnation under honest scoring is real information.

## Target bars and gap classes

Use journal-specific guidance when available. Otherwise use these heuristic target bars, read against the strict score bands above:

- `flagship_general`: 90+
- `selective_field`: 85+
- `broad_selective`: 80+
- `strong_specialist`: 75+

Under strict calibration these bars are hard to reach. That is intended: a package that honestly scores 85 should genuinely be likely to go out for review at a selective field journal.

Gap to target = target bar minus current score. Interpret the gap:

- `0-4`: at the heuristic bar, but still not a publication guarantee
- `5-9`: close; fix the top blockers before submission
- `10-19`: promising but needs focused repair before that target
- `20+`: major evidence, positioning, package, or target-choice gap

If the user gives a custom target score, use it and state that it is user-defined. Do not relax the band calibration to make a custom target easier to hit.

## High-score gates

A package cannot score at or above 90/100, or 9/10, merely because it has the expected files, acceptable word counts, no visible internal paths, and complete figure/source-data names. A 90+ score additionally requires that no fatal or major flaw remains anywhere in the package and that the remaining issues are explicitly enumerated as minor reviewer-level items. High scores require a scientific reproducibility gate:

- Methods and SI let a reader reproduce the workflow step by step from data inputs to figures, tables and headline claims.
- Formal equations or logical predicates exist for scores, ordinal classes, ranking rules, adequacy matrices, sensitivity readouts and validation checks.
- Parameter provenance, thresholds, weights, class boundaries and missing-data rules are tabulated.
- Sensitivity and validation outputs are inspectable, not only described as a "logic check".
- If the target files are `.docx`, methods/SI formulas are Word Office Math objects where formulas are part of the work; a formula-bearing package with zero `m:oMath` objects cannot pass the high-score gate.

If this gate is not checked, mark score confidence no higher than medium. If it fails, apply the relevant cap before reporting the score.

## Blocking caps

Apply caps after summing the axis scores. Apply the lowest applicable cap, explain every cap, and classify each as fatal (caps below 60) or major (caps below 80) so the band logic stays visible.

Fatal-flaw caps (manuscript is not submission-ready until fixed):

- Unsupported core result, fabricated or invented reference/data/parameter, or unresolved parameter provenance gap in a central claim: cap at 40 until fixed.
- No concrete manuscript or package artifact to inspect: cap at 45.
- Central claim materially stronger than the available evidence: cap at 55 until the claim is narrowed or the evidence is added.
- Internal inconsistency or figure/table/source-data/SI accounting drift that affects headline claims: cap at 55.
- Methods so opaque that the central analysis cannot be assessed or reproduced even in outline: cap at 55.
- Three or more distinct major flaws active at once: cap at 59; the package is not submission-ready regardless of axis sums.

Major-flaw caps (editorial handling at risk until fixed):

- No named target journal or tier: cap target-specific confidence at low and cap at 70.
- Serious methods opacity in non-central analyses, missing validation, missing uncertainty treatment, or a non-reproducible analysis basis: cap at 65.
- Methods and SI are too thin for step-by-step reviewer reproduction, even if package files are present: cap at 65.
- Weak or unclear novelty for the stated target: closest prior work not identified, or the advance over it not demonstrated: cap at 70.
- A quantitative, ordinal, screening, ranking or sensitivity-based package lacks formal equations/predicates and threshold/coefficient tables: cap at 70.
- Missing or clearly inadequate reference coverage or literature positioning for a selective target: cap at 70.
- Readiness score is based mainly on package-cleanliness checks such as word counts, file presence and path scans rather than scientific reproducibility: cap at 70 until a full scorecard is run.
- Weak, missing, or boilerplate Discussion or limitations treatment for the stated target: cap at 75.
- Serious figure readability or production-layout failure in main display items, including large rendered whitespace imbalance, distorted map aspect, misleading unused semantic colorbar segments, or text collisions: cap at 75 until labels, legends, whitespace, scale use and rendered previews are fixed.

Submission-package caps (cannot reach the 90-99 band until fixed):

- A formula-bearing Word `.docx` submission has equations rendered only as plain text, or zero verified Office Math objects in the relevant main/SI files: cap at 80.
- Internal trace leakage, local filenames, draft-management residue, or package-format blockers in editor-facing text: cap at 80.
- Missing cover letter, data/code availability, ethics/competing-interest statements, or required package statements: cap at 85.

Caps identify why the package is not yet credible for the target submission state. A capped score must always report which cap is active and what fixes would lift it.

## Calibration anchors

Use these anchors to check any score before reporting it. If a computed score contradicts an anchor, the computed score is wrong.

- A weak but fluent draft, with confident polished prose over unsupported claims, missing validation, or thin methods, must not score above 60. Expected band: 0-59.
- A merely decent draft, scientifically sound but unremarkable, with several major gaps in evidence depth, positioning, or methods detail, must not score above 70.
- A good but clearly improvable manuscript, with solid evidence and no fatal flaws but obvious reviewer targets in novelty framing, robustness, figures, or discussion, must not score above 80.
- A strong manuscript that a reviewer would still engage with substantively, raising several real comments, must not score above 90.
- 95+ is possible only for an exceptionally rigorous, nearly publication-ready manuscript with a passed Methods/SI reproducibility gate, complete package, and only trivial residual issues.
- 100 is effectively reserved for a manuscript where expert reviewers would struggle to find meaningful criticism. Treat any computed 100 as a signal to re-audit before reporting it.

## Codex Goal compatibility

When Codex supplies an external Goal context or target score, treat the scorecard as the measurement layer for that external goal. Do not define a separate internal mode.

1. Record the external goal: target journal, target bar, current evidence basis, and stop condition.
2. Score the current artifact and list blocking caps.
3. Compute the gap to target and identify the smallest set of repairs with the largest score gain.
4. Convert repairs into a short action plan with expected score impact, required evidence, and owner input.
5. Update the canonical `target_journal_scorecard.md` in place, including the current score, target score, top blockers, changed dimensions, and next verification step.
6. After revisions, rescore only the changed dimensions unless the manuscript architecture changed globally. Raise a dimension only when its specific blocker was fixed and re-verified; keep the band calibration as strict on iteration 10 as on iteration 1.

Do not let Codex Goal context turn into blind optimization. If a higher score would require unsupported claims, fabricated support, or journal overreach, recommend retargeting or narrowing the claim instead. An honest plateau below the target score is a valid loop outcome; report it as such rather than drifting the calibration upward.

## Output contract

When this scorecard is triggered, return:

- `Artifact update`
- `Target and evidence basis`
- `Overall score`
- `Score band meaning`
- `Main reasons for the score`
- `Score history`
- `Methods/SI reproducibility gate`
- `Gap to target`
- `Score by dimension`
- `Blocking caps`
- `Blockers to the next band`
- `Path to higher bands`: the concrete fixes required to reach 60, 70, 80, 90, or 100, for whichever rungs are above the current score
- `Highest-leverage repairs`
- `Codex Goal next actions` when external goal context is active
- `Rescore conditions`

The diagnostic sections are not optional. Every reported score must explain the number, the band meaning, the main reasons, the most important blockers preventing the next band, and the concrete fixes required to climb.

For generated papers, also include whether the generated text contains unsupported claims, parameter gaps, invented references, internal traces, or package residue before assigning a high score.
