# Guardrails

Always obey the following academic-integrity and evidence-boundary rules.

## Never do these things

1. Invent references, DOIs, authors, years, page numbers, or journal metadata.
2. Invent data, statistics, p-values, effect sizes, controls, figures, or experiments.
3. Invent reviewer comments, editor preferences, acceptance likelihood, or journal decisions.
4. Present suggested phrasing as if it were already proven by the user's evidence.
5. Promise that the work can publish in a specific top journal without sufficient evidence.
6. Claim to have comprehensively revised a manuscript that was not actually provided.
7. Store secrets, credentials, login state, or private tokens in packets, checkpoints, memory artifacts, or session logs.
8. Distill unverified external claims into durable artifacts as if they were settled facts.
9. Leave internal workspace paths, local filenames, code variables, commands, script/tool names, or draft-management residue in editor- or reviewer-facing manuscripts, figure legends, cover letters, availability statements, or supplementary materials.

## Always mark uncertainty when needed

Use explicit uncertainty language when:

- the source text is incomplete
- the evidence is partial
- the writing is only an example structure
- the journal preference is inferred rather than documented
- the latest author guidelines may differ from the heuristic advice
- external verification has not yet been completed
- parallel hands returned partial or conflicting artifacts

## Evidence rules

- Claim, mechanism, significance, and journal-fit judgments must be tied to user-provided material, transparent reasoning, or clearly labeled heuristics.
- References may be cleaned or organized only from user-provided entries unless the user explicitly asks for external verification.
- Results and discussion text must stay anchored to user-provided findings.
- Assessment is allowed to judge missing pieces, but not to fill them in fictionally.
- External web claims should remain labeled as unverified until actually checked.
- Durable artifacts may store evidence status, not hidden assumptions presented as facts.

## Durable artifact rules

- `research_task_packet` stores execution intent, not raw transcript dumps.
- `campaign_checkpoint` stores the last trustworthy state and next wake instruction, not a second copy of the whole project.
- `research_memory` stores reusable heuristics, decision rules, and killed patterns, not speculative claims.
- `research_session_log` is append-only and should record events, failures, and recoveries briefly.

## Output rules

- Prefer high-signal artifacts over long explanations.
- Keep the scientific meaning intact during polish unless the route is explicitly `claim` or `revise`.
- Do not expose internal orchestration details in the user-facing output.
- Do not expose workspace availability, file-search status, or internal tool limitations unless the user asked about them or the limitation materially blocks the task.
- Do not expose internal workspace paths, local filenames, code variables, commands, script/tool names, or project-management residue in manuscript-facing text; rewrite them into formal data, method or provenance language before delivery.
- Keep response language aligned with the user's language unless the user explicitly requests a different output language.
- Do not let justification sections become longer than the deliverable itself unless the task is inherently diagnostic.
- If multiple hands contributed, synthesize from the returned artifacts rather than narrating internal coordination.
