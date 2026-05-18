# Module 3: Priors, Likelihoods, and Posteriors

## Purpose

This module teaches the three central components of Bayesian modeling: prior, likelihood, and posterior.

## Learning Objectives

After this module, learners should be able to:

- Define priors and likelihoods for simple data-generating processes.
- Explain how the posterior combines prior information and data.
- Choose weakly informative priors for basic models.
- Interpret posterior summaries and credible intervals.

## Model Building Workflow

A Bayesian model usually follows this structure:

1. Define the outcome variable.
2. Choose a likelihood for the outcome.
3. Define unknown parameters.
4. Assign priors to those parameters.
5. Compute or approximate the posterior.
6. Check whether model predictions resemble the data.
7. Report uncertainty and substantive meaning.

## Example: Bus Arrival Reliability

Suppose a bus route is observed for 40 trips. A trip is "reliable" if it arrives within 5 minutes of the schedule. We observe 30 reliable trips.

Let:

```text
theta = true probability that a trip is reliable
y = number of reliable trips
n = total trips
```

A natural likelihood is:

```text
y ~ Binomial(n, theta)
```

A prior for `theta` might be:

```text
theta ~ Beta(2, 2)
```

This prior is centered at 0.5 but not very strong. After observing 30 successes in 40 trials, the posterior becomes more concentrated near high reliability.

## Prior Types

| Prior Type | Description | Use Case |
|---|---|---|
| Informative | Strong prior knowledge | Previous high-quality studies |
| Weakly informative | Rules out unrealistic values | Most applied work |
| Skeptical | Pulls effects toward zero | Claims requiring strong evidence |
| Regularizing | Stabilizes estimates | Regression or sparse data |
| Sensitivity prior | Alternative prior for comparison | Robustness checking |

## Likelihood Selection

Choose the likelihood by thinking about how the data were generated.

| Data Type | Likelihood |
|---|---|
| Success/failure | Bernoulli or Binomial |
| Count | Poisson or Negative Binomial |
| Continuous symmetric | Normal |
| Positive skewed | Lognormal or Gamma |
| Ordered categories | Ordered logistic |
| Multiple categories | Categorical or Multinomial |

## Posterior Summaries

Common posterior summaries include:

- Posterior mean
- Posterior median
- Standard deviation
- 50%, 80%, 89%, 90%, or 95% credible interval
- Probability that a parameter is above or below a meaningful threshold

Example:

```text
P(theta > 0.70 | data) = 0.86
```

This means that, under the model and prior, there is an 86% posterior probability that the reliability rate exceeds 70%.

## Credible Interval Interpretation

A 95% credible interval means:

```text
Given the model, prior, and data, there is 95% posterior probability that the parameter lies in this interval.
```

This is different from a frequentist confidence interval.

## Practice

1. For a binary survey outcome, propose a likelihood and prior.
2. For traffic crash counts per month, propose a likelihood and prior.
3. Write one posterior probability statement that would be useful to a policy maker.
4. Explain why a weakly informative prior may be better than a completely flat prior.

## Lab

Complete [Lab 1: Beta-binomial updating](../labs/lab01_beta_binomial.py).

## Next Module

Continue to [Module 4: Conjugate Models](04-conjugate-models.md).
