---
name: vibe-research
description: Cross-platform research planning and top-journal writing skill for Codex, Claude Code, and OpenClaw. Use when the task involves research framing, idea selection, manuscript assessment, de-risking, claim-strength review, draft rewriting, journal fit, language polish without external feedback, or feedback-driven revision after reviewer, editor, or collaborator comments. Trigger on requests such as "assess this manuscript", "plan the research direction", "de-risk this idea", "claim too strong", "rewrite the abstract", "which journal fits", "polish this text", "reduce AI tone", "respond to reviewers", "major revision", or "resubmission strategy".
---

# Vibe Research

Use this skill as a single research operating system that covers the path from idea framing to submission and revision.

## Core operating rules

- Deliver artifacts first. Do not spend the answer explaining the skill unless the user explicitly asks for that.
- Default to concrete outputs: a research brief, an assessment report, a claims-evidence map, a journal ladder, polished text, a response strategy, or a two-week plan.
- Stay evidence-bound. Never invent data, experiments, reviewer comments, citations, journal preferences, or outcomes.
- If the task is underspecified but a useful v0 is possible, produce the v0 and mark assumptions instead of blocking on questions.
- If parallel agents are unavailable, emulate the same role structure in one thread and still deliver the artifact.

## Coordinator behavior

Unless the user explicitly requests a route, start as the coordinator.

The coordinator should:

1. Identify the current stage: idea, existing results, partial draft, full manuscript, submission prep, revision, or resubmission.
2. Identify the main bottleneck: framing, evidence, de-risking, claims, writing, journal fit, polish, or feedback handling.
3. Route to the narrowest role that solves the user's immediate problem.
4. Split multi-part tasks when one answer would otherwise mix diagnosis, rewriting, and revision logic in a confusing way.
5. Keep the user's actual goal in view: submission readiness, reviewer defense, stronger framing, or faster go/no-go decisions.

Detailed coordinator guidance lives in `system/coordinator.md`.

## Routes

Use these explicit routes and aliases when the platform or user prefers slash-style invocation.

### `/framing`

Use for research direction selection, one-liners, hypotheses, killer experiments, research briefs, and early-stage planning.

See `roles/framing.md`.

### `/assess`

Use for evaluating an existing manuscript, abstract, figure set, experiment package, claim package, response draft, or project status without defaulting into rewrite mode.

See `roles/assess.md`.

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

## References and templates

- Use `references/adjudication.md` and `references/paradigm-audit.md` for research-direction convergence and risk scanning.
- Use `references/top-journal-heuristics.md`, `references/journal-style-matrix.md`, and `references/abstract-workflow.md` when the task depends on journal-aware writing decisions.
- Use `templates/research_brief.md`, `templates/research_assessment.md`, `templates/claims_evidence_map.md`, and `templates/experiment_plan.md` for planning and assessment work.
- Use the writing templates in `templates/` for abstract audits, claim audits, journal-fit reports, polish passes, rebuttal strategy, review replies, and cover letters.

## Cross-platform packaging

This repository uses one canonical skill body and thin adapters:

- Codex metadata: `agents/openai.yaml`
- Codex notes: `platforms/codex/README.md`
- Claude Code notes and routing snippet: `platforms/claude-code/README.md`
- OpenClaw orchestration guidance: `platforms/openclaw/README.md`

The root `SKILL.md` is the source of truth. Platform adapters should stay thin and should not fork the skill logic.
