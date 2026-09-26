#!/usr/bin/env python3
"""
Recompute the 10-trial orange-peel summary from raw CSV files.

Run from the repository root:
    python ml/analyze_orange_trials.py

Outputs:
    data/processed/orange_trials_10_summary.csv
    data/processed/orange_trials_comparison.csv
    figures/orange_10_trials_gas_drop.svg
    figures/orange_10_trials_humidity_delta.svg
    figures/orange_10_trials_baseline_vs_min.svg

Important:
- Trial 002 has an uncertain placement time; the stable baseline window follows the
  existing experiment note (60-110 s), while exposure is treated as 120-230 s.
- Trial 003 only has ~23 s of pre-exposure data in the supplied segment.
- Do not split individual rows from one trial across train/test sets.
"""

from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
PROCESSED = ROOT / "data" / "processed"
FIGURES = ROOT / "figures"

CONFIG = {
    "orange_001": dict(exposure=(70000, 140000), baseline=(30000, 65000),
                       timing="manual interval recorded (70-140 s)", note=""),
    "orange_002": dict(exposure=(120000, 230000), baseline=(60000, 110000),
                       timing="placement ~120 s uncertain; sensor transition starts ~111.258 s; removal ~230 s", note=""),
    "orange_003": dict(exposure=(300000, 400000), baseline=None,
                       timing="manual interval recorded (300-400 s); only ~23.1 s pre-exposure data supplied", note=""),
    "orange_004": dict(exposure=(100000, 210000), baseline=(50000, 90000),
                       timing="manual interval recorded (100-210 s)", note=""),
    "orange_005": dict(exposure=(100000, 210000), baseline=(50000, 90000),
                       timing="manual interval recorded (100-210 s)", note=""),
    "orange_006": dict(exposure=(100000, 200000), baseline=(50000, 90000),
                       timing="manual interval recorded (100-200 s)", note="AC turned off at trial start"),
    "orange_007": dict(exposure=(100000, 200000), baseline=(50000, 90000),
                       timing="manual interval recorded (100-200 s)", note=""),
    "orange_008": dict(exposure=(100000, 210000), baseline=(50000, 90000),
                       timing="manual interval recorded (100-210 s)", note="large humidity excursion during exposure"),
    "orange_009": dict(exposure=(110000, 210000), baseline=(60000, 100000),
                       timing="manual interval recorded (110-210 s)", note="one pre-reboot residual row discarded"),
    "orange_010": dict(exposure=(100000, 200000), baseline=(50000, 90000),
                       timing="manual interval recorded (100-200 s)",
                       note="one pre-reboot residual row discarded; peel-age/motion observation recorded in experiment note"),
}


def summarize(trial_id: str, df: pd.DataFrame, cfg: dict) -> dict:
    start, end = cfg["exposure"]

    if cfg["baseline"] is None:
        baseline = df[df["elapsed_ms"] < start].copy()
        b_start = int(baseline["elapsed_ms"].min())
        b_end = start
    else:
        b_start, b_end = cfg["baseline"]
        baseline = df[(df["elapsed_ms"] >= b_start) & (df["elapsed_ms"] < b_end)].copy()

    exposure = df[(df["elapsed_ms"] >= start) & (df["elapsed_ms"] <= end)].copy()
    recovery = df[df["elapsed_ms"] > end].copy()

    if baseline.empty or exposure.empty:
        raise ValueError(f"{trial_id}: missing baseline or exposure rows")

    baseline_mean = baseline["gas_ohm"].mean()
    baseline_sd = baseline["gas_ohm"].std(ddof=1)
    baseline_cv = baseline_sd / baseline_mean * 100.0

    min_idx = exposure["gas_ohm"].idxmin()
    min_row = exposure.loc[min_idx]
    gas_drop = (baseline_mean - min_row["gas_ohm"]) / baseline_mean * 100.0

    baseline_h = baseline["humidity_pct"].mean()
    peak_h_idx = exposure["humidity_pct"].idxmax()
    peak_h_row = exposure.loc[peak_h_idx]
    humidity_increase = peak_h_row["humidity_pct"] - baseline_h

    if recovery.empty:
        late_mean = np.nan
        recovery_fraction = np.nan
    else:
        final_start = max(end, int(df["elapsed_ms"].max()) - 60000)
        late = recovery[recovery["elapsed_ms"] >= final_start]
        late_mean = late["gas_ohm"].mean()
        denom = baseline_mean - min_row["gas_ohm"]
        recovery_fraction = ((late_mean - min_row["gas_ohm"]) / denom * 100.0
                             if denom != 0 else np.nan)

    return {
        "trial_id": trial_id,
        "samples": len(df),
        "exposure_start_ms": start,
        "exposure_end_ms": end,
        "baseline_window_start_ms": b_start,
        "baseline_window_end_ms": b_end,
        "baseline_gas_mean_ohm": baseline_mean,
        "baseline_gas_std_ohm": baseline_sd,
        "baseline_gas_cv_pct": baseline_cv,
        "min_gas_ohm": min_row["gas_ohm"],
        "min_gas_time_ms": int(min_row["elapsed_ms"]),
        "gas_drop_pct": gas_drop,
        "baseline_humidity_pct": baseline_h,
        "peak_humidity_pct": peak_h_row["humidity_pct"],
        "peak_humidity_time_ms": int(peak_h_row["elapsed_ms"]),
        "humidity_increase_pp": humidity_increase,
        "late_recovery_gas_ohm": late_mean,
        "recovery_fraction_pct": recovery_fraction,
        "timing_quality": cfg["timing"],
        "environment_note": cfg["note"],
    }


