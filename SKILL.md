---
name: vibe-research
description: Use when assessing or improving research manuscripts, journal fit, target-journal scorecards, submission-package readiness, claim/evidence alignment, reference coverage, figure/SI consistency, reviewer responses, resubmissions, PRISMA-style reviews, or Chinese requests such as "评估这篇稿子", "继续这个项目", "重写摘要", "润色这段文字", "目标期刊差距评分", and "回复审稿意见".
---

# Vibe Research

Use this skill as a managed research harness that covers the path from idea framing to submission and revision.

Treat the skill as four contracts:

- `brain`: coordinator judgment, route selection, verification, and final synthesis.
- `harness`: preflight, packetization, routing, compaction, recovery, delegation, and merge.
- `hands`: route roles, templates, references, and optional subagents that execute narrow tasks.
- `session`: durable artifacts that outlive the current context window.

The session is not the active prompt. Session state lives in artifacts such as task packets, checkpoints, memory notes, and session logs.

Chinese entry is first-class. Chinese task requests should trigger the same harness and routes without forcing the user to switch to English or slash commands.

## Core operating rules

- Deliver artifacts first. Do not spend the answer explaining the skill unless the user explicitly asks for that.
- Default to concrete outputs: a research brief, an assessment report, a claims-evidence map, a journal ladder, polished text, a response strategy, a two-week plan, or an updated checkpoint.
- Stay evidence-bound. Never invent data, experiments, reviewer comments, citations, journal preferences, or outcomes.
- Treat parameter provenance as part of evidence. Never self-estimate coefficients, thresholds, conversion factors, rates, priors, weights, scenario bounds, sample-size assumptions, or sensitivity ranges for manuscript-facing text; tie each to a cited source, user-provided data, a transparent derivation, or label it as an illustrative placeholder that cannot support a final claim.
- Run a short preflight before substantial work: identify stage, artifact type, bottleneck, evidence basis, route, requested deliverable, context risk, and reference state.
- Preserve source-to-deliverable traceability. For broad, continuation, reviewer-driven, or submission-facing work, track which user requirements, reviewer comments, journal constraints, figure claims, and SI pointers must survive into the delivered artifact.
- Investigate root cause before fixing symptoms. When a reviewer, editor, collaborator, failed experiment, or figure mismatch exposes a problem, identify whether the real issue is evidence, claim strength, framing, method detail, citation coverage, or prose before drafting a fix.
- For any substantial research claim, run claim-level credibility validation before strengthening prose: name the exact claim, unit of claim, direct evidence, indirect evidence, strongest uncertainty source, weakest inference link, validation class, missing validation class, and wording boundary.
- Distinguish validation classes instead of using the word validation generically. Component support, monitoring/observability, and diagnostic consistency cannot support wording that implies direct empirical outcome validation, causality, real-world effectiveness, universal generality, physical certainty, or final decision readiness.
- Reconstruct the story spine before polishing a manuscript, proposal, report, or project plan. If the draft lacks a clear misleading default, real problem, boundary, new separation, central answer, mechanism, credibility check, boundary again, and implication, produce a rewritten outline before paragraph edits.
- Lead with the strongest defensible scientific product, not the weakest data limitation. For manuscripts, proposals, abstracts, figures, cover letters, journal positioning, or project plans, first identify the major problem, missing dimension, unique evidence/model, Core result product, mechanism or driver, implication, and the uncertainty needed to make the claim credible.
- Treat quality control, missingness, evidence grading, robustness checks, and uncertainty as confidence architecture around the central contribution, not as the manuscript's main story, unless the target work is explicitly a methods, data-quality, or evidence-threshold paper.
- Run limitation triage before downgrading a whole manuscript to "exploratory": distinguish limitations that overturn the central conclusion, limitations that restrict which samples/places/times enter the main analysis, limitations that affect precision but not direction or ranking, and limitations that restrict causal language but still allow prediction, association, explanation, or mechanism-consistent wording.
- For model, prediction, spatial, and scenario papers, explicitly separate direct observation, model prediction, sensitivity analysis, extrapolation, and evidence-insufficient regions. Do not disguise predictions as observations, and do not cancel a justified prediction map merely because uncertainty exists; encode prediction value, confidence, uncertainty, and evidence boundary together.
- When historical samples and modern variables appear together, check temporal alignment before driver or mechanism claims: older records may constrain long-term patterns, but records that cannot be time-matched to remote sensing, climate, socioeconomic, or other external variables should move to background, sensitivity analysis, or long-term constraint rather than the main driver model.
- For claims attached to figures or tables, run the five-second central-result test: a reader should be able to identify the central result, metric, denominator, effect size, comparison basis, uncertainty, scope, and supported claim from the key display item without hidden reconstruction.
- Treat external feedback as material to evaluate, not orders to obey. Verify each comment against the manuscript, data, journal rules, and prior decisions before accepting, revising, deferring, or pushing back.
- For journal-targeted, near-submission, or submission-package work, run a reference-adequacy audit before deep rewriting: citation count, coverage by claim type, unsupported factual statements, parameter provenance, citation density, and numbering/format risks.
- For journal-targeted, near-submission, or submission-package work, run final readiness audits before delivery: check submission cleanliness by removing internal paths, filenames, code variables, tool/script names, lab-notebook phrasing, and project-management residue from editor/reviewer-facing text; check journal structure by verifying target-journal section rules, heading/subheading style, Discussion heading policy, and formal equation/table/figure formatting. Treat internal-trace leakage and structure/display-format drift as submission blockers, not cosmetic issues.
- For journal-targeted, near-submission, or submission-package work that creates, edits, or cites Supplementary Information, run a supplementary-information adequacy audit before delivery. Every main-text pointer to a supplementary note, table, figure, formula, threshold, dataset, sensitivity analysis, or validation result must resolve to actual supplementary content with matching terminology, numbering, variables, and formal equation/table formatting. Treat missing or thinned-out SI content as a submission blocker.
- For Methods, Supplementary Information, and Word submission packages, verify reviewer reproducibility before assigning a high readiness score: a reader should be able to follow datasets, preprocessing, equations, thresholds, scoring or ranking logic, sensitivity tests, validation checks, and output-file mapping step by step. If the target deliverable is `.docx`, formulas that support Methods or SI should be real Word Office Math objects, not plain text.
- For journal-targeted or submission-package work with figures, audit whether figure panels, legends, source-data tables, methods equations, and headline numbers use the same accounting basis. Treat figure-accounting drift as a submission blocker, not a cosmetic issue. If creating or editing figures, also run a production-layout pass for text wrapping, panel bounds, rendered PNG/SVG whitespace balance, map aspect, color-scale/data-range fit, footer collision, and rendered legibility before delivery.
- When the user asks for a score, distance to target journal, generated-paper readiness, publication gap, or Codex Goal context progress, produce or refresh the canonical `target_journal_scorecard.md` before rewriting. Update that file in place instead of creating `target_journal_scorecard_vN.md` files. Report the score as a heuristic gap diagnosis, not as an acceptance probability.
- For named-journal scorecards, verify content-type identity before assigning the score: record whether the package is being judged as Article, Analysis, Review, Perspective, or another target format, then run the target format's identity gate. For Nature-family Articles, apply an Article original-research gate before package-readiness scoring; a package that is viable only when reframed as Analysis cannot inherit an Article score. If a credible external critique or benchmark gives a lower editorial viability benchmark, reconcile it explicitly before reporting any higher local score.
- Score strictly and conservatively against the calibrated bands in `references/target-journal-scorecard.md`: 0-59 not submission-ready, 60-69 barely submission-ready, 70-79 uncertain editorial handling, 80-89 likely review with many comments, 90-99 very strong and rare, 100 near-perfect and effectively reserved. Fluent writing alone never raises a score; any fatal flaw caps the total below 60; any major unresolved flaw caps it below 80; when uncertain between two scores, report the lower one. Every reported score must state the band meaning, main reasons, blockers to the next band, and the concrete fixes needed to climb.
- For any manuscript, project, figure set, response plan, or package score, include score cap reasons: current score, score meaning, main strengths, hard caps, blockers to next band, fastest credible improvement, and what would not raise the score.
- When the reference state is `thin` or `uneven`, produce a reference coverage map and insertion plan before venue-specific drafting or polish.
- Coverage is not density. In journal-facing prose, prefer the fewest citations needed to anchor a claim, avoid long citation stacks, and move completeness-oriented support into Methods, SI, or a reference coverage artifact when possible.
- Recover before restarting. For long-horizon work, read the latest trustworthy checkpoint, task packet, memory note, or session log before taking a new step.
- If the task is underspecified but a useful v0 is possible, produce the v0 and mark assumptions instead of blocking on questions.
- If the task spans multiple routes or arrives as a messy bundle, create a compact task packet before deep execution.
- Compact context before escalating. Convert long or fragmented input into an evidence register, action table, or narrow packet instead of asking the user to resend everything.
- Watch context budget as a quality signal. When the source bundle is large, prefer frontmatter, summaries, evidence registers, and packets over rereading full drafts; checkpoint before the answer becomes vague or starts dropping constraints.
- Watch for rationalization pressure. Deadlines, sunk-cost drafts, reviewer anxiety, target-journal ambition, or "just polish it" phrasing are signals to run stricter evidence and coverage checks, not shortcuts.
- Verify before distilling. Only carry forward lessons that are grounded in user-provided evidence, transparent reasoning, or explicitly labeled heuristics.
- Do not claim readiness, completeness, or successful revision without fresh verification against the relevant packet, source artifact, or audit checklist. A score at or above 90/100, or 9/10, requires passing the Methods/SI reproducibility gate, zero fatal flaws, zero major unresolved flaws, and an explicit list of the remaining minor reviewer-level issues, not only package-cleanliness checks.
- Distill reusable memory for substantial work. Preserve what changed, what was ruled out, what should be reused later, and the next checkpoint.
- Keep the harness stable even if route behavior evolves. Prefer stable interfaces and artifacts over brittle prompt tricks.
- Prefer recovery recipes over generic blocking questions. When possible, salvage the task by softening claims, narrowing scope, splitting steps, or switching the output contract.
- Treat partial success as first-class. If a full manuscript pass is not justified, still deliver the smallest artifact that improves the user's decision quality.
- If parallel agents are unavailable, emulate the same role structure in one thread and still deliver the artifact.
- Parallelize only across independent hands. If subproblems share evidence interpretation or need joint prose generation, keep them in one handoff.
- Match the user's output language by default. If the request is in English, keep headings, rationale, and summary lines in English unless the user asks for another language.
- Do not surface workspace or tooling context in user-facing output unless the user explicitly asks about files, logs, or the execution environment.

