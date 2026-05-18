"""Lab 5: Hierarchical model with partial pooling.

Run:
    python labs/lab05_hierarchical_model.py
"""

from pathlib import Path

import arviz as az
import matplotlib.pyplot as plt
import pandas as pd
import pymc as pm


def main() -> None:
    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)

    data = pd.read_csv("datasets/traffic_wait_times.csv")
    stop_codes, stop_index = pd.factorize(data["stop_id"])

    with pm.Model() as model:
        mu_global = pm.Normal("mu_global", mu=8, sigma=5)
        tau = pm.HalfNormal("tau", sigma=3)
        sigma = pm.HalfNormal("sigma", sigma=3)
        z_stop = pm.Normal("z_stop", mu=0, sigma=1, shape=len(stop_codes))
        mu_stop = pm.Deterministic("mu_stop", mu_global + z_stop * tau)
        pm.Normal("wait_time", mu=mu_stop[stop_index], sigma=sigma, observed=data["wait_min"])
        idata = pm.sample(1000, tune=1000, chains=4, random_seed=11, target_accept=0.9)

    print(az.summary(idata, var_names=["mu_global", "tau", "sigma"]))

    az.plot_forest(idata, var_names=["mu_stop"], combined=True)
    plt.title("Posterior stop-level means with partial pooling")
    plt.tight_layout()
    plt.savefig(output_dir / "lab05_hierarchical_forest.png", dpi=160)


if __name__ == "__main__":
    main()
