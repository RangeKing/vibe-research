# Research Session Log

Use this as an append-only event log for long-running or multi-hand work.

## Session metadata

```yaml
session_id: ""
goal: ""
started_from: none | task_packet | checkpoint | memory | mixed
current_frontier: ""
owner: coordinator
```

## Events

- `timestamp`: ""
  `event`: wake | packetize | execute | verify | distill | checkpoint | merge | recover | blocked
  `actor`: coordinator | framing | assess | de-risk | claim | draft | journal | polish | revise | subagent
  `artifact_in`: ""
  `artifact_out`: ""
  `result`: success | partial | failed
  `note`: ""

- `timestamp`: ""
  `event`: ""
  `actor`: ""
  `artifact_in`: ""
  `artifact_out`: ""
  `result`: ""
  `note`: ""

## Current recovery status

- latest_trustworthy_artifact:
- open_issue:
- next_wake_instruction:
