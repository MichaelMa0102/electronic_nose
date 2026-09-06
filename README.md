# Electronic Nose

A beginner-friendly experimental electronic nose based on an ESP32-S3 and Bosch BME688.

## Goal

### Version 1
Recognize a small set of known odors from BME688 response patterns using machine learning.

Initial target classes:
- Clean air
- Coffee
- Orange
- Peppermint

### Version 2 — Long-term research direction
Analyze an odor at one location, transmit a digital odor representation, and reconstruct a perceptually similar smell at another location using a controlled scent generator.

> Version 2 is a much harder research problem. This repository currently focuses on Version 1.

## Current Hardware

- ESP32-S3-N16R8
- BME688 breakout
- I2C connection
- SDA: GPIO 8
- SCL: GPIO 9
- BME688 I2C address observed: `0x77`

## Wiring

| BME688 | ESP32-S3 | Purpose |
|---|---|---|
| VIN | 3V3 | Power |
| GND | GND | Ground |
| SDI | GPIO 8 | I2C SDA |
| SCK | GPIO 9 | I2C SCL |

Leave `3Vo`, `SDO`, and `CS` unconnected for the current I2C setup.

## Current Status

- [x] Select ESP32-S3 and BME688
- [x] Solder BME688 header
- [x] Verify no obvious VIN-GND short
- [x] Connect BME688 to ESP32-S3
- [x] Upload code to ESP32
- [x] Detect BME688 over I2C at `0x77`
- [x] Read temperature, humidity, pressure, gas resistance
- [ ] Establish stable clean-air baseline
- [ ] Implement structured CSV logging
- [ ] Define repeatable odor sampling protocol
- [ ] Collect multi-trial dataset
- [ ] Visualize response curves
- [ ] Train first classifier
- [ ] Evaluate classifier on unseen trials
- [ ] Build real-time Version 1 demo

## Important ML Rule

Do **not** randomly split individual time samples from the same trial into both training and test data.

The model must be tested on entire trials it has never seen before. Otherwise accuracy can look much better than real-world performance.

## Safety

Avoid exposing the sensor to flammable solvent vapors, unknown chemicals, corrosive gases, toxic substances, or very high VOC concentrations. Do not touch or contaminate the BME688 sensing area.

## License

No license has been selected yet. Add one before publishing if you want others to reuse the project.