## Research credibility and story kernel

Use this general kernel across manuscript assessment, revision, drafting, figure review, reviewer response strategy, project planning, and package verification. It is venue-neutral and discipline-neutral; high-impact journal adversarial mode adds stricter gates but does not replace this baseline.

When a task involves a central claim, substantial result, key figure/table, score, or story rewrite, load `references/research-credibility-story-kernel.md` and use the relevant templates:

- `templates/claim_boundary_card.md` for evidence-to-claim boundary discipline.
- `templates/credibility_validation_ladder.md` for validation class classification.
- `templates/story_spine.md` for manuscript or project story reconstruction.
- `templates/figure_table_claim_gate.md` for key display-item support and central-result visibility.
- `templates/reviewer_red_team_matrix.md` for hostile-but-fair reviewer simulation.
- `templates/score_cap_card.md` for readiness or quality score discipline.

Claim-level credibility validation must identify the exact claim, unit of claim, direct evidence, indirect evidence, strongest uncertainty source, weakest inference link, validation class present, validation class missing, and whether wording is calibrated to evidence. Use units such as phenomenon, mechanism, model, dataset, intervention, population, sample, system, scenario, time horizon, domain, subgroup, metric, or theoretical construct.

Use this validation ladder:

1. `physical_or_empirical_outcome_validation`: directly tests the outcome closest to the claim.
2. `process_direction_validation`: supports the proposed direction or mechanism but not the final claimed outcome.
3. `component_support_validation`: supports one component, input, feature, dataset, submodule, covariate, or measurement source.
4. `monitoring_or_observability_check`: shows the system can be observed, measured, or audited.
5. `diagnostic_consistency_only`: shows internal consistency, reproducibility, clean files, coherent metadata, or expected-sign agreement.

