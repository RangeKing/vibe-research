# Routing

Route based on the user's immediate problem, not the full lifecycle of the paper.

No new slash route is needed for session, recovery, or memory work. Handle that through the coordinator, the stable control operations, and durable artifacts.

## Navigation

- Stable control interface
- Route table
- PRISMA and campaign routing
- Many-hands, merge, and conflict rules

## Stable control interface

The harness should be expressible as:

`doctor -> packetize -> execute -> verify -> distill -> checkpoint -> wake -> merge`

These are not slash commands. They are the stable orchestration interface around the existing routes.

## Route table

### `framing`

Use when the user needs:

- research ideation
- one-liner design
- research brief creation
- killer experiments
- hypotheses and falsifiers
- a two-week go/no-go plan
- comparison among 3 or more candidate directions or storylines

Aliases:

- `/framing`
- `/idea`
- `/research-brief`
- `/plan`

### `assess`

Use when the user needs:

- a current-state evaluation of a manuscript or project
- readiness judgment
- strengths and weaknesses analysis
- figure-set or evidence-package review
- "what is missing before submission?"

Aliases:

- `/assess`
- `/evaluate`
- `/status`
- `/audit`

### `de-risk`

Use when the user needs:

- paradigm audit
- reviewer-risk scan
- minimal falsifiers
- kill criteria
- negative controls
- "how can this fail fast?"

Aliases:

- `/de-risk`
- `/derisk`
- `/risk`
- `/falsify`

### `claim`

Use when the user needs:

- claim-strength review
- safer wording
- mechanism or causality boundaries
- limitation framing
- robustness or generality review

Aliases:

- `/claim`
- `/logic`
- `/mechanism`
- `/soften`

### `draft`

Use when the user needs:

- title, abstract, introduction, results, discussion, or conclusion drafting
- storyline reconstruction
- English rewriting from bullets, Chinese notes, or rough draft text

Aliases:

- `/draft`
- `/story`
- `/rewrite`
- `/abstract`

### `journal`

Use when the user needs:

- target journal selection
- journal ladder design
- audience fit analysis
- submission positioning
- pre-submission cover-letter framing

Aliases:

- `/journal`
- `/venue`
- `/fit`
- `/target`

### `polish`

Use when the user needs:

- no-feedback polishing
- AI-tone reduction
- style cleanup
- tighter flow
- cleaner academic English
- writing-quality review
- clutter reduction
- passive-voice cleanup
- terminology consistency
- sentence-level clarity audit
- higher-level journal expression
- less AI-sounding prose
- more direct, mature manuscript tone

Aliases:

- `/polish`
- `/edit`
- `/style`
- `/cleanup`

### `revise`

Use when the user needs:

- reviewer-response strategy
- response to reviewers
- editor-letter handling
- collaborator-comment integration
- major revision or resubmission planning

Aliases:

- `/revise`
- `/rebuttal`
- `/response`
- `/resubmit`

## Systematic reviews (PRISMA)

Use when the user is doing a **PRISMA-style systematic review** (protocol, search/screening reporting, flow diagram, synthesis plan) or asks for **Methods/Results** structure aligned with PRISMA 2020.

- **No new slash route** by default: combine existing routes with a clear handoff.
- **First** use `templates/research_task_packet.md` when the work is multi-stage or mixes design + drafting + completeness checking (see `references/prisma-systematic-review.md` for fields to fill).
- **Typical sequence**: `framing` (review question, eligibility, protocol outline) → `draft` (Methods, Results, captions for flow and screening) → `assess` (checklist completeness, number consistency across text and diagram).
- If the bottleneck is overstated synthesis or generalization, add `claim` before or after `draft` as needed.

## Campaign mode

Use campaign mode when the work should continue across turns, phases, or failures rather than starting fresh.

- Recover from the latest checkpoint or memory artifact when one exists.
- Use `templates/research_task_packet.md` for the current step and `templates/campaign_checkpoint.md` for the next step.
- Use `templates/research_memory.md` when the output should preserve durable lessons.
- Use `templates/research_session_log.md` when the run spans multiple hands or needs append-only recovery state.
- If the user presents 3 or more competing paths, run `framing` with `templates/direction_tournament.md` before converging.
- Typical sequence: wake checkpoint -> packetize frontier -> one narrow route -> verify -> distill -> next checkpoint.

## Many-hands rules

- Parallel hands are allowed only when their tasks are independent and mergeable by structure.
- Each hand must receive a narrow packet with explicit scope, inputs, and stop conditions.
- Each hand must return a structured artifact rather than a long narrative summary.
- Keep one coordinator responsible for merge and final user-facing synthesis.
- If hands depend on each other's intermediate reasoning, do not parallelize them.

## Merge contract

- Merge from task packets, evidence registers, checkpoints, claim maps, or other structured artifacts.
- Prefer explicit fields over inferred prose when combining outputs.
- If one hand fails, preserve surviving artifacts and note the missing slice in the checkpoint instead of collapsing the whole run.
- If merge would require reconstructing hidden reasoning from chat history, rerun the work through a cleaner packet instead.

## Conflict rules

- If the user asks for both assessment and rewriting, assess first unless they clearly want immediate text output.
- If the user asks for style polish but the real problem is overclaim, route to `claim` before `polish`.
- If the user asks for writing-quality review, clutter cleanup, passive voice cleanup, or terminology consistency without asking for conceptual judgment, route to `polish`.
- If the user asks for "top-journal tone", "less AI-sounding", or "more natural directness" without asking for new scientific positioning, route to `polish`.
- If the user provides reviewer comments and also asks to rewrite text, route to `revise`, not `polish`.
- If the user specifies a target journal and wants rewriting, route through `journal` judgment and a reference-adequacy audit before `draft` or `polish`.
- If the user asks what is missing before submission, include reference adequacy even if the visible problem first appears to be wording or figure polish.
- If the task spans three or more routes, split it into explicit subproblems instead of pretending one role can do everything cleanly.
- If the task is a continuation of prior work, recover the frontier before choosing the route.
- If the task is tiny and self-contained, do not force packetization, checkpointing, or multi-hand structure.
