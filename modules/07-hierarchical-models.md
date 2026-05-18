# Module 7: Hierarchical Models

## Purpose

Hierarchical models are one of the most important advantages of Bayesian statistics. They allow information sharing across groups while preserving group-level differences.

## Learning Objectives

After this module, learners should be able to:

- Explain complete pooling, no pooling, and partial pooling.
- Build a hierarchical model for grouped data.
- Interpret group-level variation.
- Understand centered and non-centered parameterizations.

## Motivating Example

Suppose we measure average waiting time at 20 bus stops. Some stops have many observations and others have few. We want to estimate the mean waiting time for each stop.

Three options:

| Approach | Description | Weakness |
|---|---|---|
| Complete pooling | Treat all stops as identical | Ignores stop differences |
| No pooling | Estimate each stop separately | Noisy for small groups |
| Partial pooling | Estimate groups with shared information | Requires hierarchical model |

Partial pooling is usually the most defensible option.

## Basic Hierarchical Normal Model

For observation `i` in group `j`:

```text
y_ij ~ Normal(mu_j, sigma)
mu_j ~ Normal(mu_global, tau)
mu_global ~ Normal(0, 10)
tau ~ HalfNormal(5)
sigma ~ HalfNormal(5)
```

Interpretation:

- `mu_j` is the group-specific mean.
- `mu_global` is the overall mean.
- `tau` describes how much groups differ from each other.
- `sigma` describes within-group variation.

## Shrinkage

Hierarchical estimates are pulled toward the overall mean. This is called shrinkage.

Shrinkage is strongest when:

- A group has little data.
- Group observations are noisy.
- The estimated group-level variation is small.

Shrinkage is weaker when:

- A group has much data.
- Group observations are precise.
- Groups genuinely differ a lot.

## Centered and Non-Centered Parameterization

The centered form is:

```text
mu_j ~ Normal(mu_global, tau)
```

The non-centered form is:

```text
z_j ~ Normal(0, 1)
mu_j = mu_global + z_j * tau
```

Non-centered parameterization often improves MCMC sampling for hierarchical models.

## Practical Uses

Hierarchical models are useful for:

- Schools, classrooms, and students
- Roads, intersections, and cities
- Hospitals, doctors, and patients
- Survey respondents nested in regions
- Repeated measures over time
- Multi-site experiments

## Practice

1. Give an example of grouped data from your field.
2. Explain why no pooling can overfit.
3. Explain why complete pooling can underfit.
4. Write a hierarchical model for crash counts across road segments.

## Lab

Complete [Lab 5: Hierarchical modeling](../labs/lab05_hierarchical_model.py).

## Next Module

Continue to [Module 8: Bayesian Regression](08-bayesian-regression.md).