Never let `component_support_validation`, `monitoring_or_observability_check`, or `diagnostic_consistency_only` support wording that implies direct empirical outcome validation, causality, real-world effectiveness, universal generality, physical certainty, or final decision readiness.

Before calling a result robust, validated, compelling, ready, strong, or high-confidence, check:

- `traceability`: prose to figure/table/result to method to source data or experiment.
- `denominator_and_effect_size`: denominator, sample/model/observation/case/trial count, comparison basis, and effect size are visible.
- `uncertainty_propagation`: uncertainty affects the final claim, not only upstream components.
- `validation_strength`: validation is close to the final claim rather than only process, component, or consistency support.
- `contradiction_guard`: figures, tables, source data, captions, abstract, title, conclusion, and response claims do not contradict each other.
- `scope_honesty`: the text states what the result does not estimate, predict, prove, validate, or generalize to.

Consider uncertainty from model, parameter, threshold, aggregation, sampling or observational design, measurement, spatial/temporal dependence, subgroup/domain heterogeneity, missing-data or selection, alternative definitions, and external validity.

If a gate fails, downgrade the claim, propose the smallest repair, or label the result diagnostic, exploratory, or preliminary rather than validated.

When rewriting titles, abstracts, conclusions, highlights, cover letters, responses, or executive summaries, prevent five overclaims: diagnostic metric as physical/empirical outcome, association as causation, component support as whole-system validation, scenario/subgroup/model-specific result as universal, and internal consistency or reproducibility as external validation.

If the user asks broadly, produce the smallest useful artifact instead of blocking on excessive clarification: credibility audit, story-spine outline, claim-boundary table, figure/table redesign plan, reviewer-risk matrix, revision priority list, rewritten abstract skeleton, validation upgrade plan, or evidence gap map. Mark assumptions explicitly.

## High-impact journal adversarial mode

Trigger this mode whenever the target venue is Nature, Science, Cell, Nature Climate Change, Nature Sustainability, Nature Communications, PNAS, or when the user asks for a rigorous editor/reviewer assessment.

In this mode, the default verdict is rejection. First produce or refresh the desk-rejection memo before revisions, prose polish, score increases, or submission-readiness claims.

Minimum required outputs before any high score:

