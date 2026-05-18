# Module 6: Markov Chain Monte Carlo

## Purpose

Markov chain Monte Carlo, or MCMC, is the standard computational engine behind many Bayesian models.

## Learning Objectives

After this module, learners should be able to:

- Explain why MCMC is needed.
- Describe a Markov chain at a conceptual level.
- Interpret trace plots, R-hat, and effective sample size.
- Identify common sampling problems.

## Why MCMC?

For complex models, the posterior distribution may not have a closed-form solution. We may know the posterior only up to proportionality:

```text
posterior proportional to likelihood times prior
```

MCMC constructs a chain of samples that, after warm-up, behaves like draws from the posterior distribution.

## Markov Chain Intuition

A Markov chain is a sequence where the next state depends on the current state. In MCMC, the chain moves around the parameter space and spends more time in regions with high posterior probability.

## Modern MCMC

Many Bayesian tools use Hamiltonian Monte Carlo and the No-U-Turn Sampler. These methods use gradient information to explore the posterior efficiently.

Learners do not need to implement these methods from scratch, but they must understand diagnostics.

## Key Diagnostics

| Diagnostic | Meaning | Desired Pattern |
|---|---|---|
| Trace plot | Chain movement over iterations | Stable mixing, no trends |
| R-hat | Agreement between chains | Close to 1.00 |
| Effective sample size | Independent information in draws | Larger is better |
| Divergences | Sampling geometry problem | Zero or carefully resolved |
| Energy plot | HMC exploration quality | No major mismatch |

## Common Problems

### Poor Mixing

Chains move slowly and do not explore the posterior well.

Possible responses:

- Reparameterize the model.
- Standardize predictors.
- Use stronger regularizing priors.
- Run longer chains only after model geometry is reasonable.

### Divergences

Divergences suggest the sampler is struggling with posterior geometry.

Possible responses:

- Reparameterize hierarchical models.
- Use non-centered parameterization.
- Increase target acceptance.
- Check priors and scale.

### Too Little Effective Sample Size

Posterior summaries may be noisy.

Possible responses:

- Run more draws.
- Improve parameterization.
- Simplify the model if necessary.

## Reporting MCMC Results

A good Bayesian report includes:

- Number of chains
- Warm-up and posterior draws
- R-hat values
- Effective sample sizes
- Divergence count
- Posterior summaries
- Posterior predictive checks

## Practice

1. Explain why four chains are better than one chain.
2. What does R-hat close to 1 suggest?
3. Why can a model with many divergences produce misleading results?
4. In one paragraph, explain MCMC to a non-statistician.

## Lab

Complete [Lab 4: MCMC diagnostics](../labs/lab04_mcmc_diagnostics.py).

## Assignment

Start [Assignment 3: Monte Carlo and MCMC](../assignments/assignment03-mcmc.md).

## Next Module

Continue to [Module 7: Hierarchical Models](07-hierarchical-models.md).
