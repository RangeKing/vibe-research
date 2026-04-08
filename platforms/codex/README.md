# Codex Adapter

Codex uses the root `SKILL.md` as the canonical instructions and `agents/openai.yaml` as the UI metadata layer.

## Recommended invocation

- Explicit: `$vibe-research`
- Route-style prompts:
  - `$vibe-research /assess this manuscript status`
  - `$vibe-research /polish this abstract without changing the claims`
  - `$vibe-research /revise these reviewer comments`

## Notes

- Let the coordinator run its internal preflight before committing to a route when the request is broad or messy.
- If the input bundle is too long or mixed, compact into an evidence register or task packet before deep execution.
- Keep Codex-specific logic out of the root skill body unless it changes the actual reasoning workflow.
- If you update the skill name, description, or default prompt, regenerate `agents/openai.yaml`.