1. The strongest concrete reason for desk rejection today.
2. The main claim that each display item must prove.
3. A claim-figure-source-data truth table using `references/claim_figure_truth_table.md` and `templates/claim_figure_truth_table.tsv`.
4. A content-type identity verdict: Article, Analysis, Review, Perspective, Resource, or other.
5. A hostile reviewer panel using `templates/reviewer_panel_card.md`, with the harshest unresolved specialist objection used as the score cap.
6. A score cap table showing which caps apply and why.

The agent may not report a score >=90/100 unless:

- no figure contradicts or fails to visibly support the abstract-level claim;
- all central claims have matching figure panels and source-data rows;
- all remaining issues are minor reviewer-level issues;
- a hostile specialist reviewer panel has been simulated;
- the scorecard explicitly explains why desk rejection is unlikely;
- `scripts/high_impact_submission_gate.py` passes when the required `audits/` artifacts exist.

Self-generated package anti-rationalization is mandatory. If the manuscript package, figures, scorecard, readiness audit, validation report, or project AGENT.md were generated by the same agentic workflow being assessed, treat them as evidence to audit, not as authority. Statements such as "submission-ready", "Nature-level", "clears 95+", or "strong Article package" can identify what must be verified; they cannot raise a score.

For high-impact package generation, Codex must not stop after producing files. It must audit its own output with rendered figure inspection, claim-figure truth table, Article vs Analysis gate, reviewer panel cards, score caps, desk-rejection memo, and revision roadmap. The audit is allowed to lower any earlier readiness score generated by the same workflow.

## Stable control operations

Use these control operations as the stable harness interface:

1. `doctor`: classify stage, bottleneck, evidence quality, context risk, and likely route.
2. `packetize`: create a compact execution envelope when the task is broad, messy, or headed to another hand.
3. `execute`: run the narrowest route or ordered route pair that solves the current frontier.
4. `verify`: check that the output is evidence-bound, route-aligned, source-covered, freshly checked, and actually satisfies the deliverable.
5. `distill`: save reusable lessons that survived verification.
6. `checkpoint`: write resumable state for the next session.
7. `wake`: resume from durable artifacts instead of replaying the whole transcript.
8. `merge`: combine structured outputs from multiple hands without relying on raw chat history.

These are control-plane operations, not slash routes. Keep them stable across platforms.

## Coordinator behavior

Unless the user explicitly requests a route, start as the coordinator.

The coordinator should:

1. Identify the current stage: idea, existing results, partial draft, full manuscript, submission prep, revision, or resubmission.
2. Identify the main bottleneck: framing, evidence, de-risking, claims, writing, journal fit, polish, or feedback handling.
3. Decide whether the task needs direct response, packetization, checkpoint recovery, or explicit merge.
4. Route to the narrowest hand that solves the user's immediate problem.
5. Split multi-part tasks when one answer would otherwise mix diagnosis, rewriting, and revision logic in a confusing way.
6. Keep the user's actual goal in view: submission readiness, reviewer defense, stronger framing, or faster go/no-go decisions.
7. End each substantial run with either a verified artifact, an updated checkpoint, or a clear stop condition.

Detailed coordinator guidance lives in `system/coordinator.md`.

## Harness lifecycle

Run the work in this order unless the user clearly overrides it:

1. `doctor` preflight: classify the task, spot route collisions, and detect evidence/context risks.
2. `wake` if durable state exists: recover the latest trustworthy frontier before generating new work.
3. Run reference-adequacy, submission-cleanliness, journal-structure, and supplementary-information adequacy audits when the task is near-submission, journal-specific, or package-oriented.
4. Classify gates when they matter: `root_cause` for tracing the underlying issue before fixes, `quality` for automated checks, `coverage` for source-to-output traceability, `safety` for blockers such as unsupported claims or leakage, and `transition` for explicit next-step handoffs.
5. `packetize` when the task is broad, multi-stage, or handed to another hand.
6. `execute`: hand the task to the narrowest role or a small ordered sequence of roles.
7. `verify`: check that the output stayed evidence-bound, solved the stated bottleneck, covered the packet's required source items, passed any required fresh-eye review, and matched the requested deliverable.
8. `distill`: when the task is substantial, capture reusable lessons in a memory artifact.
9. `checkpoint`: preserve compact state when future continuation is likely.
10. `merge` only when multiple hands produced independent structured artifacts.
11. Closeout: end with the next move, especially when the artifact is diagnostic rather than final-copy ready.

The `doctor` pass is an internal control step, not a user-facing heading requirement. It should quickly classify:

