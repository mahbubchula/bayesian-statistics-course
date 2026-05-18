"""Lab 6: Bayesian logistic regression for EV adoption.

Run:
    python labs/lab06_bayesian_regression.py
"""

from pathlib import Path

import arviz as az
import matplotlib.pyplot as plt
import pandas as pd
import pymc as pm


def standardize(series: pd.Series) -> pd.Series:
    return (series - series.mean()) / series.std(ddof=0)


def main() -> None:
    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)

    data = pd.read_csv("datasets/ev_adoption_sample.csv")
    data["income_z"] = standardize(data["income_k"])
    data["commute_z"] = standardize(data["commute_km"])

    with pm.Model() as model:
        alpha = pm.Normal("alpha", mu=0, sigma=2)
        beta_income = pm.Normal("beta_income", mu=0, sigma=1)
        beta_commute = pm.Normal("beta_commute", mu=0, sigma=1)
        beta_charger = pm.Normal("beta_charger", mu=0, sigma=1)

        logit_p = (
            alpha
            + beta_income * data["income_z"].to_numpy()
            + beta_commute * data["commute_z"].to_numpy()
            + beta_charger * data["charger_access"].to_numpy()
        )
        pm.Bernoulli("adopted_ev", logit_p=logit_p, observed=data["adopted_ev"].to_numpy())
        idata = pm.sample(1000, tune=1000, chains=4, random_seed=21, target_accept=0.9)

    print(az.summary(idata, var_names=["alpha", "beta_income", "beta_commute", "beta_charger"]))

    az.plot_posterior(idata, var_names=["beta_income", "beta_commute", "beta_charger"])
    plt.tight_layout()
    plt.savefig(output_dir / "lab06_regression_coefficients.png", dpi=160)


if __name__ == "__main__":
    main()
