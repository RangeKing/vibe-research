# Reference adequacy audit

Use this audit before journal-specific rewriting, submission-package prep, resubmission planning, or any "what is missing before submission?" assessment.

## Navigation

- Why this exists
- Mandatory triggers
- Quick classification
- Heuristic bands
- Coverage buckets
- Support grading
- Frequent failure patterns
- Output contract

## Why this exists

Selective journals often reject manuscripts that are conceptually interesting but under-cited, unevenly cited, or citation-thin in exactly the places editors check first:

- opening problem framing
- field significance and sector or societal relevance
- key field or sector statistics
- closest methodological precedents
- comparison against adjacent datasets, methods, or competing papers
- numerical parameters, thresholds, coefficients, conversion factors, priors, rates, weights, scenario bounds, and sensitivity ranges
- limitation and risk framing
- population-, region-, or system-specific claims

Low reference count is not the only failure mode. More common is **coverage imbalance**: a manuscript may cite a few recent papers yet still leave major claim categories unsupported.

## Mandatory triggers

Run this audit when any of the following is true:

- the user names a target journal
- the work is near submission
- the task is a submission package, cover letter, or retargeting pass
- the user asks what is missing before submission
- the manuscript is being rewritten for a selective journal
- the task includes supplement construction or figure-story alignment for a journal submission
- the task drafts or revises Methods, equations, models, scenario analysis, sensitivity analysis, or any text that introduces numerical parameters

## Quick classification

Classify reference state as one of:

- `adequate`: reference count and coverage both look plausible for the artifact and venue
- `thin`: total count is obviously too low for a full manuscript or major section
- `uneven`: count may be acceptable, but one or more key claim buckets lack support
- `unknown`: citation format or source text is too incomplete to judge reliably

Also classify parameter provenance:

- `complete`: every manuscript-facing parameter has a source, derivation, unit, and role in the analysis.
- `partial`: most parameters are grounded, but some values, units, or sensitivity bounds still need verification.
- `missing`: one or more parameters appear self-estimated, uncited, or detached from the dataset/method.
- `not_applicable`: the artifact does not use numerical parameters or scenario assumptions.

## Heuristic bands

These are heuristics, not hard rules:

- Full selective-journal research manuscript: anything below roughly `15` references is usually a red flag unless the paper is unusually narrow or short.
- Full Article/Analysis/Resource targeted to a selective journal (for example a Nature-family or flagship field venue): expect a plausible working band around `25-50`, with coherent coverage across framing, methods, comparison set, and implications.
- Section-level rewrite or pre-submission memo: count matters less than whether all factual claims and positioning moves are supported.

Never invent a target count as a journal rule if the journal only gives a recommendation or upper bound.

## Coverage buckets

Check whether the manuscript has enough support in each relevant bucket:

1. **Problem framing**
   Does the opening explain why the question matters using real field literature, not only a statistic report?
2. **Sector significance**
   Are core industry, application, policy, or societal-relevance claims supported?
3. **Closest prior work**
   Are the main methodological or dataset predecessors cited, especially the nearest competing papers?
4. **Journal bridge**
   For a target venue, are there citations that connect the manuscript to the journal's audience and discourse?
5. **Regional or social claims**
   If the text makes claims about specific populations, stakeholder groups, regions, or geography-specific importance, is there context-appropriate support?
6. **Limitations and boundary conditions**
   Are visibility limits, uncertainty sources, and known sector constraints grounded in literature rather than only author assertion?
7. **Methods and validation**
   Are named methods, accuracy claims, data-fusion logic, and comparator approaches anchored to prior literature where appropriate?
8. **Parameter provenance**
   Are numerical parameters, coefficients, thresholds, conversion factors, priors, scenario bounds, weights, sample-size assumptions, and sensitivity ranges supported by literature, user-provided data, transparent derivation, or clearly labeled placeholder status?

## Support grading

For citation-facing or selective-journal work, grade candidate support rather than treating all relevant papers as equivalent:

- `strong`: directly supports the specific claim, scope, population/system, and mechanism or method.
- `partial`: supports part of the claim but misses scope, context, mechanism, geography, or evidence strength.
- `background`: useful for context but not direct evidence for the manuscript's claim.
- `limiting/contradictory`: qualifies, narrows, or conflicts with the claim and should shape wording.
- `metadata-only`: title, abstract, citation count, or database record suggests relevance but the source has not been read enough to support the claim.

Do not use title similarity, citation count, or a broad review article as direct support for an experimental, causal, clinical, or methodological claim. If support is only `partial` or `background`, soften the claim or mark a reference gap.

Do not use self-estimated values as manuscript evidence. A parameter can enter final text only when its value, unit, scope, and uncertainty or sensitivity role are tied to one of:

- a user-provided dataset or calculation that can be described transparently
- a cited literature source that directly matches the parameter's system and scope
- a formal method, standard, protocol, or validated model
- a clearly marked placeholder status for planning text, not final manuscript claims

## Frequent failure patterns

- only citing global reports and almost no peer-reviewed literature
- citing methods papers but not field-importance papers
- citing broad field-level papers but not the specific subfield or sector literature the claims depend on
- citing broad reviews but not the closest competing or precedent papers
- using one citation to support several distinct claims with different scopes
- strong discussion claims that are not matched by literature in the introduction
- figures making comparative or contextual claims that the reference list does not support
- Methods or SI text that contains plausible-looking values without parameter provenance
- sensitivity ranges that are chosen because they "look reasonable" rather than because literature, data, or a stated design rationale supports them
- reference formatting that is clearly off for the target journal

## Output contract

When this audit is triggered, return at least:

- `Reference state`
- `Current count / plausible band`
- `Coverage map`
- `Parameter provenance`
- `Top missing buckets`
- `Insertion plan`
- `Formatting / sequence risks`

If you are also rewriting, do the audit first internally, then revise the text and reference list together instead of bolting citations on at the end.
