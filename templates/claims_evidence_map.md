# Claims-Evidence Map

```yaml
claims:
  - id: C1
    text: ""
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
    data_source: ""
    caption_draft: ""
    stands_alone_check: pass | fail
    fix_if_fail: ""
```
