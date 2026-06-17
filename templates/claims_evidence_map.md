# Claims-Evidence Map

```yaml
claims:
  - id: C1
    text: ""
    unit_of_claim: phenomenon | mechanism | model | dataset | intervention | population | sample | system | scenario | time_horizon | domain | subgroup | metric | theoretical_construct
    validation_class: physical_or_empirical_outcome_validation | process_direction_validation | component_support_validation | monitoring_or_observability_check | diagnostic_consistency_only | missing
    direct_evidence:
      - ""
    indirect_evidence:
      - ""
    uncertainty_included:
      - ""
    uncertainty_excluded:
      - ""
    scope_boundary: ""
    contradiction_trigger: ""
    parameter_provenance:
      - parameter: ""
        value: ""
        unit: ""
        role_in_claim: ""
        source_or_derivation: ""
        support_grade: strong | partial | background | limiting/contradictory | metadata-only | missing
        sensitivity_needed: yes | no | unclear
    evidence:
      - id: E1
        type: experiment | ablation | case_study | theorem | user_study
        what_to_show: ""
        confounders:
          - ""
        controls:
          - ""
        what_would_change_my_mind: ""

figures:
  - id: F1
    takeaway: ""
    supports: [C1]
    five_second_central_result_test: pass | partial | fail | not_applicable
    metric: ""
    denominator: ""
    effect_size: ""
    uncertainty: ""
    scope: ""
    data_source: ""
    caption_draft: ""
    stands_alone_check: pass | fail
    fix_if_fail: ""
```
