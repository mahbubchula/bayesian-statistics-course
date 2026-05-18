# Module 5: Monte Carlo Computation

## Purpose

Most useful Bayesian models cannot be solved by hand. Monte Carlo methods approximate posterior quantities using random samples.

## Learning Objectives

After this module, learners should be able to:

- Explain Monte Carlo approximation.
- Estimate posterior means, intervals, and probabilities from simulated draws.
- Use simulation to understand uncertainty.
- Recognize Monte Carlo error.

## The Main Idea

If we can draw samples from a posterior distribution:

```text
theta_1, theta_2, ..., theta_S
```

then we can approximate posterior summaries.

Posterior mean:

```text
mean(theta_s)
```

Posterior interval:

```text
quantile(theta_s, 0.025), quantile(theta_s, 0.975)
```

Posterior probability:

```text
mean(theta_s > threshold)
```

## Example: Probability of High Reliability

Suppose:

```text
theta | y ~ Beta(32, 12)
```

We want:

```text
P(theta > 0.70 | data)
```

Draw 20,000 samples from `Beta(32, 12)` and compute the proportion greater than 0.70.

This turns a probability calculation into a simulation calculation.

## Monte Carlo Error

Monte Carlo estimates vary because they are based on random samples. Increasing the number of samples reduces simulation noise.

If an estimated posterior probability is based on `S` independent samples, a rough standard error is:

```text
sqrt(p * (1 - p) / S)
```

## Simulation-Based Workflow

1. Draw samples from the prior.
2. Draw synthetic data from the likelihood.
3. Compare simulated data to plausible real data.
4. Fit the model or update analytically if possible.
5. Draw samples from the posterior.
6. Summarize posterior quantities.
7. Draw posterior predictive data.

## Prior Predictive Checks

Before fitting a model, simulate from the prior predictive distribution:

```text
parameter ~ prior
data ~ likelihood(parameter)
```

Ask:

- Are the simulated data plausible?
- Does the prior allow impossible values?
- Is the prior too narrow or too wide?

## Practice

1. Simulate 10,000 draws from `Beta(5, 5)`.
2. Estimate `P(theta > 0.60)`.
3. Repeat with 1,000 draws and compare.
4. Explain why simulation is useful even when formulas exist.

## Lab

Complete [Lab 3: Monte Carlo integration](../labs/lab03_monte_carlo.py).

## Next Module

Continue to [Module 6: MCMC](06-mcmc.md).
