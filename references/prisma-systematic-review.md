# PRISMA-style systematic reviews

Use this reference when the user is planning, drafting, or assessing a **systematic review** that should follow **PRISMA 2020** reporting expectations. This skill does **not** implement automated literature search or database crawling; it supports **decisions and manuscript structure** only.

## What PRISMA 2020 expects (high level)

- A clear **review question** and **eligibility criteria** (PICO or equivalent where applicable).
- **Information sources** and **search strategy** described reproducibly (databases, dates, language limits, supplementary approaches).
- **Study selection**: record counts through identification → screening → eligibility → included, with reasons for exclusions at the full-text stage.
- **Data extraction** and **risk-of-bias** (or quality) tools stated **a priori** where relevant to the field.
- **Synthesis** plan: qualitative, quantitative (e.g. meta-analysis), or both, with heterogeneity and sensitivity considerations when meta-analysis is used.
- **Reporting** aligned to the PRISMA 2020 checklist items the study type requires (see the official PRISMA 2020 statement and extension papers for your review type).

## Flow diagram and where it lives in the manuscript

- The **PRISMA flow diagram** belongs with **results of the search and selection process** (often **Results**, sometimes Methods + Results cross-reference depending on journal style).
- Narrative text should **match the numbers** in the diagram: included/excluded counts, reasons, and any post hoc decisions must not contradict the figure or each other.
- If the review is **ongoing** (e.g. living review), state what is frozen for the current report versus what will update later.

## Task packet usage (`templates/research_task_packet.md`)

For systematic reviews, make the task packet explicit about:

- **Objective**: review question and synthesis goal.
- **Scope**: databases, time window, languages, study designs in/out.
- **Route sequence**: typically `framing` (protocol-level design) → `draft` (Methods / Results structure and PRISMA-aligned prose) → `assess` (completeness vs checklist and internal consistency).
- **Evidence basis**: what the user has already run (searches, exports, screening logs) versus what is still planned.
- **Deliverable**: e.g. Methods subsection outline, PRISMA flow narrative, risk-of-bias table plan, or full-section draft.
- **Acceptance checks**: numbers line up across text, tables, and flow; eligibility rules applied consistently; limitations acknowledge evidence gaps.

## Route mapping (no dedicated `/` route)

| Need | Primary routes |
|------|-------------------|
| Review question, eligibility, protocol outline | `framing` |
| Methods / Results prose, flow diagram caption, search reporting | `draft` |
| Checklist completeness, figure–text consistency, missing PRISMA items | `assess` |
| Overstated synthesis claims | `claim` |
| Revision after peer review on reporting | `revise` |

If the task spans several of these, **one task packet** before deep execution keeps the workflow resumable.
