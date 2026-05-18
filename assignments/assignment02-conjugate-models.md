# Assignment 2: Conjugate Modeling

## Goal

Use conjugate Bayesian models to update uncertainty and report posterior summaries.

## Dataset

Use `datasets/coin_quality.csv`.

The dataset records pass/fail counts for product-quality batches. Treat each row as binomial data.

## Tasks

1. For each batch, use a `Beta(2, 2)` prior for the pass probability.
2. Compute the posterior distribution for each batch.
3. Report posterior mean and 95% credible interval for each batch.
4. Compute `P(theta > 0.75 | data)` for each batch using simulation.
5. Compare results using `Beta(2, 2)` and `Beta(10, 4)` priors.
6. Explain how prior strength changes posterior conclusions.

## Required Output

- One table of posterior summaries.
- One plot showing prior and posterior for at least one batch.
- One paragraph on sensitivity to prior choice.

## Rubric

| Criterion | Points |
|---|---:|
| Correct posterior updates | 30 |
| Correct simulation summaries | 25 |
| Prior sensitivity comparison | 20 |
| Interpretation | 15 |
| Clean table and figure | 10 |
