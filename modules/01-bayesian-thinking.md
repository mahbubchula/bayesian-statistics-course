# Module 1: Bayesian Thinking

## Purpose

Bayesian statistics is a framework for learning under uncertainty. Instead of treating unknown quantities as fixed numbers that can only be estimated indirectly, Bayesian analysis represents uncertainty directly with probability distributions.

## Learning Objectives

After this module, learners should be able to:

- Explain the difference between uncertainty and randomness.
- Describe a prior, likelihood, posterior, and posterior predictive distribution.
- Interpret probability as a degree of uncertainty.
- Explain why Bayesian inference is useful for research decisions.

## Core Idea

Bayesian inference starts with a prior belief about an unknown quantity, combines it with data through a likelihood, and produces an updated belief called the posterior.

```text
prior belief + observed data = updated belief
```

Mathematically:

```text
posterior proportional to likelihood times prior
```

or:

```text
p(parameter | data) proportional to p(data | parameter) p(parameter)
```

## Frequentist and Bayesian Questions

A frequentist question often sounds like:

```text
If the null hypothesis were true, how unusual would this result be?
```

A Bayesian question often sounds like:

```text
Given the data and assumptions, what values of the parameter are plausible?
```

Neither framework solves every problem automatically. Bayesian analysis is especially helpful when uncertainty must be explicitly communicated or used for decisions.

## Example: Traffic Signal Improvement

Suppose a city tests a new signal timing plan and wants to know whether it reduces average waiting time.

A classical approach may estimate a mean difference and report a p-value. A Bayesian approach asks:

- What did we believe about the effect before the study?
- How compatible are the data with possible effect sizes?
- After seeing the data, what is the probability that the effect is practically meaningful?
- What decision should be made under cost, risk, and uncertainty?

## Key Vocabulary

| Term | Meaning |
|---|---|
| Parameter | Unknown quantity we want to learn |
| Data | Observed evidence |
| Prior | Distribution representing uncertainty before observing current data |
| Likelihood | Model for how data are generated given the parameter |
| Posterior | Updated uncertainty after combining prior and likelihood |
| Posterior predictive | Distribution of future or replicated data |

## Common Misunderstandings

**Misunderstanding 1: The prior is just personal opinion.**  
A prior can represent expert knowledge, previous studies, weak information, regularization, or formal assumptions. Priors should be justified and tested.

**Misunderstanding 2: Bayesian results are automatically subjective.**  
All statistical models require assumptions. Bayesian analysis makes many of those assumptions explicit.

**Misunderstanding 3: The posterior gives one answer.**  
The posterior is a distribution. It represents a range of plausible values and their relative support.

## Practice

1. Choose a research question from your field.
2. Identify one unknown parameter.
3. Write a sentence describing a possible prior.
4. Write a sentence describing the data you would collect.
5. Write a sentence describing how a posterior result would help decision-making.

## Mini Reflection

Write 150 to 250 words answering:

```text
Why is uncertainty useful rather than something to hide?
```

## Next Module

Continue to [Module 2: Probability Review](02-probability-review.md).
