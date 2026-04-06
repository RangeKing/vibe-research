# Routing

Route based on the user's immediate problem, not the full lifecycle of the paper.

## Route table

### `framing`

Use when the user needs:

- research ideation
- one-liner design
- research brief creation
- killer experiments
- hypotheses and falsifiers
- a two-week go/no-go plan

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

## Conflict rules

- If the user asks for both assessment and rewriting, assess first unless they clearly want immediate text output.
- If the user asks for style polish but the real problem is overclaim, route to `claim` before `polish`.
- If the user provides reviewer comments and also asks to rewrite text, route to `revise`, not `polish`.
- If the user specifies a target journal and wants rewriting, route through `journal` judgment before `draft` or `polish`.
- If the task spans three or more routes, split it into explicit subproblems instead of pretending one role can do everything cleanly.
