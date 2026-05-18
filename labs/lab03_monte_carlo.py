"""Lab 3: Monte Carlo posterior summaries.

Run:
    python labs/lab03_monte_carlo.py
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def posterior_summary(draws: np.ndarray) -> dict:
    return {
        "mean": float(np.mean(draws)),
        "sd": float(np.std(draws, ddof=1)),
        "q05": float(np.quantile(draws, 0.05)),
        "q50": float(np.quantile(draws, 0.50)),
        "q95": float(np.quantile(draws, 0.95)),
        "prob_gt_0_60": float(np.mean(draws > 0.60)),
    }


def main() -> None:
    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)

    rng = np.random.default_rng(123)
    draws_1k = rng.beta(18, 12, size=1_000)
    draws_50k = rng.beta(18, 12, size=50_000)

    print("Monte Carlo comparison")
    print("1,000 draws:", posterior_summary(draws_1k))
    print("50,000 draws:", posterior_summary(draws_50k))

    plt.figure(figsize=(9, 5))
    plt.hist(draws_50k, bins=60, density=True, alpha=0.75, color="#2563eb")
    plt.axvline(0.60, color="black", linestyle="--", linewidth=1)
    plt.title("Monte Carlo draws from posterior Beta(18, 12)")
    plt.xlabel("Parameter value")
    plt.ylabel("Density")
    plt.tight_layout()
    plt.savefig(output_dir / "lab03_monte_carlo.png", dpi=160)


if __name__ == "__main__":
    main()
