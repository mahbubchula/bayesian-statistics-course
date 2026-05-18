# Module 11: Causal and Time-Series Extensions

## Purpose

This module introduces advanced directions where Bayesian thinking is valuable: causal inference and time-series modeling.

## Learning Objectives

After this module, learners should be able to:

- Explain the difference between prediction and causal inference.
- Describe Bayesian adjustment for confounding.
- Understand Bayesian time-series modeling at a high level.
- Identify when advanced models require stronger assumptions.

## Bayesian Causal Inference

Bayesian methods do not automatically solve causality. A causal claim still requires a credible research design.

Important ideas:

- Treatment
- Outcome
- Confounder
- Mediator
- Collider
- Counterfactual
- Identification assumption

Bayesian inference can represent uncertainty in causal quantities once the causal model is specified.

## Example: Policy Intervention

Question:

```text
Did a new bus priority policy reduce average corridor delay?
```

A Bayesian analysis may include:

- Pre-policy and post-policy data
- Control corridor
- Time trend
- Day-of-week effects
- Weather or demand variables
- Posterior distribution of the policy effect

## Bayesian Difference-in-Differences

A simplified structure:

```text
y_it ~ Normal(mu_it, sigma)
mu_it = alpha + group_effect + time_effect + policy_effect * treated_i * post_t
```

The posterior distribution of `policy_effect` represents uncertainty about the intervention effect under the design assumptions.

## Bayesian Time Series

Time-series models account for dependency over time.

Common structures:

- Autoregressive models
- State-space models
- Dynamic regression
- Bayesian structural time series
- Gaussian processes

## Forecasting With Uncertainty

Bayesian forecasts produce predictive distributions, not just point forecasts.

For each future time:

- Posterior mean forecast
- Credible interval for expected value
- Prediction interval for future observation

## Caution

Advanced Bayesian models can look impressive but still be wrong if:

- Key confounders are missing.
- Measurement is poor.
- Time trends are misspecified.
- Priors are unrealistic.
- Diagnostics are ignored.

## Practice

1. Define one causal question from transportation, health, or education.
2. List possible confounders.
3. Explain what data would improve the design.
4. Describe why forecasting intervals are more useful than point forecasts.

## Next Module

Continue to [Module 12: Capstone Research Workflow](12-capstone-research-workflow.md).
