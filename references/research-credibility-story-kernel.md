# Research Credibility And Story Kernel

Use this reference for manuscript assessment, claim review, drafting, figure/table review, reviewer simulation, response strategy, scorecards, and project planning. It is deliberately venue-neutral and field-neutral.

## Navigation

- Core purpose
- Contribution-first narrative
- Claim-level credibility validation
- Evidence-to-claim boundary discipline
- Result credibility gates
- Limitation triage
- Model, scenario, and spatial story rules
- Temporal matching for historical samples and modern variables
- Story-spine reconstruction
- Central-result figure/table gate
- Editor pull test
- Reviewer attack test
- Red-team reviewer simulation
- Score discipline
- Anti-overclaim rewrite checks
- Minimum useful output

## Core purpose

Research help should improve judgment before prose. Before polishing, reconstruct what the work claims, what evidence directly supports it, what only supports a component or process, and what wording the evidence can honestly bear.

Use neutral terms such as target venue, target format, gatekeeper reader, specialist reviewer, central claim, key figure/table, empirical outcome, diagnostic/proxy metric, validation class, and scope boundary.

## Contribution-first narrative

Lead with the strongest defensible scientific product, not the weakest data limitation. High-level journals need a positive, legible contribution that an editor can repeat in one sentence: a new map, prediction, mechanism, threshold, risk zone, scenario result, model, dataset, synthesis, or management priority that changes what the field can see or decide.

Before assessment or rewriting, identify:

- major scientific, social, environmental, health, engineering, or policy problem
- missing dimension in the current literature
- unique evidence, experiment, observation, model, comparison, or scenario analysis
- Core result product: the memorable map, prediction, mechanism, threshold, classification, risk transfer, intervention boundary, or decision priority
- mechanism, driver, or explanatory account behind the result
- implication for future research, management, policy, or practice
- uncertainty that must be visible for the conclusion to remain bold but credible

Quality control, evidence thresholds, missing-data labels, robustness checks, and uncertainty analysis should normally function as confidence architecture around that product. They tell the reader which parts of the result are high-confidence, sensitivity-dependent, extrapolated, or unresolved. They should not become the headline story unless the work is explicitly a methods, data-quality, or evidence-standard paper.

Prefer this lift:

- weak: "we screened and checked a dataset"
- stronger: "we used evidence thresholds to produce a confidence-graded prediction, map, mechanism test, or decision ranking that was not previously possible"

## Claim-level credibility validation

For every substantial claim, identify:

- exact claim
- unit of claim: phenomenon, mechanism, model, dataset, intervention, population, sample, system, scenario, time horizon, domain, subgroup, metric, or theoretical construct
- evidence directly supporting the claim
- evidence only indirectly supporting the claim
- strongest uncertainty source
- weakest inference link
- validation class present
- validation class missing
- whether the wording is calibrated to the evidence

Validation ladder, strongest to weakest:

1. `physical_or_empirical_outcome_validation`: directly tests the outcome closest to the claim.
2. `process_direction_validation`: supports the proposed direction or mechanism but not the final claimed outcome.
3. `component_support_validation`: supports one component, input, feature, dataset, submodule, covariate, or measurement source.
4. `monitoring_or_observability_check`: shows the system can be observed, measured, or audited.
5. `diagnostic_consistency_only`: shows internal consistency, reproducibility, clean files, coherent metadata, or expected-sign agreement.

Never let `component_support_validation`, `monitoring_or_observability_check`, or `diagnostic_consistency_only` support wording that implies direct outcome validation, causality, real-world effectiveness, universal generality, physical certainty, or final decision readiness.

## Evidence-to-claim boundary discipline

For every main result, answer:

- What exactly is proven?
- What is only suggested?
- What is explicitly not proven?
- What wording is allowed?
- What wording is prohibited unless new evidence is added?
- What figure, table, result, experiment, or source supports the allowed wording?
- What contradiction would invalidate the current claim?

Use `templates/claim_boundary_card.md` in `/claim`, `/assess`, `/draft`, `/revise`, and near-submission verification when a central claim is involved.

