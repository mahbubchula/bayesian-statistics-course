# Module 2: Probability Review

## Purpose

Bayesian statistics depends on conditional probability. This module reviews the probability concepts needed for the rest of the course.

## Learning Objectives

After this module, learners should be able to:

- Use probability notation clearly.
- Apply the product rule, sum rule, and Bayes theorem.
- Distinguish between joint, marginal, and conditional probability.
- Explain base-rate effects in diagnostic reasoning.

## Probability Rules

### Sum Rule

For mutually exclusive events:

```text
P(A or B) = P(A) + P(B)
```

More generally:

```text
P(A or B) = P(A) + P(B) - P(A and B)
```

### Product Rule

```text
P(A and B) = P(A | B) P(B)
```

also:

```text
P(A and B) = P(B | A) P(A)
```

### Bayes Theorem

From the product rule:

```text
P(A | B) = P(B | A) P(A) / P(B)
```

The denominator can be expanded:

```text
P(B) = P(B | A) P(A) + P(B | not A) P(not A)
```

## Diagnostic Example

Suppose a screening test has:

- Disease prevalence: 1%
- Sensitivity: 95%
- False positive rate: 10%

Question:

```text
If a person tests positive, what is the probability they have the disease?
```

Calculation:

```text
P(Disease | Positive)
= P(Positive | Disease) P(Disease) / P(Positive)
```

where:

```text
P(Positive) = 0.95 * 0.01 + 0.10 * 0.99 = 0.1085
```

So:

```text
P(Disease | Positive) = 0.0095 / 0.1085 = 0.0876
```

Even with a positive test, the probability is about 8.8%. The low base rate matters.

## Why This Matters for Bayesian Statistics

In Bayesian inference:

```text
P(parameter | data) = P(data | parameter) P(parameter) / P(data)
```

This has the same structure as the diagnostic example:

- `P(parameter)` is the prior.
- `P(data | parameter)` is the likelihood.
- `P(parameter | data)` is the posterior.
- `P(data)` normalizes the posterior.

## Probability Distributions

Bayesian models use probability distributions for data and unknown parameters.

| Distribution | Typical Use |
|---|---|
| Bernoulli | Single yes/no outcome |
| Binomial | Number of successes in fixed trials |
| Poisson | Count over time or space |
| Normal | Continuous measurement |
| Exponential | Waiting time |
| Beta | Probability between 0 and 1 |
| Gamma | Positive rate or scale parameter |

## Practice

1. A test has sensitivity 90%, false positive rate 5%, and prevalence 2%. Compute `P(Disease | Positive)`.
2. Give one example of a Bernoulli variable in transportation research.
3. Give one example of a Poisson variable in public health or traffic safety.
4. Explain the difference between `P(data | model)` and `P(model | data)`.

## Next Module

Continue to [Module 3: Priors, Likelihoods, and Posteriors](03-priors-likelihood-posteriors.md).
