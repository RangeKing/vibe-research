---
name: vibe-research
description: Managed research and manuscript skill for assessing drafts, continuing from checkpoints, comparing directions, de-risking ideas, rewriting abstracts or sections, choosing journals, checking figure-claim alignment, planning PRISMA-style reviews, handling reviewer feedback or resubmission, and polishing prose toward direct, high-level journal expression. Also triggers on Chinese requests such as "评估这篇稿子", "继续这个项目", "重写摘要", "润色这段文字", "清理赘词", "改掉被动语态", "检查术语是否一致", "推荐投稿期刊", and "回复审稿意见".
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
- Run a short preflight before substantial work: identify stage, artifact type, bottleneck, evidence basis, route, requested deliverable, context risk, and reference state.
- Preserve source-to-deliverable traceability. For broad, continuation, reviewer-driven, or submission-facing work, track which user requirements, reviewer comments, journal constraints, figure claims, and SI pointers must survive into the delivered artifact.
- Investigate root cause before fixing symptoms. When a reviewer, editor, collaborator, failed experiment, or figure mismatch exposes a problem, identify whether the real issue is evidence, claim strength, framing, method detail, citation coverage, or prose before drafting a fix.
- Treat external feedback as material to evaluate, not orders to obey. Verify each comment against the manuscript, data, journal rules, and prior decisions before accepting, revising, deferring, or pushing back.
- For journal-targeted, near-submission, or submission-package work, run a reference-adequacy audit before deep rewriting: citation count, coverage by claim type, unsupported factual statements, citation density, and numbering/format risks.
- For journal-targeted, near-submission, or submission-package work, run final readiness audits before delivery: check submission cleanliness by removing internal paths, filenames, code variables, tool/script names, lab-notebook phrasing, and project-management residue from editor/reviewer-facing text; check journal structure by verifying target-journal section rules, heading/subheading style, Discussion heading policy, and formal equation/table/figure formatting. Treat internal-trace leakage and structure/display-format drift as submission blockers, not cosmetic issues.
- For journal-targeted, near-submission, or submission-package work that creates, edits, or cites Supplementary Information, run a supplementary-information adequacy audit before delivery. Every main-text pointer to a supplementary note, table, figure, formula, threshold, dataset, sensitivity analysis, or validation result must resolve to actual supplementary content with matching terminology, numbering, variables, and formal equation/table formatting. Treat missing or thinned-out SI content as a submission blocker.
- For journal-targeted or submission-package work with figures, audit whether figure panels, legends, source-data tables, methods equations, and headline numbers use the same accounting basis. Treat figure-accounting drift as a submission blocker, not a cosmetic issue.
- When the reference state is `thin` or `uneven`, produce a reference coverage map and insertion plan before venue-specific drafting or polish.
- Coverage is not density. In journal-facing prose, prefer the fewest citations needed to anchor a claim, avoid long citation stacks, and move completeness-oriented support into Methods, SI, or a reference coverage artifact when possible.
- Recover before restarting. For long-horizon work, read the latest trustworthy checkpoint, task packet, memory note, or session log before taking a new step.
- If the task is underspecified but a useful v0 is possible, produce the v0 and mark assumptions instead of blocking on questions.
- If the task spans multiple routes or arrives as a messy bundle, create a compact task packet before deep execution.
- Compact context before escalating. Convert long or fragmented input into an evidence register, action table, or narrow packet instead of asking the user to resend everything.
- Watch context budget as a quality signal. When the source bundle is large, prefer frontmatter, summaries, evidence registers, and packets over rereading full drafts; checkpoint before the answer becomes vague or starts dropping constraints.
- Watch for rationalization pressure. Deadlines, sunk-cost drafts, reviewer anxiety, target-journal ambition, or "just polish it" phrasing are signals to run stricter evidence and coverage checks, not shortcuts.
- Verify before distilling. Only carry forward lessons that are grounded in user-provided evidence, transparent reasoning, or explicitly labeled heuristics.
- Do not claim readiness, completeness, or successful revision without fresh verification against the relevant packet, source artifact, or audit checklist.
- Distill reusable memory for substantial work. Preserve what changed, what was ruled out, what should be reused later, and the next checkpoint.
- Keep the harness stable even if route behavior evolves. Prefer stable interfaces and artifacts over brittle prompt tricks.
- Prefer recovery recipes over generic blocking questions. When possible, salvage the task by softening claims, narrowing scope, splitting steps, or switching the output contract.
- Treat partial success as first-class. If a full manuscript pass is not justified, still deliver the smallest artifact that improves the user's decision quality.
- If parallel agents are unavailable, emulate the same role structure in one thread and still deliver the artifact.
- Parallelize only across independent hands. If subproblems share evidence interpretation or need joint prose generation, keep them in one handoff.
- Match the user's output language by default. If the request is in English, keep headings, rationale, and summary lines in English unless the user asks for another language.
- Do not surface workspace or tooling context in user-facing output unless the user explicitly asks about files, logs, or the execution environment.

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
- failure risks such as `context_overload`, `budget_pressure`, `route_collision`, `evidence_gap`, `symptom_fix`, `source_coverage_gap`, `feedback_fragmented`, `reviewer_overcompliance`, `journal_overreach`, `citation_thin`, `coverage_uneven`, `citation_dense`, `supplement_drift`, `internal_trace_leak`, `heading_style_drift`, `equation_format_drift`, `campaign_drift`, `checkpoint_stale`, or `merge_conflict`

