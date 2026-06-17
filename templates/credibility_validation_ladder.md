# Credibility Validation Ladder

Use this ladder to classify evidence before using the word validation.

| Validation class | What it can support | What it cannot support by itself |
|---|---|---|
| `physical_or_empirical_outcome_validation` | Direct outcome wording close to the claim, if denominator, uncertainty, and scope are stated | Universal generality outside the tested scope |
| `process_direction_validation` | Directional or mechanistic plausibility | Final outcome validation or real-world effectiveness |
| `component_support_validation` | Plausibility of one component, input, dataset, feature, covariate, measure, or submodule | Whole-system validation, causal certainty, final readiness |
| `monitoring_or_observability_check` | Traceability, auditability, measurement feasibility | Proof that the claimed outcome occurs |
| `diagnostic_consistency_only` | Internal consistency, reproducibility hygiene, expected signs, metadata coherence | Outcome validation, causality, external validity, decision readiness |

Rule: never let `component_support_validation`, `monitoring_or_observability_check`, or `diagnostic_consistency_only` justify wording that implies direct empirical outcome validation, causality, real-world effectiveness, universal generality, physical certainty, or final decision readiness.
