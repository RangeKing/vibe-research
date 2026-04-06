# OpenClaw Adapter

Use the root `SKILL.md` as the source of truth. This adapter explains how to apply the same role system when subagent orchestration is available.

## Recommended orchestration patterns

### For early-stage research

- Coordinator + `framing`
- Optional parallel support from `de-risk`, `claim`, and `journal`

### For manuscript assessment

- Coordinator + `assess`
- Optional follow-up from `claim` or `journal`

### For submission preparation

- Coordinator + `journal`
- Follow with `draft` or `polish`

### For revision

- Coordinator + `revise`
- Optional support from `claim` when reviewer criticism targets overclaim

## Suggested spawn behavior

- Keep one coordinator thread responsible for final synthesis.
- Spawn narrow specialist threads only when they materially reduce ambiguity.
- Use the same route names as the root skill: `framing`, `assess`, `de-risk`, `claim`, `draft`, `journal`, `polish`, `revise`.

## Fallback rule

If parallel sessions are unavailable, emulate the same role sequence in one thread and still produce the artifact. Do not answer with orchestration theory instead of the requested research output.
