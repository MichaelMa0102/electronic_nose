# Dataset

- `raw/`: original captured measurements; never edit manually
- `processed/`: cleaned, labeled, or summarized data
- `examples/`: small example files safe to commit

Raw logger columns:

```text
elapsed_ms,temp_c,humidity_pct,pressure_hpa,gas_ohm
```

Labeled trial columns:

```text
trial_id,label,phase,elapsed_ms,temp_c,humidity_pct,pressure_hpa,gas_ohm
```

Suggested phases: `purge`, `baseline`, `exposure`, `recovery`.

## Orange-peel dataset

The current milestone contains 10 independent orange-peel trials:

```text
orange_001 ... orange_010
```

The exposure timing was recorded manually and is not identical across all trials. See the matching file in `experiments/` and `data/processed/orange_trials_10_summary.csv`.

Important data-quality notes:

- `orange_002`: physical placement time was uncertain; the existing experiment note records the transition.
- `orange_003`: only about 23.1 s of pre-exposure data was supplied.
- `orange_006`: air conditioner was turned off at trial start.
- `orange_008`: large humidity excursion during exposure.
- `orange_009` and `orange_010`: a residual pre-reboot row was discarded.
- Never silently remove a trial simply because its response looks unusual. Keep the observation and record the condition.

## Critical ML rule

Training, validation, and test splits must happen at the **trial level**, not by randomly mixing rows from the same trial.

The current 10-trial orange dataset is still only **one odor class**. Before claiming classification performance, collect contrasting classes (for example clean-air/sham trials and another odor) under the same controlled protocol.
