# Paradigm Audit Checklist

Use this checklist to surface bad defaults, path dependence, and easy-to-miss evaluation failures.

## Metrics and task definition

- Does the main metric actually represent the research question?
- Is there an obvious route for metric gaming?
- Does one metric hide an important tradeoff?

## Baselines and controls

- Is the baseline truly strong, or merely convenient?
- Is an obvious baseline missing?
- Is a negative control needed to rule out leakage or shortcut behavior?

## Confounders

- Could there be data leakage, temporal leakage, sampling bias, or duplicate examples?
- Could compute budget or hyperparameter unfairness explain the improvement?

## Toxic default signals

- Everyone repeats a setup choice that nobody justifies.
- A legacy paper made an arbitrary decision and the field copied it.
- A problem is assumed to be hard only because people use the same framing.

## Reproducibility

- Is there a minimal reproducible setup?
- Does the main conclusion depend on one seed, one split, or one cherry-picked example?

## Narrative pressure test

- Would the introduction make a skeptical reader care?
- Can the killer figure stand alone?
- Does the conclusion explain what changes in practice or understanding?
