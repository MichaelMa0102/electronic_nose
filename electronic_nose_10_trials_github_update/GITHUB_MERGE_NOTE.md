# GitHub merge note — orange trials 003–010

This update is designed to merge into the root of:

`MichaelMa0102/electronic_nose`

## Existing files kept in the repository

Trials `orange_001` and `orange_002` are already present in the current GitHub repository and are not duplicated in this update package.

## Files added / updated

- `data/raw/orange_003.csv` through `orange_010.csv`
- `data/processed/orange_003_labeled.csv` through `orange_010_labeled.csv`
- `data/processed/orange_003_summary.csv` through `orange_010_summary.csv`
- `data/processed/orange_trials_comparison.csv` — updated to 10 trials
- `data/processed/orange_trials_10_summary.csv` — richer 10-trial table
- `experiments/004_orange_003.md` through `011_orange_010.md`
- `experiments/012_orange_10_trial_summary.md`
- `figures/orange_10_trials_*.svg` and `.png`
- `ml/analyze_orange_trials.py`
- `README_SNIPPET.md`
- `data/README.md` — expanded dataset notes

## Data-cleaning decisions

- Pre-reboot residual rows were discarded where present.
- Phase labels use the user's recorded exposure times.
- `orange_006` records that the air conditioner was turned off at trial start.
- `orange_008` uses the corrected exposure window `100000–210000 ms`.
- `orange_009` uses `110000–210000 ms`.
- `orange_010` records the qualitative peel-age / movement observation.
- `orange_003` contains only ~23.1 s of pre-exposure baseline because no earlier rows were supplied; nothing was fabricated.

## Regenerate analysis

From the repository root:

```bash
python ml/analyze_orange_trials.py
```

The script expects all ten raw CSVs to be present, including existing `orange_001.csv` and `orange_002.csv`.

## Suggested commit message

`data: add orange peel trials 003-010 and 10-trial summary`
