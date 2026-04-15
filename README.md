# Vibe Research

[中文说明](./README_CN.md)

Vibe Research is a cross-platform managed research harness and manuscript-writing skill for Codex, Claude Code, and OpenClaw.

It is designed for work that sits between scientific judgment and writing execution: idea framing, project assessment, de-risking, claim calibration, journal fit, drafting, polish, and feedback-driven revision.

## What This Repository Is

This repository is not a paper template and not a general writing prompt pack.

It is a structured research harness with:

- a coordinator brain that acts as the control plane
- a harness layer for recovery, packetization, delegation, and merge
- reusable durable session artifacts
- specialist routes for narrow research-writing tasks
- references for domain-specific judgment
- templates for concrete deliverables
- thin platform adapters for Codex, Claude Code, and OpenClaw

The root [SKILL.md](./SKILL.md) is the source of truth.

## Scope: what “full pipeline” means here

In this repository, **full pipeline** means the **manuscript and decision chain** from research framing through **major revision and resubmission**, consistent with the coordinator and eight routes. It also explicitly includes:

- **Systematic reviews (PRISMA)**: workflow, reporting structure, and synthesis-oriented writing and decisions—not building automated search engines or crawlers.
- **Figure storytelling**: aligning figures and captions with the main claims, primary messages, and common integrity checks—not software-specific plotting tutorials.
- **Persistent memory in a lightweight sense**: reusable conversation artifacts and templates, not a storage engine or background runtime.

**Out of scope** (stated briefly so expectations stay clear): wet-lab experimental SOPs; end-to-end raw-data statistics pipelines; automated database or literature crawling; real-time journal policy verification; and full grant proposals as a primary deliverable.

## What The Skill Helps With

Use this skill when you need help with tasks such as:

- selecting or reframing a research direction
- deciding whether an idea is worth pursuing
- assessing manuscript readiness
- identifying the highest-risk evidence gap
- softening overclaim or causality overreach
- rewriting titles, abstracts, introductions, results, or discussions
- choosing a target journal or building a journal ladder
- polishing text without changing the scientific position
- making prose sound more like a strong journal manuscript and less like AI output
- responding to reviewer, editor, or collaborator feedback
- continuing a research campaign from a prior checkpoint
- comparing several directions and preserving what was ruled out
- summarizing lessons from failed experiments or review cycles

## Core Design

The skill uses a four-part managed-harness model:

- Brain: coordinator judgment, routing, verification, and final synthesis
- Harness: preflight, packetization, compaction, delegation, wake, and merge
- Hands: route-specific task handling such as `assess`, `claim`, `draft`, or `revise`
- Session: durable artifacts that outlive the current context window

This design helps the skill avoid a common failure mode in research assistance: mixing diagnosis, rewriting, journal fit, rebuttal logic, and campaign state into one vague answer.

## Routes

The main routes are:

- `/framing`: research direction, one-liners, hypotheses, killer experiments, research briefs
- `/assess`: manuscript or project-state evaluation without defaulting into rewrite mode
- `/de-risk`: falsifiers, negative controls, kill criteria, reviewer-risk scans
- `/claim`: claim strength, causality boundaries, mechanism wording, limitations
- `/draft`: drafting and rewriting scientific text
- `/journal`: journal fit, audience fit, and submission positioning
- `/polish`: style cleanup without external feedback
- `/revise`: feedback-driven revision and response strategy

See the route files in [roles/](./roles/) for the narrow behavior of each role.

## Harness Behavior

By default, the coordinator follows this lifecycle:

1. Internal preflight (`doctor`)
2. `wake` from durable artifacts when continuation state exists
3. Task packet creation when needed
4. Route execution
5. Verification against evidence and deliverable
6. Distillation into reusable memory artifacts when useful
7. Checkpointing for resumable state
8. Merge only when multiple independent hands contributed
9. Closeout with the next best move

This is especially useful for messy real-world inputs such as:

- a long bundle of draft text plus reviewer comments
- a project summary with partial evidence
- a request that mixes journal fit, rewriting, and claim review
- a project that needs to continue from prior memory instead of restarting

## Evidence And Integrity Rules

This skill is intentionally evidence-bound.

It should not:

- invent data, experiments, references, reviewer comments, or journal decisions
- present speculative wording as proven fact
- pretend to have revised material that was never provided
- promise that a manuscript can publish in a specific journal without support

Guardrails live in [system/guardrails.md](./system/guardrails.md).

