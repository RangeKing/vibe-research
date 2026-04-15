# Codex Adapter

Codex uses the root `SKILL.md` as the canonical instructions and `agents/openai.yaml` as the UI metadata layer.

## Recommended invocation

- Explicit: `$vibe-research`
- Route-style prompts:
  - `$vibe-research /assess this manuscript status`
  - `$vibe-research /polish this abstract without changing the claims`
  - `$vibe-research /revise these reviewer comments`
- Chinese natural-language prompts:
  - `$vibe-research 评估这篇稿子目前离投稿还有多远`
  - `$vibe-research 从这个 checkpoint 继续，先找当前 frontier`
  - `$vibe-research 回复这些审稿意见，并给出修改策略`

## Notes

- Let the coordinator run its internal preflight before committing to a route when the request is broad or messy.
- If the input bundle is too long or mixed, compact into an evidence register or task packet before deep execution.
- If the user provides a checkpoint, memory note, or session log, wake from that artifact before generating new prose.
- Keep merge local to the coordinator and merge from structured artifacts, not from chat narration.
- Keep Codex-specific logic out of the root skill body unless it changes the actual reasoning workflow.
- If you update the skill name, description, or default prompt, regenerate `agents/openai.yaml`.
