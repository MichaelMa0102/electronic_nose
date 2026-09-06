# Experiment 001 — Hardware Bring-up

## Goal
Verify ESP32-S3 communication with the BME688.

## Results
- ESP32 programmed successfully from Arduino IDE
- BME688 detected over I2C
- Address observed: `0x77`
- Temperature, humidity, pressure and gas resistance readings work

## Observation
Gas resistance increased after startup even without intentionally presenting an odor. Future experiments should include a defined warm-up period.

## Next Step
Establish a repeatable clean-air baseline procedure.
