# Module 4: Conjugate Models

## Purpose

Conjugate models give closed-form Bayesian updates. They are the best way to understand posterior learning before using MCMC.

## Learning Objectives

After this module, learners should be able to:

- Explain what conjugacy means.
- Update beta-binomial, gamma-Poisson, and normal-normal models.
- Interpret prior strength as pseudo-data.
- Use conjugate models for quick uncertainty analysis.

## What Is Conjugacy?

A prior is conjugate to a likelihood when the posterior belongs to the same distribution family as the prior.

This makes updating simple:

```text
prior parameters + data summaries = posterior parameters
```

## Beta-Binomial Model

Use this model for a probability.

```text
theta ~ Beta(alpha, beta)
y ~ Binomial(n, theta)
theta | y ~ Beta(alpha + y, beta + n - y)
```

Interpretation:

- `alpha - 1` can be thought of as prior successes.
- `beta - 1` can be thought of as prior failures.

Example:

```text
Prior: Beta(2, 2)
Data: 30 successes out of 40
Posterior: Beta(32, 12)
```

## Gamma-Poisson Model

Use this model for count rates.

```text
lambda ~ Gamma(alpha, beta)
y_i ~ Poisson(lambda)
lambda | y ~ Gamma(alpha + sum(y), beta + n)
```

Here `beta` is a rate parameter.

Example:

```text
Prior crash rate: Gamma(3, 1)
Monthly counts: 2, 4, 3, 5, 4
Posterior: Gamma(21, 6)
```

## Normal-Normal Model

Use this model for a mean when observation variance is known or treated as known.

```text
mu ~ Normal(mu0, tau0^2)
y_i ~ Normal(mu, sigma^2)
```

Posterior precision is:

```text
1 / tau_n^2 = 1 / tau0^2 + n / sigma^2
```

Posterior mean is a precision-weighted average of the prior mean and sample mean:

```text
mu_n = tau_n^2 * (mu0 / tau0^2 + n * ybar / sigma^2)
```

## Why Conjugate Models Matter

Conjugate models teach:

- How priors behave like information.
- How larger data reduce prior influence.
- How posterior uncertainty changes with sample size.
- Why Bayesian inference is a full distribution, not one estimate.

## Practice

1. Start with `Beta(1, 1)` and observe 14 successes in 20 trials. Find the posterior.
2. Start with `Beta(10, 10)` and observe the same data. Compare the posterior.
3. For crash counts `3, 4, 1, 2`, start with `Gamma(2, 1)`. Find the posterior.
4. Explain why conjugate models may be insufficient for complex research questions.

## Lab

Complete [Lab 2: Normal-normal updating](../labs/lab02_normal_normal.py).

## Assignment

Start [Assignment 2: Conjugate Modeling](../assignments/assignment02-conjugate-models.md).

## Next Module

Continue to [Module 5: Monte Carlo Computation](05-computation-monte-carlo.md).
