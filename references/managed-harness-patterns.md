# Managed Harness Patterns

Use this file when you want the shortest mapping from managed-agent design principles into Vibe Research.

## Principle map

### Stable interfaces over brittle harness tricks

Anthropic's managed-agents design centers on interfaces that can survive changing implementations.

In Vibe Research, the stable interface is:

`doctor -> packetize -> execute -> verify -> distill -> checkpoint -> wake -> merge`

Do not add new routes when a control-plane operation is enough.

### Session outside the context window

The current prompt is not durable state.

In Vibe Research, durable session state lives in:

- `research_task_packet`
- `campaign_checkpoint`
- `research_memory`
- `research_session_log`

Use the smallest artifact that can safely resume work.

### Brain separated from hands

The brain is the coordinator. The hands are route roles, templates, references, and optional subagents.

Implications:

- the coordinator owns synthesis
- hands take narrow packets
- hands return structured artifacts
- hands do not become the system of record

### Replaceable parts, not pets

Do not require one immortal conversation to preserve progress.

If a task is interrupted:

- recover from the latest trustworthy artifact
- continue from the frontier
- avoid replaying the full history unless necessary

### Failure isolation

One broken slice should not corrupt the whole campaign.

Preferred response:

- keep surviving artifacts
- mark the failed slice
- record the recovery move
- continue if the remaining work is still decision-useful

### Security boundary

Managed-agent systems isolate credentials from execution environments.

For this skill, the analogous rule is simpler:

- never store credentials or login state in durable artifacts
- keep unverified external findings labeled as unverified
- preserve evidence status, not hidden trust

## Practical defaults

- Short task: skip heavy harness steps and answer directly.
- Broad task: packetize before deep execution.
- Continuation task: wake first.
- Multi-hand task: only parallelize independent slices.
- Distillation task: preserve reusable rules, not transcript residue.
