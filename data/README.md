# Dataset

- `raw/`: original captured measurements; never edit manually
- `processed/`: cleaned or transformed data
- `examples/`: small example files safe to commit

Suggested columns:

```text
elapsed_ms,temp_c,humidity_pct,pressure_hpa,gas_ohm,label,trial_id,phase
```

Suggested phases: `purge`, `baseline`, `exposure`, `recovery`.

## Critical ML rule

Training, validation, and test splits should happen at the **trial level**, not by randomly mixing rows from the same trial.
