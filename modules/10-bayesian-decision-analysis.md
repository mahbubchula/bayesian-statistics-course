# Module 10: Bayesian Decision Analysis

## Purpose

Bayesian statistics is especially useful when decisions must be made under uncertainty. This module connects posterior distributions to decisions.

## Learning Objectives

After this module, learners should be able to:

- Explain expected utility and expected loss.
- Use posterior probabilities for decision thresholds.
- Distinguish statistical significance from practical value.
- Build a simple Bayesian decision rule.

## From Inference to Decision

A posterior distribution answers:

```text
What is plausible after seeing the data?
```

A decision analysis asks:

```text
What should we do, given uncertainty, costs, benefits, and risk?
```

## Expected Loss

Suppose a decision `d` has loss `L(d, theta)` if the true state is `theta`.

The posterior expected loss is:

```text
E[L(d, theta) | data]
```

Choose the decision with the smallest posterior expected loss.

## Practical Thresholds

For many research problems, the important question is not whether an effect is exactly zero. It is whether the effect is practically meaningful.

Example:

```text
P(waiting_time_reduction > 2 minutes | data)
```

This is often more useful than asking whether the effect is nonzero.

## Decision Example

A new traffic control system costs money to implement. Decision makers may require:

```text
P(average_delay_reduction > 10%) > 0.80
```

If this posterior probability is above 0.80, the system is adopted. If not, more data may be collected.

## Value of Information

Sometimes the best decision is not immediate adoption or rejection, but collecting more data.

Ask:

- How uncertain are we?
- How costly is a wrong decision?
- How expensive is more data collection?
- Could new data change the decision?

## Communicating Decisions

A strong decision report includes:

- The posterior probability of benefits.
- The expected loss or expected utility.
- Sensitivity to prior choices.
- Sensitivity to cost assumptions.
- A clear recommendation with uncertainty.

## Practice

1. Define a decision in your field with two possible actions.
2. List one benefit and one cost for each action.
3. Define a posterior probability threshold for action.
4. Explain why "statistically significant" is not the same as "worth implementing."

## Next Module

Continue to [Module 11: Causal and Time-Series Extensions](11-causal-and-time-series.md).
