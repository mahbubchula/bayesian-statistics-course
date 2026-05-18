"""Lab 4: MCMC diagnostics with PyMC and ArviZ.

Run:
    python labs/lab04_mcmc_diagnostics.py
"""

from pathlib import Path

import arviz as az
import matplotlib.pyplot as plt
import numpy as np
import pymc as pm


def main() -> None:
    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)

    rng = np.random.default_rng(7)
    observed = rng.normal(loc=8.0, scale=1.5, size=80)

    with pm.Model() as model:
        mu = pm.Normal("mu", mu=10, sigma=5)
        sigma = pm.HalfNormal("sigma", sigma=3)
        pm.Normal("wait_time", mu=mu, sigma=sigma, observed=observed)
        idata = pm.sample(1000, tune=1000, chains=4, random_seed=7, target_accept=0.9)

    print(az.summary(idata, var_names=["mu", "sigma"]))

    az.plot_trace(idata, var_names=["mu", "sigma"])
    plt.tight_layout()
    plt.savefig(output_dir / "lab04_trace.png", dpi=160)

    az.plot_posterior(idata, var_names=["mu", "sigma"])
    plt.tight_layout()
    plt.savefig(output_dir / "lab04_posterior.png", dpi=160)


if __name__ == "__main__":
    main()