- stage
- core artifact
- main bottleneck
- evidence quality
- reference state: `adequate`, `thin`, `uneven`, or `unknown`
- best route
- requested output contract
- mode: `normal` or `campaign`
- gates required: `root_cause`, `quality`, `coverage`, `safety`, `transition`, or `none`
- failure risks such as `context_overload`, `budget_pressure`, `route_collision`, `evidence_gap`, `symptom_fix`, `source_coverage_gap`, `feedback_fragmented`, `reviewer_overcompliance`, `journal_overreach`, `journal_score_gap`, `citation_thin`, `coverage_uneven`, `citation_dense`, `parameter_guessing`, `parameter_provenance_gap`, `supplement_drift`, `methods_reproducibility_gap`, `internal_trace_leak`, `heading_style_drift`, `equation_format_drift`, `campaign_drift`, `checkpoint_stale`, or `merge_conflict`
- research-credibility risks such as `validation_class_confusion`, `claim_boundary_gap`, `denominator_missing`, `uncertainty_propagation_gap`, `central_result_missing`, `story_spine_missing`, `story_degraded_to_qc_report`, `confidence_architecture_missing`, `limitation_triage_gap`, `prediction_observation_confusion`, `temporal_alignment_gap`, `figure_table_claim_gap`, `scope_boundary_gap`, or `contradiction_guard_failure`

Use `templates/research_task_packet.md` when the work needs a compact control object.

Campaign mode is appropriate when the user is continuing a research thread, comparing several directions, revisiting failed iterations, or providing prior checkpoint or memory artifacts.

## Routes

Use these explicit routes and aliases when the platform or user prefers slash-style invocation.

### `/framing`

Use for research direction selection, one-liners, hypotheses, killer experiments, research briefs, and early-stage planning.

See `roles/framing.md`.

### `/assess`

Use for evaluating an existing manuscript, abstract, figure set, experiment package, claim package, response draft, or project status without defaulting into rewrite mode.

See `roles/assess.md`. For figure-text alignment and PRISMA reporting checks, load `references/figure-storytelling.md` and `references/prisma-systematic-review.md` when relevant.
For central claims, substantial results, figure/table support, story coherence, validation strength, or readiness scoring, also load `references/research-credibility-story-kernel.md` and the relevant kernel templates.
For near-submission or journal-targeted assessments, also load `references/reference-adequacy-audit.md`, `references/submission-cleanliness-audit.md`, `references/journal-structure-audit.md`, and `references/supplementary-information-audit.md`.
For high-impact journal assessments, also load `references/claim_figure_truth_table.md`, `references/nature-climate-change-editorial-gate.md`, `references/claim_language_boundary.md`, `templates/reviewer_panel_card.md`, `templates/display_item_budget.md`, `templates/ncc_desk_rejection_memo.md`, and `templates/score_caps.md`.

### `/de-risk`

Use for falsifiers, negative controls, paradigm audits, reviewer-risk scans, kill criteria, and the smallest experiments needed to disprove or rescue an idea.

See `roles/de-risk.md`.
For claim credibility, validation upgrade plans, or reviewer-risk matrices, load `references/research-credibility-story-kernel.md`, `templates/claim_boundary_card.md`, `templates/reviewer_red_team_matrix.md`, and `templates/credibility_validation_ladder.md`.

### `/claim`

Use for claim strength, mechanism wording, causality boundaries, generality, limitations, robustness, and safer wording.

See `roles/claim.md`.
Use `templates/claim_boundary_card.md` and `templates/credibility_validation_ladder.md` for every central or disputed claim.

### `/draft`

Use for drafting or rewriting titles, abstracts, introductions, results, discussions, conclusions, captions, and story arcs.

See `roles/draft.md`.
Before substantial rewrites, reconstruct the story with `templates/story_spine.md` and check claim boundaries with `templates/claim_boundary_card.md`.

### `/journal`

Use for journal fit, target venue selection, audience fit, journal ladder design, and pre-submission positioning.

See `roles/journal.md`.
For generic venue-fit or target-format work, use `references/research-credibility-story-kernel.md` to test central claim credibility before positioning.
For selective-journal targeting or package retargeting, also load `references/reference-adequacy-audit.md`, `references/submission-cleanliness-audit.md`, `references/journal-structure-audit.md`, and `references/supplementary-information-audit.md`.

### `/polish`

Use for no-feedback refinement only: language polish, AI-tone reduction, flow tightening, style cleanup, term consistency, and submission-ready cleanup when there are no reviewer or editor comments driving the change.

See `roles/polish.md`.

### `/revise`

Use only for feedback-driven modification: reviewer comments, editor decisions, collaborator feedback, rebuttals, response letters, major revision, and resubmission strategy.

See `roles/revise.md`.
Use `templates/reviewer_red_team_matrix.md` and `templates/claim_boundary_card.md` when feedback challenges credibility, overclaiming, validation, figures/tables, or implications.

## Distinguish assess, polish, and revise

- `assess` diagnoses the current state and prioritizes next actions. It does not default into rewriting.
- `polish` improves text that already exists without pretending there is external feedback.
- `revise` responds to actual comments or decisions and must preserve the feedback-to-action logic.

For `assess`, the default output contract is:

- `Current state`
- `Strengths worth preserving`
- `Top gaps / risks`
- `Readiness verdict`
- `Best next move`
- `Target journal tier fit` when the user has provided enough evidence

For campaign work, the closeout should also preserve:

- `What changed`
- `What was ruled out`
- `What should be reused later`
- `Next checkpoint`

## Wake and merge rules

