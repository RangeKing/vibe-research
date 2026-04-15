# Claude Code Adapter

Use the root `SKILL.md` as the canonical workflow description. This adapter adds a Claude Code friendly invocation style and optional routing rules.

## Recommended invocation

- `/framing`
- `/assess`
- `/de-risk`
- `/claim`
- `/draft`
- `/journal`
- `/polish`
- `/revise`

Example prompts:

- `/assess evaluate this abstract and tell me what is missing before submission`
- `/polish make this paragraph cleaner without changing the scientific meaning`
- `/revise turn these reviewer comments into a response strategy`
- `评估这篇摘要，告诉我投稿前最该补什么`
- `从这个 checkpoint 继续，先恢复当前 frontier`
- `这些审稿意见该怎么回复，顺便给我修改策略`

## Suggested routing snippet for `CLAUDE.md`

```markdown
## Skill routing

When the user's request matches the Vibe Research workflow, invoke `vibe-research` first instead of answering ad hoc.

Use `vibe-research` for:
- research framing, direction selection, and research briefs
- manuscript or project assessment
- de-risking, falsifiers, and reviewer-risk scans
- claim-strength review and limitation framing
- title, abstract, and manuscript rewriting
- journal-fit analysis and submission positioning
- polish-only cleanup with no external feedback
- reviewer, editor, or collaborator feedback-driven revision
```

## Boundary reminder

- `polish` is not `revise`
- `assess` should not silently turn into a rewrite unless the user asks
- broad bundles should go through the coordinator's internal preflight and compaction rules before deep rewriting
- checkpoint or memory-driven continuations should wake from durable artifacts before route execution
- if multiple specialist hands are used, merge from their returned artifacts rather than their free-form summaries
- the root skill logic remains platform-neutral