Use `templates/research_task_packet.md` when the work needs a compact control object.

Campaign mode is appropriate when the user is continuing a research thread, comparing several directions, revisiting failed iterations, or providing prior checkpoint or memory artifacts.

## Routes

Use these explicit routes and aliases when the platform or user prefers slash-style invocation.

### `/framing`

Use for research direction selection, one-liners, hypotheses, killer experiments, research briefs, and early-stage planning.

See `roles/framing.md`.

### `/assess`

Use for evaluating an existing manuscript, abstract, figure set, experiment package, claim package, response draft, or project status without defaulting into rewrite mode.

See `roles/assess.md`. For figure–text alignment and PRISMA reporting checks, load `references/figure-storytelling.md` and `references/prisma-systematic-review.md` when relevant.
For near-submission or journal-targeted assessments, also load `references/reference-adequacy-audit.md`, `references/submission-cleanliness-audit.md`, `references/journal-structure-audit.md`, and `references/supplementary-information-audit.md`.

### `/de-risk`

Use for falsifiers, negative controls, paradigm audits, reviewer-risk scans, kill criteria, and the smallest experiments needed to disprove or rescue an idea.

See `roles/de-risk.md`.

### `/claim`

Use for claim strength, mechanism wording, causality boundaries, generality, limitations, robustness, and safer wording.

See `roles/claim.md`.

### `/draft`

Use for drafting or rewriting titles, abstracts, introductions, results, discussions, conclusions, captions, and story arcs.

See `roles/draft.md`.

### `/journal`

Use for journal fit, target venue selection, audience fit, journal ladder design, and pre-submission positioning.

See `roles/journal.md`.
For selective-journal targeting or package retargeting, also load `references/reference-adequacy-audit.md`, `references/submission-cleanliness-audit.md`, `references/journal-structure-audit.md`, and `references/supplementary-information-audit.md`.

### `/polish`

Use for no-feedback refinement only: language polish, AI-tone reduction, flow tightening, style cleanup, term consistency, and submission-ready cleanup when there are no reviewer or editor comments driving the change.

See `roles/polish.md`.

### `/revise`

Use only for feedback-driven modification: reviewer comments, editor decisions, collaborator feedback, rebuttals, response letters, major revision, and resubmission strategy.

See `roles/revise.md`.

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
- `symptom_fix`: stop drafting and trace the problem backward to its source: missing evidence, overclaim, weak method, bad figure accounting, citation gap, or unclear prose.
- `source_coverage_gap`: map required source items to output sections before rewriting; do not finalize until required reviewer comments, claim constraints, figure/SI pointers, or journal rules are either covered or explicitly deferred.
- `feedback_fragmented`: normalize comments into an action table before entering `revise`.
- `reviewer_overcompliance`: verify whether the requested change is scientifically correct, journal-appropriate, and compatible with prior decisions before implementing; push back or narrow the response when the comment is wrong or overreaching.
- `journal_overreach`: judge the current evidence tier first, then discuss the stretch target separately.
- `citation_thin`: build a reference coverage map and insertion plan before doing more journal-specific polish.
- `figure_accounting_drift`: reconcile the statistical basis across figure panels, captions, source data, methods, and headline text before styling or journal retargeting.
- `coverage_uneven`: identify the unsupported claim buckets, insert the missing literature, and only then resume manuscript-level rewriting.
- `citation_dense`: reduce redundant citation stacks, keep anchor citations in main-text claims, and migrate completeness citations to Methods, SI, or a coverage map.
- `supplement_drift`: inventory every main-text SI pointer, compare it with the current SI and any prior detailed SI/checkpoint, restore missing provenance tables, formulas, coefficient/threshold tables, sensitivity/validation tables, variable definitions, and cross-references before polishing prose.
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
- Use the writing templates in `templates/` for abstract audits, claim audits, journal-fit reports, polish passes, rebuttal strategy, review replies, and cover letters.

## Cross-platform packaging

This repository uses one canonical skill body and thin adapters:

- Codex metadata: `agents/openai.yaml`
- Codex notes: `platforms/codex/README.md`
- Claude Code notes and routing snippet: `platforms/claude-code/README.md`
- OpenClaw orchestration guidance: `platforms/openclaw/README.md`

The root `SKILL.md` is the source of truth. Platform adapters should stay thin and should not fork the skill logic.

Source README files and platform notes are allowed in this repository, but runtime installation/export should omit source-only documentation from the installed skill package.