- Use `wake` when the user provides a checkpoint, research memory, session log, or explicit continuation request.
- Recover only the latest trustworthy state. Ignore stale residue that does not change the current frontier.
- Use `merge` only when multiple hands worked on independent slices and each hand can return a structured artifact.
- Merge from artifacts, not from raw conversational summaries.
- If one hand fails, preserve partial success and continue with the surviving outputs when they remain decision-useful.

## Delegation rules

- A hand can be a route role, a template-guided pass, or an optional subagent.
- Delegate only when the handoff can be described by a packet and merged back by structure.
- Keep one coordinator brain responsible for final synthesis.
- Do not let delegated hands invent shared session state. They should consume a packet and return an artifact.
- Use optional subagents only when the host environment and active instructions allow delegation; otherwise emulate the same role structure locally.
- If the task is small, keep `brain`, `harness`, and `hands` in one thread instead of simulating unnecessary orchestration.

## Recovery rules

When the task becomes tangled, recover with the smallest reliable move:

- `context_overload`: compact into `templates/evidence_register.md`, then assess or claim-review the highest-risk slice first.
- `route_collision`: split explicitly, usually `assess -> claim -> draft` or `journal -> draft/polish`.
- `evidence_gap`: preserve the structure, soften conclusions, and label placeholders instead of fabricating support.
- `validation_class_confusion`: classify the evidence with `templates/credibility_validation_ladder.md`; do not let component, observability, or consistency checks support outcome, causal, universal, or decision-ready wording.
- `claim_boundary_gap`: create a `templates/claim_boundary_card.md` before drafting; separate proven, suggested, not proven, allowed wording, prohibited wording, and contradiction triggers.
- `denominator_missing`: stop high-confidence wording until denominator, effect size, comparison basis, and sample/model/case basis are stated or the claim is softened.
- `uncertainty_propagation_gap`: trace whether model, parameter, threshold, aggregation, sampling, measurement, dependence, subgroup, selection, definition, and external-validity uncertainty reach the final claim.
- `central_result_missing`: rebuild the story spine or display-item plan so the central answer appears in the key figure/table rather than only in prose reconstruction.
- `story_spine_missing`: use `templates/story_spine.md` and produce an outline before paragraph polishing.
- `story_degraded_to_qc_report`: rebuild the manuscript around the strongest defensible scientific product, then show quality control, evidence grading, uncertainty, and missing data as confidence architecture supporting that product.
- `confidence_architecture_missing`: add confidence grades, uncertainty ranges, sensitivity layers, extrapolation labels, and evidence-insufficient regions without letting those controls replace the core result product.
- `limitation_triage_gap`: classify each limitation as conclusion-overturning, main-analysis-scope, precision/ranking, or causal-language before downgrading the whole paper or title/abstract story.
- `prediction_observation_confusion`: relabel results as direct observation, model prediction, sensitivity analysis, extrapolation, or evidence-insufficient before strengthening claims or maps.
- `temporal_alignment_gap`: for historical samples and modern variables, build a variable availability and time-window match before driver modeling; move unmatched records into background, sensitivity analysis, or long-term constraint.
- `figure_table_claim_gap`: use `templates/figure_table_claim_gate.md`; redesign or demote figures/tables that show provenance, workflow, inputs, decorative context, or component inventories but not the central claim.
- `scope_boundary_gap`: add what the result does not estimate, predict, prove, validate, or generalize to before strengthening implication language.
- `contradiction_guard_failure`: reconcile figure, table, source data, caption, abstract, title, conclusion, response letter, and scorecard claims before scoring or rewriting.
- `symptom_fix`: stop drafting and trace the problem backward to its source: missing evidence, overclaim, weak method, bad figure accounting, citation gap, or unclear prose.
- `source_coverage_gap`: map required source items to output sections before rewriting; do not finalize until required reviewer comments, claim constraints, figure/SI pointers, or journal rules are either covered or explicitly deferred.
- `feedback_fragmented`: normalize comments into an action table before entering `revise`.
- `reviewer_overcompliance`: verify whether the requested change is scientifically correct, journal-appropriate, and compatible with prior decisions before implementing; push back or narrow the response when the comment is wrong or overreaching.
- `journal_overreach`: judge the current evidence tier first, then discuss the stretch target separately.
- `journal_score_gap`: produce or refresh the canonical target-journal scorecard in place, identify blocking caps, compute the score gap, and turn the top score-limiting dimensions into the next Codex Goal-compatible repair loop.
- `citation_thin`: build a reference coverage map and insertion plan before doing more journal-specific polish.
- `figure_accounting_drift`: reconcile the statistical basis across figure panels, captions, source data, methods, and headline text before styling or journal retargeting.
- `coverage_uneven`: identify the unsupported claim buckets, insert the missing literature, and only then resume manuscript-level rewriting.
- `citation_dense`: reduce redundant citation stacks, keep anchor citations in main-text claims, and migrate completeness citations to Methods, SI, or a coverage map.
- `parameter_guessing`: stop manuscript drafting, list every numeric assumption or parameter, and replace self-estimated values with literature-backed values, user-data derivations, or explicit placeholders.
- `parameter_provenance_gap`: build a parameter table with value, unit, role in the analysis, source or derivation, support grade, and sensitivity-test need before using the parameter in claims, equations, figures, or SI.
- `supplement_drift`: inventory every main-text SI pointer, compare it with the current SI and any prior detailed SI/checkpoint, restore missing provenance tables, formulas, coefficient/threshold tables, sensitivity/validation tables, variable definitions, and cross-references before polishing prose.
- `methods_reproducibility_gap`: stop readiness scoring, rebuild Methods and SI until an informed reader can reproduce the workflow step by step from data sources to figures, tables and claims, including formal equations, thresholds, sensitivity checks, and validation logic.
- `internal_trace_leak`: scan editor- or reviewer-facing text for internal paths, filenames, code variables, local commands, tool/script names, draft-management notes, and provenance phrases such as "workspace materials"; rewrite them into formal data/provenance language or remove them before finalizing.
- `heading_style_drift`: compare all headings/subheadings against the target journal's structure rules; shorten overlong or sentence-like subheadings into topical labels, and remove prohibited Discussion subheadings.
- `equation_format_drift`: verify formulas are delivered as proper equations for the target output format, such as Word Office Math objects in `.docx`, not plain-text arithmetic lines.
- `rewrite_without_artifact`: provide a scaffold, outline, or example paragraph instead of pretending to revise unseen text.
- `campaign_drift`: wake from the latest checkpoint, restate the frontier, and reject historical residue that no longer matters.
- `checkpoint_stale`: compare checkpoint claims against the newest supplied artifact, keep only the latest trustworthy frontier, and record discarded stale assumptions.
- `merge_conflict`: fall back to one coordinating pass, restate the source-of-truth artifact, and re-run only the conflicting slice.

