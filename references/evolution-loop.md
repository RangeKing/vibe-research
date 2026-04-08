# Evolution Loop

Read this file when the user is continuing a project, comparing several directions, or asking what should be remembered from failed iterations.

This note selectively borrows from EvoScientist's strongest idea: a research assistant should improve through verified iteration, not by pretending each turn is a fresh start.

## Human-on-the-loop, not runtime-heavy

In this repository, "evolving" does not mean a separate runtime, background workers, or a storage engine.

It means the skill should:

- recover the latest trustworthy checkpoint
- execute one narrow research step
- verify the result against evidence
- distill only reusable lessons
- preserve the next checkpoint

The human remains on the loop by setting direction, deciding when to continue, and choosing which artifacts to trust or reuse.

## Two kinds of memory

### 1. Ideation memory

Use for durable direction-level lessons:

- which questions matter
- which directions survived comparison
- why rejected paths were rejected
- what kinds of novelty or framing actually differentiate the project

### 2. Execution memory

Use for operational lessons:

- which evidence gaps repeatedly kill claims
- which reviewer concerns keep recurring
- which writing constraints should carry forward
- which audit checks matter for figures, PRISMA, or revision logic

Keep the two kinds of memory separate when possible. A rejected direction is not the same as a reusable writing rule.

## Verify before distill

Never copy raw transcript residue into memory.

Before preserving a lesson, ask:

- did this survive evidence checks?
- is this a verified blocker, or only a speculation?
- is this reusable later, or only local to this turn?
- would reusing this reduce future confusion or duplicated work?

Only preserve lessons that pass those filters.

## Candidate evolution

When the user presents several plausible paths, do not jump to one answer too early.

Instead:

1. compare candidates with a fixed lens
2. keep one winner
3. keep up to two viable backups
4. move the rest into a graveyard with reasons

Use `templates/direction_tournament.md` for the comparison and `templates/campaign_checkpoint.md` for the survivors and killed paths.

## Closeout contract for long-horizon work

For campaign work, the closeout should preserve:

- what changed
- what was ruled out
- what should be reused later
- next checkpoint

Use `templates/research_memory.md` when the output should preserve durable lessons.

Use `templates/campaign_checkpoint.md` when the output should preserve resumable state.
