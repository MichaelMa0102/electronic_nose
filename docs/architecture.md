# Architecture

## Version 1

```text
Odor sample
    ↓
Controlled sampling / chamber
    ↓
BME688
    ↓ I2C
ESP32-S3
    ↓
Raw time-series measurements
    ↓
Feature extraction
    ↓
ML classifier
    ↓
Predicted odor class + confidence
```

Development priority:
1. repeatable sampling
2. trustworthy dataset
3. unseen-trial evaluation
4. real-time classification
5. custom PCB / enclosure

## Version 2 Research Direction

```text
Original odor
    ↓
sensor system
    ↓
odor representation
    ↓ network
scent reconstruction system
    ↓
reproduced odor
```

A constrained odor vocabulary and controlled scent cartridges are a more realistic intermediate target than arbitrary odor reconstruction.