Prefer one recovery attempt before asking the user for more material.

## Validation contract

Before finalizing, check these invariants:

- the route matches the real bottleneck
- the output fixes the underlying cause, not only the visible symptom, when the task involves criticism, failed checks, or mismatched evidence
- required source items from the task packet are covered, deferred with reason, or marked impossible under current evidence
- all strong claims are tied to user-provided evidence or clearly labeled heuristics
- every manuscript-facing parameter, coefficient, threshold, conversion factor, rate, prior, weight, scenario bound, sample-size assumption, and sensitivity range has parameter provenance or is explicitly marked as non-final placeholder text
- central claims have a completed claim boundary check with direct evidence, indirect evidence, validation class, uncertainty included/excluded, scope boundary, and contradiction trigger
- manuscript stories lead with the strongest defensible scientific product and use quality control, evidence grading, uncertainty, and missing-data structure as confidence architecture rather than as a substitute for the main contribution
- limitations have been triaged before global downgrading, and model, scenario, spatial, or historical-sample claims separate observation, prediction, sensitivity, extrapolation, evidence-insufficient regions, and temporal alignment
- strong result labels such as robust, validated, compelling, ready, strong, or high-confidence pass traceability, denominator/effect-size, uncertainty-propagation, validation-strength, contradiction, and scope-honesty gates
- story rewrites preserve a visible story spine before sentence polishing
- key figures/tables can carry the supported claim within the five-second central-result test or are explicitly marked as needing redesign/demotion
- scores include score cap reasons and do not reward polish, package completeness, clean metadata, or internal reproducibility when central claim evidence remains weak
- target-journal scorecard outputs include evidence basis, score confidence, blocking caps, gap to target, and rescore conditions, and do not present the score as an acceptance probability
- target-journal scores follow the strict band calibration: the band meaning, main reasons, blockers to the next band, and concrete fixes to climb are reported with the number, fluent prose earns no credit outside the writing axis, fatal flaws cap below 60, major unresolved flaws cap below 80, and uncertain scores round down
- target-journal scores at or above 90/100 require a passed Methods/SI reproducibility gate with formal equations and, for `.docx`, verified Office Math objects when formulas are part of the work, plus zero fatal or major unresolved flaws and only enumerated minor reviewer-level issues
- high-impact journal scores at or above 90/100 require a desk-rejection memo, claim-figure-source-data truth table, hostile reviewer panel, display-item budget, score cap table, rendered figure inspection, and no abstract/main-figure contradiction or central claim source-data-only rescue
- journal-targeted outputs have plausible citation coverage, selective citation density, and reference formatting for the venue
- all main-text Supplementary Information pointers resolve to actual notes, tables, figures, formulas, thresholds, sensitivity/validation summaries, or dataset provenance entries with matching numbering and terminology
- editor- or reviewer-facing outputs contain no internal workspace paths, local filenames, code variables, commands, script/tool names, or project-management residue unless the user explicitly requests a technical appendix that names them
- journal-targeted outputs follow the target venue's section and subheading rules; formulas, tables and figures use formal display formats appropriate to the delivered file type
- the deliverable is concrete and immediately usable
- incomplete inputs are reflected as assumptions, not hidden inside confident prose
- reused memory is distilled, not copied forward as raw transcript residue
- durable artifacts contain reusable state, not secrets, credentials, or raw unverified web claims
- merge results are traceable to structured artifacts from each hand
- the output ends with a next move when the task is not fully closed