## Result credibility gates

Before calling a result robust, validated, compelling, ready, strong, or high-confidence, check:

- Gate A Traceability: prose to figure/table/result to method to source data or experiment.
- Gate B Denominator and effect size: sample, model, observation, case, trial, comparison basis, and effect size are visible.
- Gate C Uncertainty propagation: uncertainty reaches the final claim, not only upstream components.
- Gate D Validation strength: validation is close to the final claim, not only process/component/consistency support.
- Gate E Contradiction guard: figures, tables, source data, captions, abstract, title, conclusion, and response-letter claims agree.
- Gate F Scope honesty: text states what the result does not estimate, predict, prove, validate, or generalize to.

Consider these uncertainty classes: model, parameter, threshold, aggregation, sampling or observational, measurement, spatial/temporal dependence, subgroup/domain heterogeneity, missing-data or selection, robustness to alternative definitions, and external validity.

If any gate fails, downgrade the claim, propose the smallest repair, or mark the result diagnostic, exploratory, or preliminary rather than validated.

## Limitation triage

Do not let any limitation automatically downgrade the whole manuscript to an internal audit or preliminary screen. Classify each limitation first:

1. `conclusion_overturning`: could reverse or invalidate the central result. Change the claim, redesign the analysis, or stop the high-level story.
2. `main_analysis_scope`: determines which samples, locations, time periods, variables, or observations belong in the main analysis. Handle with inclusion criteria, evidence weights, confidence grades, or sensitivity analysis.
3. `precision_or_ranking`: affects numerical precision, interval width, uncertainty, or local ranking but not the main direction or broad spatial/temporal ordering. Handle with uncertainty propagation, robustness tests, and range language.
4. `causal_language_boundary`: limits causal or mechanistic interpretation but still permits association, prediction, explanatory power, mechanism-consistent wording, or priority identification.

Only the first class should usually collapse the central story. The second, third, and fourth classes should shape the confidence architecture and wording boundaries.

## Model, scenario, and spatial story rules

For model, prediction, spatial extrapolation, or scenario papers, separate result layers explicitly:

- direct observation
- model prediction
- sensitivity analysis
- extrapolation
- evidence-insufficient or no-judgment regions

Do not disguise model predictions as direct observations. Also do not delete justified prediction maps simply because extrapolation or uncertainty exists. The right high-level product is often a map or scenario result that shows prediction value, confidence, uncertainty, and unresolved regions together.

For scenario papers, require baseline state, scenario definition, feasibility constraint, change magnitude, risk-class transition, uncertainty range, regions with large improvement, regions with limited improvement, and the mechanism explaining heterogeneous responses. Do not stop at mean changes when the publishable result is spatial response, risk transfer, or management boundary.

For spatial-map papers, require direct-observation labels, predicted-area labels, spatial block or regional holdout validation, prediction uncertainty, confidence levels, extrapolation masks, and evidence-insufficient areas. The map should not pretend every location has equal evidence strength; it should show where the answer is strong, weak, extrapolated, or still unavailable.

## Temporal matching for historical samples and modern variables

When historical samples and modern variables appear in the same analysis, check time matching before driver or mechanism claims:

- Each sample, layer, observation window, or experiment should have a stated time range.
- External variables should match that time range as closely as possible.
- Records that cannot be matched to remote sensing, climate, socioeconomic, or other external variables should not enter the main driver model.
- Older records may provide long-term constraints, background evidence, or sensitivity checks, but should not be forced into explanation by modern covariates.
- Build a variable availability matrix showing which variables are usable for each time period and location.

If time matching fails, move the analysis to background interpretation, sensitivity analysis, or long-term constraint instead of presenting it as the main factor explanation.

## Story-spine reconstruction

Before rewriting a manuscript, reconstruct the story spine:

1. Misleading default.
2. Real problem.
3. Boundary.
4. New separation.
5. Central answer.
6. Mechanism.
7. Credibility check.
8. Boundary again.
9. Implication.

