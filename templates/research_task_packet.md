# Research Task Packet

```yaml
task:
  objective: ""
  frontier: ""
  campaign_mode: true | false
  stage: idea | results | draft | near_submission | revision | resubmission
  route: framing | assess | de-risk | claim | draft | journal | polish | revise
  session_state: none | packet | checkpoint | memory | session_log | mixed
  recovery_mode: none | wake_first | compact_first | salvage_partial | ask_for_anchor_artifact
  context_budget:
    pressure: low | medium | high
    read_depth: full | summaries_only | packet_only
    checkpoint_before_expanding: true | false
  target_journal: ""
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
