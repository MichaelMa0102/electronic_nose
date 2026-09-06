from pathlib import Path
import sys
import pandas as pd
import matplotlib.pyplot as plt

if len(sys.argv) != 2:
    print("Usage: python visualize_trial.py path/to/trial.csv")
    raise SystemExit(1)

path = Path(sys.argv[1])
df = pd.read_csv(path)

time_s = df["elapsed_ms"] / 1000.0

plt.figure()
plt.plot(time_s, df["gas_ohm"])
plt.xlabel("Time (s)")
plt.ylabel("Gas resistance (ohm)")
plt.title(path.name)
plt.tight_layout()
plt.show()
