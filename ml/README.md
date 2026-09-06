# Machine Learning

Start with simple baseline models:
- logistic regression
- k-nearest neighbors
- SVM
- random forest

Recommended pipeline:

```text
raw time-series trials
        ↓
quality checks
        ↓
trial-level feature extraction
        ↓
grouped train/test split by trial
        ↓
baseline classifiers
        ↓
confusion matrix + accuracy
        ↓
test on completely unseen trials
```

Possible features:
- baseline gas resistance
- minimum / maximum gas resistance
- relative change from baseline
- exposure slope
- recovery slope
- humidity change
- temperature change
