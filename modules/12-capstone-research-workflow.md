# Module 12: Capstone Research Workflow

## Purpose

The final module shows how to combine the course into a complete Bayesian research workflow.

## Learning Objectives

After this module, learners should be able to:

- Define a Bayesian research question.
- Build a reproducible model workflow.
- Write a transparent model report.
- Present uncertainty clearly.

## Capstone Workflow

1. State the research question.
2. Define the outcome and predictors.
3. Choose a likelihood.
4. Justify priors.
5. Fit the model.
6. Diagnose computation.
7. Check model predictions.
8. Summarize posterior results.
9. Conduct sensitivity analysis.
10. Communicate conclusions and limitations.

## Recommended Report Structure

```text
Title
Abstract
Research question
Data description
Model specification
Prior justification
Computation and diagnostics
Posterior results
Posterior predictive checks
Sensitivity analysis
Decision or implication
Limitations
Reproducibility statement
References
```

## Model Specification Template

Use a clear block like this:

```text
y_i ~ likelihood(parameter_i)
parameter_i = function(alpha, beta, predictors)
alpha ~ prior
beta ~ prior
scale_parameter ~ prior
```

Every symbol should be explained in words.

## Posterior Results Template

Use sentences like:

```text
The posterior mean effect was X, with a 95% credible interval from L to U.
Under the model, the probability that the effect is positive was P.
The probability that the effect exceeds the practical threshold T was Q.
```

## Reproducibility Checklist

- Raw or synthetic dataset included
- Data cleaning steps documented
- Random seed set
- Model code included
- Software versions listed
- Diagnostics shown
- Figures and tables generated from code
- Limitations stated honestly

## Presentation Checklist

A good capstone presentation should answer:

- What was the decision or research problem?
- What uncertainty mattered?
- What model did you build?
- Did the model compute reliably?
- What did the posterior show?
- What decision or interpretation follows?
- What are the limitations?

## Final Practice

Draft a one-page capstone plan with:

- Research title
- Data source
- Outcome variable
- Candidate likelihood
- At least two priors
- Main posterior quantity of interest
- One model check
- One decision or interpretation

## Course Completion

After completing the capstone, learners should be able to use Bayesian statistics as a full research workflow, not only as a formula or software package.
