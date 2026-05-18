"""Lab 2: Normal-normal Bayesian updating.

This lab assumes the observation standard deviation is known.

Run:
    python labs/lab02_normal_normal.py
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm


def normal_normal_update(mu0: float, tau0: float, sigma: float, data: np.ndarray) -> tuple[float, float]:
    n = len(data)
    ybar = float(np.mean(data))
    prior_precision = 1 / tau0**2
    data_precision = n / sigma**2
    posterior_variance = 1 / (prior_precision + data_precision)
    posterior_mean = posterior_variance * (mu0 * prior_precision + n * ybar / sigma**2)
    posterior_sd = float(np.sqrt(posterior_variance))
    return float(posterior_mean), posterior_sd


def main() -> None:
    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)

    data = np.array([7.5, 8.2, 6.9, 9.1, 7.8, 8.5, 7.2, 8.0, 8.7, 7.9])

    mu0 = 10.0
    tau0 = 3.0
    sigma = 1.2

    posterior_mean, posterior_sd = normal_normal_update(mu0, tau0, sigma, data)

    print("Normal-normal updating")
    print(f"Sample mean: {np.mean(data):.3f}")
    print(f"Prior mean: {mu0:.3f}, prior sd: {tau0:.3f}")
    print(f"Posterior mean: {posterior_mean:.3f}, posterior sd: {posterior_sd:.3f}")
    print(f"95% credible interval: {norm.ppf(0.025, posterior_mean, posterior_sd):.3f}, {norm.ppf(0.975, posterior_mean, posterior_sd):.3f}")

    x = np.linspace(4, 14, 600)
    plt.figure(figsize=(9, 5))
    plt.plot(x, norm.pdf(x, mu0, tau0), label="Prior", linewidth=2)
    plt.plot(x, norm.pdf(x, posterior_mean, posterior_sd), label="Posterior", linewidth=2)
    plt.axvline(np.mean(data), color="black", linestyle="--", linewidth=1, label="Sample mean")
    plt.title("Normal-normal Bayesian updating")
    plt.xlabel("Mean waiting time")
    plt.ylabel("Density")
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_dir / "lab02_normal_normal.png", dpi=160)


if __name__ == "__main__":
    main()
