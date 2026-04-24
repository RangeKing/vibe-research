# Harness Engineering Notes

Read this file when you are updating the coordinator, route orchestration, platform adapters, or the skill's own evaluation strategy.

This note treats Vibe Research as a managed harness rather than a long prompt. The goal is to keep interfaces stable even when route behavior, host platforms, or model strengths change.

## Navigation

- Core design rules
- Packet, checkpoint, memory, log
- Compaction, stale-harness checks, delegation, and security
- Regression harness and coordinator spot-check

## Core design rules

### 1. Do not adopt a pet harness

Avoid designs that depend on one irreplaceable prompt state, one giant answer, or one fragile thread that must never be interrupted.

In this skill:

- the coordinator is replaceable
- route hands are replaceable
- the current context window is replaceable
- durable artifacts are the source of recoverable state

If a run fails, the next run should be able to `wake` from artifacts instead of nursing a broken conversation back to health.

### 2. Keep the stable interface small

The stable harness contract is:

`doctor -> packetize -> execute -> verify -> distill -> checkpoint -> wake -> merge`

Everything else can evolve underneath that interface.

- `doctor` decides the task shape
- `packetize` creates the handoff envelope
- `execute` runs one narrow route or route sequence
- `verify` checks evidence and deliverable fit
- `distill` saves reusable lessons
- `checkpoint` preserves resumable state
- `wake` restores the current frontier from durable artifacts
- `merge` combines structured outputs from independent hands

If a proposed change adds detail but does not improve one of these operations, it is probably the wrong change.

### 3. Session lives outside the prompt

Do not treat the active context window as the system of record.

Durable session state should live in:

- `templates/research_task_packet.md`
- `templates/campaign_checkpoint.md`
- `templates/research_memory.md`
- `templates/research_session_log.md`

These artifacts are intentionally compact. They should be sufficient to resume work without replaying an entire transcript.

### 4. Decouple the brain from the hands

The coordinator is the brain. Route roles, templates, references, and optional subagents are hands.

Design implications:

- hands should receive a narrow packet
- hands should return a structured artifact
- hands should not invent shared state
- the coordinator owns final merge and user-facing synthesis

Do not bury control logic inside each role. Keep roles narrow and content-focused.

### 5. Failure isolation beats heroic recovery

Prefer designs where one bad handoff or one weak slice does not poison the whole run.

Use a small stable taxonomy:

- `context_overload`
- `route_collision`
- `evidence_gap`
- `feedback_fragmented`
- `journal_overreach`
- `rewrite_without_artifact`
- `campaign_drift`
- `merge_conflict`
- `handoff_blur`

Prefer one recovery attempt before asking the user for more material.

## Packet, checkpoint, memory, log

### Task packet

Use `templates/research_task_packet.md` when work needs a handoff envelope.

It should preserve:

- objective
- current frontier
- route
- session state
- explicit inputs
- evidence basis
- output contract
- acceptance checks
- stop conditions
- merge target when relevant

### Campaign checkpoint

Use `templates/campaign_checkpoint.md` when the next run must resume from the last trustworthy state.

It should preserve:

- last trustworthy state
- active frontier
- surviving and killed paths
- evidence gaps
- blocked-on items
- next wake instruction

### Research memory

Use `templates/research_memory.md` for durable rules rather than transient status.

Good contents:

- reusable heuristics
- decision rules
- killed patterns
- review or writing constraints
- do-not-repeat items

Bad contents:

- speculative claims
- raw transcript residue
- secrets or login details
- unverified web assertions

### Session log

Use `templates/research_session_log.md` for append-only event history on long or multi-hand runs.

It should record:

- key events
- handoffs
- failures
- recoveries
- state transitions

It should not become a second transcript.

## Compaction as a first-class tool

If the context is too long, fragmented, or repetitive, compact before continuing.

Preferred compaction objects:

- `templates/evidence_register.md` for claim-heavy material
- `templates/research_task_packet.md` for workflow-heavy material
- `templates/research_assessment.md` for project-status triage

Compaction should preserve:

- what is known
- what is missing
- what is risky
- what should happen next

## Stale-harness check

Harness assumptions go stale as model behavior improves.

When maintaining this skill, ask:

- Is this instruction a stable contract or just a workaround for an old model behavior?
- Can this behavior move from prose into a template or artifact field?
- Are we forcing packetization, checkpointing, or delegation where a direct answer is now safer?
- Are we preserving state in too many places?

Delete dead harness weight aggressively.

## Delegation and merge policy

Delegate only when all of the following are true:

- the subproblem is independent
- ownership is clear
- inputs can be packetized
- outputs can be merged by structure

Good delegation examples:

- compare several research directions independently
- audit figure-story alignment separately from journal fit
- rewrite two isolated sections with shared constraints

