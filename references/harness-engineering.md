# Harness Engineering Notes

Read this file when you are updating the coordinator, route orchestration, platform adapters, or the skill's own evaluation strategy.

This skill borrows from coding-harness thinking: make control flow explicit, machine-checkable where possible, and recoverable without starting over.

It also borrows selectively from EvoScientist: scientific workflow staging, verified distillation, and lightweight evolving memory artifacts without importing a heavyweight runtime.

## What to borrow

### 1. Preflight before execution

Before deep work, run a short internal `doctor` pass:

- what stage is the project in?
- what artifact is actually present?
- what is the main bottleneck?
- which route should own the task?
- what is the concrete output contract?
- what is the main failure risk?

If this is skipped, the skill tends to mix diagnosis, rewriting, and revision into one muddy answer.

### 2. Control plane vs execution plane

- Control plane: coordinator, routing, compaction, recovery, verification, final synthesis
- Execution plane: the route roles and templates

Do not bury control logic inside each role. Keep roles narrow and content-focused.

### 3. Structured task packets

Broad tasks should not rely on one long natural-language blob.

Use `templates/research_task_packet.md` to preserve:

- objective
- scope
- route
- evidence basis
- deliverable
- acceptance checks
- fallback artifact
- campaign state when relevant

This makes multi-step work easier to split, resume, or hand off.

### 4. Compaction as a first-class tool

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

### 5. Failure taxonomy

Use a small stable taxonomy so recovery is consistent:

- `context_overload`
- `route_collision`
- `evidence_gap`
- `feedback_fragmented`
- `journal_overreach`
- `rewrite_without_artifact`

Prefer one recovery attempt before asking the user for more material.

### 6. Actionable summary compression

Long work should collapse into four control signals:

- current phase
- last trustworthy checkpoint
- current blocker
- recommended next move

This keeps status updates useful without leaking orchestration theory into user-facing prose.

### 7. Verify, then distill

Do not turn raw conversation residue into memory.

For long-horizon work:

- verify what actually survived evidence checks
- distill only reusable lessons
- preserve the next checkpoint so the work can continue cleanly later

### 8. Candidate evolution without runtime complexity

When several plausible directions exist, compare them explicitly instead of free-associating toward a winner.

Use:

- `templates/direction_tournament.md` to rank candidates
- `templates/campaign_checkpoint.md` to preserve survivors and killed paths
- `templates/research_memory.md` to keep durable lessons

## Regression harness for this skill

When maintaining the skill, validate behavior with representative prompts rather than only reading the docs.

Suggested regression set:

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
Expected behavior: task packet when useful, then `framing` → `draft` with `references/prisma-systematic-review.md`, and `assess` for checklist completeness.

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

## Coordinator regression spot-check

Use this as a **manual** pass when changing the coordinator, routing, or skill scope: for each prompt shape above, confirm `system/coordinator.md`, `system/routing.md`, and `system/guardrails.md` still imply the expected route and recovery.

**Spot-check (2026-04-07):** Prompts 1–12 should be checked against the current coordinator, routing, route files, and reference/template pointers after each substantial skill update. Automated `quick_validate.py` is not present in this repo—use this table for manual regression.

## Maintenance rule

If a proposed skill update adds more prose but does not improve preflight, compaction, routing, recovery, or validation, it is probably the wrong update.
