# Bayesian Statistics: From Foundations to Research Applications

Complete open course for students, researchers, and applied data scientists who want to learn Bayesian statistics from first principles and use it in real research workflows.

This course is designed by Mahbub Hassan for self-study, classroom teaching, and research-lab training. It emphasizes intuition, mathematical reasoning, computational practice, and reproducible applied analysis.

## Course Goals

By the end of this course, learners should be able to:

- Explain Bayesian thinking using priors, likelihoods, posteriors, and posterior predictive distributions.
- Build conjugate Bayesian models for proportions, rates, means, and uncertainty estimation.
- Use Monte Carlo simulation and Markov chain Monte Carlo for models without closed-form solutions.
- Fit Bayesian regression and hierarchical models with Python.
- Diagnose convergence, interpret uncertainty, and communicate posterior results clearly.
- Compare models using predictive checks and information criteria.
- Design a complete Bayesian research project from problem statement to final report.

## Who This Course Is For

- Undergraduate and graduate students in statistics, engineering, transportation, economics, public health, social science, and data science.
- Researchers who use quantitative methods and want stronger uncertainty reasoning.
- Machine learning practitioners who want probabilistic modeling skills.
- Students preparing for thesis, journal paper, or research assistant work.

## Recommended Background

Learners should know basic algebra, probability, and Python. Prior exposure to regression helps, but the course reviews the needed foundations.

## Course Structure

| Week | Module | Main Outcome |
|---|---|---|
| 1 | [Bayesian Thinking](modules/01-bayesian-thinking.md) | Understand Bayesian reasoning and uncertainty |
| 2 | [Probability Review](modules/02-probability-review.md) | Use probability rules needed for Bayesian modeling |
| 3 | [Priors, Likelihoods, and Posteriors](modules/03-priors-likelihood-posteriors.md) | Translate research questions into Bayesian models |
| 4 | [Conjugate Models](modules/04-conjugate-models.md) | Solve beta-binomial, gamma-Poisson, and normal models |
| 5 | [Monte Carlo Computation](modules/05-computation-monte-carlo.md) | Approximate posterior quantities with simulation |
| 6 | [MCMC](modules/06-mcmc.md) | Understand sampling, chains, diagnostics, and convergence |
| 7 | [Hierarchical Models](modules/07-hierarchical-models.md) | Model grouped data with partial pooling |
| 8 | [Bayesian Regression](modules/08-bayesian-regression.md) | Fit linear, logistic, and count regression models |
| 9 | [Model Checking and Comparison](modules/09-model-checking-comparison.md) | Evaluate models with posterior predictive checks |
| 10 | [Decision Analysis](modules/10-bayesian-decision-analysis.md) | Connect posterior inference to decisions |
| 11 | [Causal and Time-Series Extensions](modules/11-causal-and-time-series.md) | Extend Bayesian thinking to advanced applied questions |
| 12 | [Capstone Workflow](modules/12-capstone-research-workflow.md) | Complete a reproducible Bayesian research project |

## Labs

| Lab | Topic | File |
|---|---|---|
| 1 | Beta-binomial updating | [lab01_beta_binomial.py](labs/lab01_beta_binomial.py) |
| 2 | Normal-normal updating | [lab02_normal_normal.py](labs/lab02_normal_normal.py) |
| 3 | Monte Carlo integration | [lab03_monte_carlo.py](labs/lab03_monte_carlo.py) |
| 4 | MCMC diagnostics | [lab04_mcmc_diagnostics.py](labs/lab04_mcmc_diagnostics.py) |
| 5 | Hierarchical modeling | [lab05_hierarchical_model.py](labs/lab05_hierarchical_model.py) |
| 6 | Bayesian regression workflow | [lab06_bayesian_regression.py](labs/lab06_bayesian_regression.py) |

## Assignments

- [Assignment 1: Bayesian Foundations](assignments/assignment01-foundations.md)
- [Assignment 2: Conjugate Modeling](assignments/assignment02-conjugate-models.md)
- [Assignment 3: Monte Carlo and MCMC](assignments/assignment03-mcmc.md)
- [Assignment 4: Hierarchical Regression](assignments/assignment04-hierarchical-regression.md)
- [Capstone Project](assignments/capstone-project.md)

## Quick Start

Clone the repository:

```bash
git clone https://github.com/mahbubchula/bayesian-statistics-course.git
cd bayesian-statistics-course
```

Create a Python environment:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Run a lab:

```bash
python labs/lab01_beta_binomial.py
```

## Software

Core tools:

- Python
- NumPy
- pandas
- SciPy
- Matplotlib
- ArviZ
- PyMC

PyMC is used for applied Bayesian modeling. The early modules are written so learners can understand the statistics before relying on software.

## Datasets

Small teaching datasets are included in the `datasets` folder:

- `coin_quality.csv`: binary quality-control data for beta-binomial modeling
- `traffic_wait_times.csv`: waiting-time data for normal and hierarchical models
- `ev_adoption_sample.csv`: simple applied dataset for Bayesian regression

These datasets are synthetic teaching data and should not be interpreted as real-world measurements.

## Suggested Teaching Format

For a 12-week course:

- 1 lecture per week
- 1 lab or tutorial per week
- 4 graded assignments
- 1 final capstone project

For a short workshop:

- Day 1: Modules 1 to 4
- Day 2: Modules 5 to 8
- Day 3: Modules 9 to 12 and capstone planning

## Repository Map

```text
bayesian-statistics-course/
  README.md
  syllabus.md
  index.html
  requirements.txt
  modules/
  labs/
  assignments/
  datasets/
  slides/
  assets/
```

## Citation

If you use this course in teaching or training, please cite the repository:

Mahbub Hassan. Bayesian Statistics: From Foundations to Research Applications. GitHub repository, 2026.

## License

Course text, assignments, and teaching materials are released under the Creative Commons Attribution 4.0 International License. Code examples are released under the MIT License.
