# Research Task Packet

```yaml
task:
  objective: ""
  frontier: ""
  campaign_mode: true | false
  codex_goal_context: none | supplied | inferred | unknown
  stage: idea | results | draft | near_submission | revision | resubmission
  route: framing | assess | de-risk | claim | draft | journal | polish | revise
  session_state: none | packet | checkpoint | memory | session_log | mixed
  recovery_mode: none | wake_first | compact_first | salvage_partial | ask_for_anchor_artifact
  context_budget:
    pressure: low | medium | high
    read_depth: full | summaries_only | packet_only
    checkpoint_before_expanding: true | false
  rationalization_pressure:
    level: low | medium | high
    triggers:
      - deadline | sunk_cost | reviewer_anxiety | journal_ambition | just_polish | external_feedback | other
  target_journal: ""
  target_score:
    bar: ""
    source: heuristic | user_defined | journal_specific | unknown
    current_score: ""
    current_band: not_submission_ready | barely_submission_ready | uncertain_editorial_handling | likely_review | very_strong | near_perfect | unknown
    journal_score_gap: ""
  bottleneck: ""
  inputs:
    artifacts:
      - ""
    source_notes:
      - ""
  memory_inputs:
    - ""
  surviving_candidates:
    - ""
  killed_candidates:
    - ""
  scope:
    include:
      - ""
    exclude:
      - ""
  artifact_basis:
    provided:
      - ""
    missing:
      - ""
  source_coverage:
    required: none | light | strict
    required_items:
      - id: ""
        source: user_decision | reviewer_comment | journal_rule | claim | figure | supplementary_information | citation | other
        requirement: ""
        output_target: ""
        status: pending | covered | deferred | impossible
    deferred_items:
      - id: ""
        reason: ""
  evidence_basis: strong | partial | weak | unknown
  reference_state: adequate | thin | uneven | unknown
  gates:
    root_cause:
      required: true | false
      issue: ""
      likely_source: evidence | claim | framing | method | citation | figure_si_accounting | prose | unknown
      checked_before_drafting: true | false
    quality:
      required: true | false
      checks:
        - ""
    coverage:
      required: true | false
      blocking: true | false
      checks:
        - "Required source items are covered or explicitly deferred"
    safety:
      required: true | false
      blockers:
        - ""
    transition:
      required: true | false
      next_action: ""
  citation_plan:
    needed: true | false
    artifact: none | reference_coverage_map
    priority_buckets:
      - ""
  scorecard_plan:
    needed: true | false
    artifact: none | target_journal_scorecard
    evidence_basis: complete_package | manuscript_only | partial_artifact | verbal_summary | unknown
    score_confidence: high | medium | low | unknown
    blocking_caps:
      - ""
    dimensions_to_rescore:
      - ""
  deliverable: ""
  merge_target: none | coordinator_synthesis | checkpoint_update | memory_update
  acceptance_checks:
    - "Matches the real bottleneck"
    - "Stays evidence-bound"
    - "Produces a concrete usable artifact"
  stop_conditions:
    - ""
  distillation_targets:
    - ""
  fallback_artifact: ""
  next_checkpoint: ""
  next_if_blocked: ""
```