def save_figures(summary: pd.DataFrame) -> None:
    FIGURES.mkdir(parents=True, exist_ok=True)
    labels = [x[-3:] for x in summary["trial_id"]]

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(labels, summary["gas_drop_pct"])
    ax.set_title("Orange peel: gas-resistance drop by trial")
    ax.set_xlabel("Trial")
    ax.set_ylabel("Drop from baseline (%)")
    ax.set_ylim(0, 100)
    ax.grid(axis="y", alpha=0.25)
    fig.tight_layout()
    fig.savefig(FIGURES / "orange_10_trials_gas_drop.svg")
    fig.savefig(FIGURES / "orange_10_trials_gas_drop.png", dpi=180)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(labels, summary["humidity_increase_pp"])
    ax.set_title("Orange peel: humidity increase by trial")
    ax.set_xlabel("Trial")
    ax.set_ylabel("Humidity increase (percentage points)")
    ax.grid(axis="y", alpha=0.25)
    fig.tight_layout()
    fig.savefig(FIGURES / "orange_10_trials_humidity_delta.svg")
    fig.savefig(FIGURES / "orange_10_trials_humidity_delta.png", dpi=180)
    plt.close(fig)

    x = np.arange(len(labels))
    width = 0.38
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(x - width / 2, summary["baseline_gas_mean_ohm"] / 1000.0, width, label="Baseline")
    ax.bar(x + width / 2, summary["min_gas_ohm"] / 1000.0, width, label="Exposure minimum")
    ax.set_xticks(x, labels)
    ax.set_title("Orange peel: baseline vs exposure minimum")
    ax.set_xlabel("Trial")
    ax.set_ylabel("Gas resistance (kOhm)")
    ax.legend()
    ax.grid(axis="y", alpha=0.25)
    fig.tight_layout()
    fig.savefig(FIGURES / "orange_10_trials_baseline_vs_min.svg")
    fig.savefig(FIGURES / "orange_10_trials_baseline_vs_min.png", dpi=180)
    plt.close(fig)


def main() -> None:
    rows = []
    for trial_id, cfg in CONFIG.items():
        path = RAW / f"{trial_id}.csv"
        if not path.exists():
            raise FileNotFoundError(f"Missing {path}")
        df = pd.read_csv(path)
        rows.append(summarize(trial_id, df, cfg))

    summary = pd.DataFrame(rows)
    PROCESSED.mkdir(parents=True, exist_ok=True)
    summary.to_csv(PROCESSED / "orange_trials_10_summary.csv", index=False)

    comparison_cols = [
        "trial_id",
        "baseline_gas_mean_ohm",
        "baseline_gas_cv_pct",
        "min_gas_ohm",
        "gas_drop_pct",
        "baseline_humidity_pct",
        "peak_humidity_pct",
        "humidity_increase_pp",
        "late_recovery_gas_ohm",
        "timing_quality",
    ]
    summary[comparison_cols].to_csv(PROCESSED / "orange_trials_comparison.csv", index=False)
    save_figures(summary)

    print(summary[[
        "trial_id", "baseline_gas_mean_ohm", "min_gas_ohm",
        "gas_drop_pct", "humidity_increase_pp"
    ]].to_string(index=False))


if __name__ == "__main__":
    main()
