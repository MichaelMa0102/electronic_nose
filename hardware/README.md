# Hardware

## Current Prototype
- ESP32-S3-N16R8
- BME688 breakout
- Breadboard
- Dupont jumper wires
- USB data cable

## Wiring

| Signal | BME688 | ESP32-S3 |
|---|---|---|
| 3.3 V | VIN | 3V3 |
| Ground | GND | GND |
| I2C SDA | SDI | GPIO 8 |
| I2C SCL | SCK | GPIO 9 |

Do not add a custom PCB, battery, display, or enclosure until the sensing and classification pipeline is demonstrated reliably.
