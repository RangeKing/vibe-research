---
name: vibe-research
description: Cross-platform evolving research harness and manuscript-oriented writing skill for Codex, Claude Code, and OpenClaw. Use when the task involves research framing, idea selection, campaign continuation, comparing several directions, manuscript assessment, de-risking, claim-strength review, draft rewriting, journal fit, figure-to-claim alignment, systematic review or PRISMA-style planning/reporting, or summarizing lessons from failed experiments, review cycles, or revisions. Trigger on requests such as "assess this manuscript", "continue this project", "compare these research directions", "plan the research direction", "de-risk this idea", "claim too strong", "rewrite the abstract", "which journal fits", "check whether figures support the conclusions", "draft a PRISMA Methods section", "summarize what we learned from these failed experiments", "respond to reviewers", "major revision", or "resubmission strategy".
---

# Vibe Research

Use this skill as an evolving research harness that covers the path from idea framing to submission and revision.

Treat the skill as two layers:

- The coordinator is the control plane: preflight, route selection, scope control, compaction, campaign stewardship, recovery, and final synthesis.
- The route roles are the execution plane: framing, assessment, claim review, drafting, journal fit, polish, and revision.

## Core operating rules

- Deliver artifacts first. Do not spend the answer explaining the skill unless the user explicitly asks for that.
- Default to concrete outputs: a research brief, an assessment report, a claims-evidence map, a journal ladder, polished text, a response strategy, or a two-week plan.
- Stay evidence-bound. Never invent data, experiments, reviewer comments, citations, journal preferences, or outcomes.
- Run a short preflight before substantial work: identify stage, artifact type, bottleneck, evidence basis, route, requested deliverable, and context risk.
- For long-horizon work, switch into campaign mode: read prior checkpoints or memory artifacts, recover the current frontier, and continue from the latest trustworthy checkpoint.
- If the task is underspecified but a useful v0 is possible, produce the v0 and mark assumptions instead of blocking on questions.
- If the task spans multiple routes or arrives as a messy bundle, create a compact task packet before deep execution.
- Compact context before escalating. Convert long or fragmented input into an evidence register, action table, or narrow packet instead of asking the user to resend everything.
- Verify before distilling. Only carry forward lessons that are grounded in user-provided evidence, transparent reasoning, or explicitly labeled heuristics.
- Distill reusable memory for substantial work. Preserve what changed, what was ruled out, what should be reused later, and the next checkpoint.
- Prefer recovery recipes over generic blocking questions. When possible, salvage the task by softening claims, narrowing scope, splitting steps, or switching the output contract.
- Treat partial success as first-class. If a full manuscript pass is not justified, still deliver the smallest artifact that improves the user's decision quality.
- If parallel agents are unavailable, emulate the same role structure in one thread and still deliver the artifact.
- Match the user's output language by default. If the request is in English, keep headings, rationale, and summary lines in English unless the user asks for another language.
- Do not surface workspace or tooling context in user-facing output unless the user explicitly asks about files, logs, or the execution environment.

## Coordinator behavior

Unless the user explicitly requests a route, start as the coordinator.

The coordinator should:

1. Identify the current stage: idea, existing results, partial draft, full manuscript, submission prep, revision, or resubmission.
2. Identify the main bottleneck: framing, evidence, de-risking, claims, writing, journal fit, polish, or feedback handling.
3. Decide whether the task is normal mode or campaign mode.
4. Route to the narrowest role that solves the user's immediate problem.
5. Split multi-part tasks when one answer would otherwise mix diagnosis, rewriting, and revision logic in a confusing way.
6. Keep the user's actual goal in view: submission readiness, reviewer defense, stronger framing, or faster go/no-go decisions.

Detailed coordinator guidance lives in `system/coordinator.md`.

## Harness lifecycle

Run the work in this order unless the user clearly overrides it:

