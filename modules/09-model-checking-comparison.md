# Module 9: Model Checking and Comparison

## Purpose

Bayesian modeling does not end after fitting. A responsible analysis checks whether the model can reproduce important patterns in the data.

## Learning Objectives

After this module, learners should be able to:

- Explain posterior predictive checking.
- Identify model misfit with simulated replicated data.
- Compare models using predictive criteria.
- Avoid choosing models only by in-sample fit.

## Posterior Predictive Distribution

The posterior predictive distribution asks:

```text
What data would we expect to see again if the fitted model were true?
```

Workflow:

1. Draw parameters from the posterior.
2. Simulate replicated data from the likelihood.
3. Compare replicated data to observed data.

## Posterior Predictive Checks

Compare observed and simulated:

- Means
- Standard deviations
- Quantiles
- Counts of extreme values
- Group-level patterns
- Time trends
- Residual structure

If the observed pattern is rarely seen in replicated data, the model may be missing something important.

## Good Fit Does Not Mean True Model

A model is a simplified representation. Posterior predictive checks help identify useful and harmful simplifications, but they do not prove the model is true.

## Model Comparison

Common Bayesian model comparison tools:

| Tool | Use |
|---|---|
| LOO-CV | Approximate leave-one-out predictive accuracy |
| WAIC | Information criterion based on posterior predictive density |
| Bayes factor | Evidence ratio for models, sensitive to priors |
| Stacking | Weighted predictive model averaging |

For applied work, predictive checking and cross-validation are often more useful than a single ranking number.

## Overfitting

A model can fit current data well but predict future data poorly. Bayesian priors reduce overfitting, but they do not eliminate it automatically.

## Model Expansion

When checks reveal misfit, possible responses include:

- Add missing predictors.
- Use a different likelihood.
- Add group-level structure.
- Model nonlinearity.
- Allow varying variance.
- Revisit measurement assumptions.

## Practice

1. Name three statistics you would check for a waiting-time model.
2. Explain why posterior predictive checks use simulated data.
3. Compare LOO-CV and Bayes factors conceptually.
4. Describe one way a regression model can fit poorly even with good coefficient estimates.

## Next Module

Continue to [Module 10: Bayesian Decision Analysis](10-bayesian-decision-analysis.md).
