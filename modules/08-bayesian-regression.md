# Module 8: Bayesian Regression

## Purpose

Regression is the most common applied modeling workflow. Bayesian regression provides full uncertainty over coefficients, predictions, and decisions.

## Learning Objectives

After this module, learners should be able to:

- Fit Bayesian linear regression.
- Interpret posterior distributions for coefficients.
- Use regularizing priors.
- Extend regression to binary and count outcomes.

## Bayesian Linear Regression

For continuous outcome `y`:

```text
y_i ~ Normal(mu_i, sigma)
mu_i = alpha + beta_1 x_1i + beta_2 x_2i
alpha ~ Normal(0, 10)
beta_k ~ Normal(0, 2)
sigma ~ HalfNormal(5)
```

The coefficients are not single numbers. Each coefficient has a posterior distribution.

## Standardizing Predictors

Standardization often improves modeling:

```text
x_standardized = (x - mean(x)) / sd(x)
```

Benefits:

- Priors become easier to choose.
- MCMC sampling improves.
- Coefficients are easier to compare.

## Regularizing Priors

Weakly informative priors reduce unreasonable estimates.

Example:

```text
beta ~ Normal(0, 1)
```

This says large effects are possible but less likely.

## Logistic Regression

For binary outcomes:

```text
y_i ~ Bernoulli(p_i)
logit(p_i) = alpha + beta x_i
```

Use logistic regression when the outcome is yes/no, success/failure, adopted/not adopted, crash/no crash.

## Poisson Regression

For count outcomes:

```text
y_i ~ Poisson(lambda_i)
log(lambda_i) = alpha + beta x_i
```

Use count models for crashes, calls, arrivals, incidents, or events per unit.

## Posterior Prediction

Bayesian regression naturally gives predictive uncertainty:

```text
new parameter draw -> predicted mean -> simulated outcome
```

This separates uncertainty about the mean from uncertainty about future observations.

## Communication

Instead of only reporting:

```text
beta = 0.42
```

report:

```text
The posterior mean of beta is 0.42, with a 95% credible interval from 0.10 to 0.75. Under the model, the probability that beta is positive is 0.99.
```

## Practice

1. Write a Bayesian linear regression model for travel time.
2. Write a Bayesian logistic regression model for EV adoption.
3. Explain why priors on regression coefficients are useful.
4. Explain how posterior prediction differs from fitted values.

## Lab

Complete [Lab 6: Bayesian regression workflow](../labs/lab06_bayesian_regression.py).

## Assignment

Start [Assignment 4: Hierarchical Regression](../assignments/assignment04-hierarchical-regression.md).

## Next Module

Continue to [Module 9: Model Checking and Comparison](09-model-checking-comparison.md).