Bad delegation examples:

- co-writing one tightly coupled discussion section
- splitting unresolved evidence interpretation
- parallelizing a task just because the user provided many files

Merge only from structured artifacts. If merge requires reconstructing hidden reasoning from chat history, rerun through a cleaner packet.

## Security and credential boundary

This skill is allowed to reason about external verification, but durable artifacts must never become credential stores.

Never write into packets, checkpoints, memory, or session logs:

- tokens
- login state
- vault values
- private URLs that function as credentials

External findings should remain marked as unverified until actually checked.

## Regression harness for this skill

When maintaining the skill, validate behavior with representative prompts rather than only reading the docs.

### Existing regression set

1. Pure assessment
Prompt shape: "Assess this abstract and tell me the highest-leverage fix before submission."
Expected behavior: routes to `assess`, does not silently rewrite the whole abstract.

2. Overclaim disguised as polish
Prompt shape: "Polish this abstract for Nature-level tone."
Expected behavior: if claims are too strong, surfaces `claim` logic before or alongside polish.

3. Feedback-driven rewrite
Prompt shape: "Here are reviewer comments and my current response draft."
Expected behavior: routes to `revise`, preserves comment-to-action logic, does not treat it as ordinary polish.

4. Early-stage idea de-risking
Prompt shape: "Is this project worth doing, and what is the fastest falsifier?"
Expected behavior: routes to `framing` or `de-risk`, outputs a go/no-go style artifact.

5. Context overload
Prompt shape: a long, messy bundle of notes plus draft plus reviewer comments.
Expected behavior: compact first, split the problem, and deliver the highest-leverage slice instead of an omnibus answer.

6. Journal overreach
Prompt shape: "Can this go to Nature?" with only partial evidence.
Expected behavior: separates current tier fit from aspirational positioning and does not promise acceptance.

7. PRISMA systematic review framing
Prompt shape: "I need a PRISMA-style systematic review Methods and Results skeleton; here is my review question and databases."
Expected behavior: task packet when useful, then `framing` -> `draft` with `references/prisma-systematic-review.md`, and `assess` for checklist completeness.

8. Figures vs conclusions
Prompt shape: "Reviewers say my figures do not support the conclusions—what should I fix?"
Expected behavior: `assess` using `references/figure-storytelling.md`; escalate to `claim` or `draft`/`revise` depending on whether the issue is evidence, wording, or response to comments.

9. Campaign continuation
Prompt shape: "Continue this project from the checkpoint below."
Expected behavior: recover the frontier from prior state, execute one narrow step, then emit an updated checkpoint instead of restarting from scratch.

10. Direction tournament
Prompt shape: "Compare these four project directions and tell me which one to back."
Expected behavior: use `templates/direction_tournament.md`, keep one winner, up to two backups, and an explicit graveyard with reasons.

11. Failure graveyard reuse
Prompt shape: "Summarize what we learned from these failed experiments and what we should stop repeating."
Expected behavior: distill reusable lessons into `templates/research_memory.md`, including a `Do Not Repeat` section.

12. Draft -> verify -> distill
Prompt shape: "Rewrite this results section and tell me what writing rules we should keep for the rest of the paper."
Expected behavior: draft, verify against evidence, and preserve reusable writing constraints in memory or a checkpoint.

### Managed-harness additions

13. Wake from checkpoint only
Prompt shape: "Continue from this checkpoint; I do not have the original notes here."
Expected behavior: `wake` from the checkpoint, recover the frontier, and continue without demanding the full original transcript.

14. Short task should stay short
Prompt shape: "Polish these three sentences without changing the claims."
Expected behavior: route directly to `polish`; do not force campaign/session machinery.

15. Two independent hands
Prompt shape: "Compare these two project directions and separately audit whether the abstract overclaims."
Expected behavior: split into independent structured outputs only if they remain mergeable by packet and artifact.

16. Partial failure isolation
Prompt shape: a mixed task where one requested slice lacks evidence.
Expected behavior: preserve the successful slice, downgrade the weak slice, and write the gap into checkpoint or memory instead of failing the whole response.

17. External verification boundary
Prompt shape: "Check this journal policy and preserve what matters for later."
Expected behavior: keep unverified claims labeled until checked and never distill credentials or hidden session state.

## Coordinator regression spot-check

Use this as a manual pass when changing the coordinator, routing, or skill scope: for each prompt shape above, confirm `system/coordinator.md`, `system/routing.md`, and `system/guardrails.md` still imply the expected route, recovery, and artifact behavior.

**Spot-check (2026-04-09):** Prompts 1-17 should be checked against the current coordinator, routing, route files, and reference/template pointers after each substantial skill update. Run `scripts/quick_validate.py` for structure checks, then use this table for manual regression.