## Repository Layout

```text
.
├── SKILL.md                      # Canonical skill definition
├── agents/openai.yaml            # Codex-facing UI metadata
├── system/                       # Coordinator, routing, and guardrails
├── roles/                        # Narrow specialist routes
├── references/                   # Load-on-demand judgment aids
├── templates/                    # Deliverable templates and compaction objects
└── platforms/                    # Thin adapters for each host environment
```

Key files:

- [SKILL.md](./SKILL.md): main workflow and routing contract
- [system/coordinator.md](./system/coordinator.md): control-plane behavior
- [system/routing.md](./system/routing.md): route selection rules
- [system/guardrails.md](./system/guardrails.md): academic-integrity boundaries
- [references/harness-engineering.md](./references/harness-engineering.md): maintenance notes for evolving the skill itself
- [references/managed-harness-patterns.md](./references/managed-harness-patterns.md): managed-agent design principles mapped into this skill
- [references/evolution-loop.md](./references/evolution-loop.md): EvoScientist-inspired campaign logic and lightweight memory philosophy
- [references/prisma-systematic-review.md](./references/prisma-systematic-review.md): PRISMA-oriented systematic review structure and task-packet use
- [references/figure-storytelling.md](./references/figure-storytelling.md): figures, captions, and claim alignment
- [references/high-journal-expression.md](./references/high-journal-expression.md): direct, non-AI-sounding journal expression rules for polish work
- [templates/research_task_packet.md](./templates/research_task_packet.md): compact control object for broad or multi-stage work
- [templates/campaign_checkpoint.md](./templates/campaign_checkpoint.md): resumable state for long-horizon work
- [templates/research_memory.md](./templates/research_memory.md): distilled reusable lessons
- [templates/research_session_log.md](./templates/research_session_log.md): append-only session state for long or multi-hand runs
- [templates/direction_tournament.md](./templates/direction_tournament.md): ranked comparison of competing options
- [templates/polish_pass.md](./templates/polish_pass.md): compact rewrite-oriented polish deliverable
- [templates/writing_quality_review.md](./templates/writing_quality_review.md): structured writing-quality audit

## Platform Adapters

This repository keeps one canonical logic layer and thin platform-specific adapters:

- [platforms/codex/README.md](./platforms/codex/README.md)
- [platforms/claude-code/README.md](./platforms/claude-code/README.md)
- [platforms/openclaw/README.md](./platforms/openclaw/README.md)

The adapters should stay thin. If a change affects the reasoning workflow, update [SKILL.md](./SKILL.md) first.

## Example Usage

### Codex

```text
$vibe-research /assess this manuscript status
$vibe-research continue this project from this checkpoint
$vibe-research /polish this abstract without changing the claims
$vibe-research /revise these reviewer comments
$vibe-research 评估这篇稿子当前最关键的问题
$vibe-research 从这个 checkpoint 继续，并找出下一步
$vibe-research 回复这些审稿意见，并给出修改策略
```

### Claude Code

```text
/assess evaluate this abstract and tell me what is missing before submission
/claim this discussion overstates causality; rewrite it safely
/revise turn these reviewer comments into a response strategy
```

### OpenClaw

Typical pattern:

- coordinator thread owns synthesis
- specialist routes are spawned only when they reduce ambiguity
- broad tasks are compacted before parallelization

## How To Maintain This Skill

When updating the skill:

1. Treat [SKILL.md](./SKILL.md) as the source of truth.
2. Keep role files narrow and content-focused.
3. Move detailed maintenance notes into [references/](./references/) instead of bloating the root skill.
4. Add or reuse templates when the same control object or deliverable keeps recurring.
5. Keep platform adapters synchronized, but thin.

The repository now includes a lightweight harness-maintenance note in [references/harness-engineering.md](./references/harness-engineering.md), including suggested regression prompt shapes for future iteration.
It also includes [references/managed-harness-patterns.md](./references/managed-harness-patterns.md) as the shortest interface-level summary of the managed-harness design.
Use [scripts/quick_validate.py](./scripts/quick_validate.py) for repo-local structure checks after substantial edits.

## Who This Is For

This skill is a good fit for:

- researchers exploring or rescuing a project direction
- authors aiming to raise manuscript quality and venue fit for selective journals
- teams handling rebuttals, major revision, or resubmission
- AI-skill builders who want a research-oriented harness rather than a flat prompt

It is not intended to replace real scientific evidence, peer review, or journal-specific policy verification.
