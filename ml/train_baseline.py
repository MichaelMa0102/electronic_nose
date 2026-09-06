from pathlib import Path
import sys
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import GroupShuffleSplit

if len(sys.argv) != 2:
    print("Usage: python train_baseline.py path/to/trial_features.csv")
    raise SystemExit(1)

df = pd.read_csv(Path(sys.argv[1]))

required = {"label", "trial_id"}
missing = required - set(df.columns)
if missing:
    raise ValueError(f"Missing columns: {sorted(missing)}")

feature_cols = [
    c for c in df.columns
    if c not in {"label", "trial_id"}
    and pd.api.types.is_numeric_dtype(df[c])
]

X = df[feature_cols]
y = df["label"]
groups = df["trial_id"]

splitter = GroupShuffleSplit(n_splits=1, test_size=0.25, random_state=42)
train_idx, test_idx = next(splitter.split(X, y, groups))

model = RandomForestClassifier(n_estimators=300, random_state=42)
model.fit(X.iloc[train_idx], y.iloc[train_idx])

pred = model.predict(X.iloc[test_idx])

print("Features:", feature_cols)
print("\\nConfusion matrix:")
print(confusion_matrix(y.iloc[test_idx], pred))
print("\\nClassification report:")
print(classification_report(y.iloc[test_idx], pred))
