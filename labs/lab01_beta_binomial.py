"""Lab 1: Beta-binomial Bayesian updating.

Run:
    python labs/lab01_beta_binomial.py
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import beta


def summarize(draws: np.ndarray, threshold: float = 0.70) -> dict:
    return {
        "mean": float(np.mean(draws)),
        "median": float(np.median(draws)),
        "ci_2_5": float(np.quantile(draws, 0.025)),
        "ci_97_5": float(np.quantile(draws, 0.975)),
        f"prob_gt_{threshold}": float(np.mean(draws > threshold)),
    }


def main() -> None:
    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)

    prior_alpha = 2
    prior_beta = 2
    successes = 30
    trials = 40
    failures = trials - successes

    posterior_alpha = prior_alpha + successes
    posterior_beta = prior_beta + failures

    rng = np.random.default_rng(42)
    posterior_draws = rng.beta(posterior_alpha, posterior_beta, size=20_000)
    summary = summarize(posterior_draws)

    print("Beta-binomial updating")
    print(f"Prior: Beta({prior_alpha}, {prior_beta})")
    print(f"Data: {successes} successes out of {trials}")
    print(f"Posterior: Beta({posterior_alpha}, {posterior_beta})")
    print(summary)

    x = np.linspace(0, 1, 500)
    plt.figure(figsize=(9, 5))
    plt.plot(x, beta.pdf(x, prior_alpha, prior_beta), label="Prior", linewidth=2)
    plt.plot(x, beta.pdf(x, posterior_alpha, posterior_beta), label="Posterior", linewidth=2)
    plt.axvline(0.70, color="black", linestyle="--", linewidth=1, label="Practical threshold")
    plt.title("Beta-binomial Bayesian updating")
    plt.xlabel("Reliability probability")
    plt.ylabel("Density")
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_dir / "lab01_beta_binomial.png", dpi=160)


if __name__ == "__main__":
    main()
