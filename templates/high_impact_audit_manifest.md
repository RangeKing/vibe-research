# High-Impact Audit Manifest

Required artifacts before any high-impact submission-ready claim:

- `audits/claim_figure_truth_table.tsv`
- `audits/display_item_budget.tsv`
- `audits/reviewer_panel_cards.md`
- `audits/ncc_desk_rejection_memo.md`
- `audits/score_caps.md`
- `audits/abstract_claim_boundary.tsv`
- `audits/figure_scientific_scores.tsv`

Verification command:

```bash
python3 scripts/high_impact_submission_gate.py <package-root> --reported-score <score>
```

Result:
- Gate status:
- Active cap:
- Score allowed:
- Rescore condition:
