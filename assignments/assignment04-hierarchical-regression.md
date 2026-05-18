# Assignment 4: Hierarchical Regression

## Goal

Fit and interpret a Bayesian model that uses group structure or predictors.

## Option A: Hierarchical Waiting-Time Model

Use `datasets/traffic_wait_times.csv`.

Tasks:

1. Fit a complete-pooling model.
2. Fit a hierarchical model with stop-level means.
3. Compare posterior estimates for each stop.
4. Explain shrinkage.
5. Report diagnostics.

## Option B: EV Adoption Logistic Regression

Use `datasets/ev_adoption_sample.csv`.

Tasks:

1. Fit a Bayesian logistic regression.
2. Use income, commute distance, and charger access as predictors.
3. Report posterior summaries for coefficients.
4. Interpret the probability that each coefficient is positive.
5. Create one posterior prediction scenario.

## Required Output

- Model specification
- Prior justification
- Posterior summary table
- One figure
- Diagnostics
- Interpretation and limitation

## Rubric

| Criterion | Points |
|---|---:|
| Model specification | 25 |
| Prior justification | 15 |
| Correct computation and diagnostics | 25 |
| Interpretation | 25 |
| Reproducibility | 10 |