If the current draft lacks this spine, produce a rewritten outline before editing paragraphs. Use `templates/story_spine.md`.

## Central-result figure/table gate

Use the five-second central-result test for any key display item: a reader should identify the central result within five seconds from the key figure or table.

Every main figure/table should expose one-sentence message, metric and unit/class, comparison basis, effect size, denominator, uncertainty or robustness marker, scope labels, source/method traceability, supported claim, and claim boundary. A display item that only shows provenance, inputs, workflow, decorative maps, dense dashboards, or component inventories cannot carry the central claim unless redesigned.

Use `templates/figure_table_claim_gate.md`.

## Editor pull test

Before finalizing a title, abstract, introduction objective, Results subheadings, figure order, Discussion opening, or cover-letter pitch, check:

- Can an editor state the main contribution in one sentence?
- Does the title present a result rather than a workflow?
- Does the abstract end with a finding, prediction, risk, mechanism, or management implication?
- Do Results subheadings read like discoveries rather than process steps?
- Do figures move from problem to evidence to model/mechanism to future or action?
- Is uncertainty transparent without overpowering the contribution?
- Is the story bold enough to justify the target venue while staying evidence-bound?

If not, raise the story level before sentence polishing.

## Reviewer attack test

When making the story more ambitious, simultaneously check overclaim risk:

- Which conclusions may lack evidence?
- Which results are direct observations versus model predictions?
- Which results belong only in sensitivity analysis?
- Which regions or cases are extrapolated?
- Are sample times and external-variable times aligned?
- Are scenarios physically, ecologically, socially, or statistically feasible?
- Is uncertainty quantified and propagated to the final claim?
- Are causal and predictive/associational claims separated?
- Do the strongest conclusions come from the highest-confidence evidence?
- Could a figure imply that all areas have equal support when they do not?

Fix risk with confidence grading, sensitivity layers, language calibration, or figure legends. Do not abandon the central contribution unless the risk is conclusion-overturning.

## Red-team reviewer simulation

For substantial assessment, revision, or near-submission work, simulate hostile-but-fair readers:

- gatekeeper reader
- domain specialist
- methods/statistics reviewer
- data/reproducibility reviewer
- skeptical generalist
- application/decision reviewer

Do not obey reviewer-like criticism blindly. Decide whether each objection reveals an evidence gap, framing gap, methods gap, citation gap, or communication issue. Use `templates/reviewer_red_team_matrix.md`.

## Score discipline

Scores are heuristic gap diagnoses, not probabilities of acceptance or success. Do not reward polish unless evidence and claim boundaries are sound. A clean package, reproducible code, complete metadata, or polished writing cannot overcome a weak central claim.

Any fatal claim-evidence contradiction caps readiness below a strong score. Any major unresolved evidence or validation gap caps readiness even if writing is fluent. A score above 90/100 requires no fatal flaws, no major unresolved evidence gaps, central figures/tables that carry the claim, adequate uncertainty propagation, validation close to the claim, review-level traceability, and clear scope boundaries.

Use `templates/score_cap_card.md` whenever giving a numeric or banded score.

## Anti-overclaim rewrite checks

Prevent five common overclaims:

1. Diagnostic metric presented as physical or empirical outcome.
2. Correlation or association presented as causation.
3. Component support presented as whole-system validation.
4. Scenario, subgroup, model, sample, or dataset result presented as universal.
5. Internal consistency or reproducibility presented as external validation.

For every rewrite, check whether any sentence implies stronger evidence than exists, converts proxy/diagnostic evidence into outcome evidence, erases denominator/uncertainty/scope, makes a domain-level claim from subgroup evidence, or implies validation where only support exists. If yes, soften the claim or add the missing boundary.

## Minimum useful output

If the user asks broadly, do not block on excessive clarification. Produce the smallest useful artifact: credibility audit, story-spine outline, claim-boundary table, figure/table redesign plan, reviewer-risk matrix, revision priority list, rewritten abstract skeleton, validation upgrade plan, or evidence gap map. Mark assumptions explicitly.