1. `doctor` preflight: classify the task, spot route collisions, and detect evidence/context risks.
2. Task packet: define objective, scope, evidence basis, route, deliverable, acceptance bar, fallback artifact, and campaign state when relevant.
3. Route execution: hand the task to the narrowest role or a small ordered sequence of roles.
4. Verification: check that the output stayed evidence-bound, solved the stated bottleneck, and matched the requested deliverable.
5. Distillation: when the task is substantial, capture reusable lessons in a memory or checkpoint artifact.
6. Compact or resume: if the task is too broad, preserve a compact state and continue on the highest-leverage slice instead of resetting.
7. Closeout: end with the next move, especially when the artifact is diagnostic rather than final-copy ready.

The `doctor` pass is an internal control step, not a user-facing heading requirement. It should quickly classify:

- stage
- core artifact
- main bottleneck
- evidence quality
- best route
- requested output contract
- mode: `normal` or `campaign`
- failure risks such as `context_overload`, `route_collision`, `evidence_gap`, `feedback_fragmented`, or `journal_overreach`

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

## Recovery rules

When the task becomes tangled, recover with the smallest reliable move:

- `context_overload`: compact into `templates/evidence_register.md`, then assess or claim-review the highest-risk slice first.
- `route_collision`: split explicitly, usually `assess -> claim -> draft` or `journal -> draft/polish`.
- `evidence_gap`: preserve the structure, soften conclusions, and label placeholders instead of fabricating support.
- `feedback_fragmented`: normalize comments into an action table before entering `revise`.
- `journal_overreach`: judge the current evidence tier first, then discuss the stretch target separately.
- `rewrite_without_artifact`: provide a scaffold, outline, or example paragraph instead of pretending to revise unseen text.

Prefer one recovery attempt before asking the user for more material.

## Validation contract

Before finalizing, check these invariants:

- the route matches the real bottleneck
- all strong claims are tied to user-provided evidence or clearly labeled heuristics
- the deliverable is concrete and immediately usable
- incomplete inputs are reflected as assumptions, not hidden inside confident prose
- reused memory is distilled, not copied forward as raw transcript residue
- the output ends with a next move when the task is not fully closed

## References and templates

- Use `references/harness-engineering.md` when updating the coordinator, platform adapters, or evaluation strategy for this skill.
- Use `references/evolution-loop.md` when the task spans multiple iterations, needs a checkpoint, or should distill reusable research memory instead of only solving the immediate prompt.
- Use `references/adjudication.md` and `references/paradigm-audit.md` for research-direction convergence and risk scanning.
- Use `references/manuscript-heuristics.md`, `references/journal-style-matrix.md`, and `references/abstract-workflow.md` when the task depends on journal-aware or high-standard manuscript writing decisions.
- Use `references/prisma-systematic-review.md` for PRISMA-style systematic reviews (design, reporting structure, and task-packet handoffs).
- Use `references/figure-storytelling.md` when figures, captions, or visual claims must align with the main text and integrity checks matter.
- Use `templates/research_task_packet.md` for multi-stage tasks, broad bundles, or any handoff to a specialist route or subagent.
- Use `templates/campaign_checkpoint.md` when the user is continuing work across turns, phases, or review cycles.
- Use `templates/research_memory.md` when the output should preserve durable lessons, audit rules, or "do not repeat" patterns.
- Use `templates/direction_tournament.md` when the user presents 3 or more directions, framing options, or writing strategies.
- Use `templates/research_brief.md`, `templates/research_assessment.md`, `templates/claims_evidence_map.md`, and `templates/experiment_plan.md` for planning and assessment work.
- Use `templates/evidence_register.md` for compaction, overclaim review, and evidence-bound rewrites.
- Use the writing templates in `templates/` for abstract audits, claim audits, journal-fit reports, polish passes, rebuttal strategy, review replies, and cover letters.

## Cross-platform packaging

This repository uses one canonical skill body and thin adapters:

- Codex metadata: `agents/openai.yaml`
- Codex notes: `platforms/codex/README.md`
- Claude Code notes and routing snippet: `platforms/claude-code/README.md`
- OpenClaw orchestration guidance: `platforms/openclaw/README.md`

The root `SKILL.md` is the source of truth. Platform adapters should stay thin and should not fork the skill logic.
