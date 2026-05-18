# Assignment 3: Monte Carlo and MCMC

## Goal

Demonstrate simulation-based Bayesian inference and MCMC diagnostics.

## Tasks

1. Simulate 50,000 draws from a posterior `Beta(32, 12)`.
2. Estimate posterior mean, median, 90% interval, and `P(theta > 0.70)`.
3. Fit a Bayesian normal model to `datasets/traffic_wait_times.csv`.
4. Use PyMC with at least 4 chains.
5. Report posterior summaries for the mean and standard deviation.
6. Include trace plots or diagnostic summary.
7. Explain whether the computation appears reliable.

## Required Output

- Monte Carlo summary table
- MCMC summary table
- At least one diagnostic figure
- Interpretation for a non-technical audience

## Rubric

| Criterion | Points |
|---|---:|
| Monte Carlo computation | 20 |
| Correct PyMC model | 25 |
| Diagnostic interpretation | 25 |
| Posterior communication | 20 |
| Reproducibility | 10 |