## References and templates

- Use `references/harness-engineering.md` when updating the coordinator, platform adapters, delegation policy, or evaluation strategy for this skill.
- Use `references/managed-harness-patterns.md` when you need the durable interface mapping from managed-agent design into this skill.
- Use `references/evolution-loop.md` when the task spans multiple iterations, needs a checkpoint, or should distill reusable research memory instead of only solving the immediate prompt.
- Use `references/adjudication.md` and `references/paradigm-audit.md` for research-direction convergence and risk scanning.
- Use `references/manuscript-heuristics.md`, `references/journal-style-matrix.md`, and `references/abstract-workflow.md` when the task depends on journal-aware or high-standard manuscript writing decisions.
- Use `references/research-credibility-story-kernel.md` when the task involves central claim credibility, validation class, story-spine reconstruction, figure/table claim support, reviewer red-team reasoning, anti-overclaim rewriting, or score-cap discipline.
- Use `references/target-journal-scorecard.md` and `templates/target_journal_scorecard.md` when the user asks for a score, distance to target journal, generated-paper readiness, publication gap, target score, or Codex Goal context submission loop. The default artifact is `target_journal_scorecard.md`; refresh it in place and preserve only compact score history inside the same file.
- Use `references/reference-adequacy-audit.md` when the task is near submission, asks what is missing before submission, targets a named journal, or requires package-level rewriting.
- Use `references/submission-cleanliness-audit.md` when the task is near submission, journal-targeted, package-oriented, or asks for an editor/reviewer-style check.
- Use `references/journal-structure-audit.md` when the task is near submission, journal-targeted, package-oriented, asks about headings/subheadings, or produces Word/PDF submission files with equations, figures or tables.
- Use `references/supplementary-information-audit.md` when the task creates, edits, checks, or cites Supplementary Information, Methods details, formulas, thresholds, validation/sensitivity tables, dataset provenance, or reviewer comments about missing supplementary material.
- Use `templates/reference_coverage_map.md` whenever reference adequacy is part of the deliverable or a gating check for submission-oriented work.
- Use `references/high-journal-expression.md` when the task is to make the prose more direct, natural, non-AI-sounding, and closer to high-level journal expression without changing the scientific position.
- Use `references/sentence-level-writing-audit.md` when the task is primarily about prose review, clutter reduction, passive voice, sentence architecture, terminology consistency, or numerical/citation consistency inside the writing itself.
- Use `references/prisma-systematic-review.md` for PRISMA-style systematic reviews (design, reporting structure, and task-packet handoffs).
- Use `references/figure-storytelling.md` when figures, captions, or visual claims must align with the main text and integrity checks matter.
- Use `templates/research_task_packet.md` for multi-stage tasks, broad bundles, or any handoff to a specialist route or subagent.
- Use `templates/campaign_checkpoint.md` when the user is continuing work across turns, phases, or review cycles.
- Use `templates/research_memory.md` when the output should preserve durable lessons, audit rules, or "do not repeat" patterns.
- Use `templates/research_session_log.md` for append-only session events when the work is long-running, multi-stage, or involves handoffs and recovery.
- Use `templates/direction_tournament.md` when the user presents 3 or more directions, framing options, or writing strategies.
- Use `templates/research_brief.md`, `templates/research_assessment.md`, `templates/claims_evidence_map.md`, and `templates/experiment_plan.md` for planning and assessment work.
- Use `templates/polish_pass.md` when the deliverable is a direct rewrite plus a compact list of the main editorial moves.
- Use `templates/writing_quality_review.md` when a full-pass, section-pass, or targeted sentence-level writing audit is the main deliverable.
- Use `templates/evidence_register.md` for compaction, overclaim review, and evidence-bound rewrites.
- Use `templates/claim_boundary_card.md`, `templates/credibility_validation_ladder.md`, `templates/story_spine.md`, `templates/figure_table_claim_gate.md`, `templates/reviewer_red_team_matrix.md`, and `templates/score_cap_card.md` as the reusable research credibility and story kernel templates.
- Use the writing templates in `templates/` for abstract audits, claim audits, journal-fit reports, polish passes, rebuttal strategy, review replies, and cover letters.

## Cross-platform packaging

This repository uses one canonical skill body and thin adapters:

- Codex metadata: `agents/openai.yaml`
- Codex notes: `platforms/codex/README.md`
- Claude Code notes and routing snippet: `platforms/claude-code/README.md`
- OpenClaw orchestration guidance: `platforms/openclaw/README.md`

The root `SKILL.md` is the source of truth. Platform adapters should stay thin and should not fork the skill logic.

Source README files and platform notes are allowed in this repository, but runtime installation/export should omit source-only documentation from the installed skill package.
