# Current Wiring

```text
BME688                    ESP32-S3
------                    --------
VIN    -----------------> 3V3
GND    -----------------> GND
SDI    -----------------> GPIO 8
SCK    -----------------> GPIO 9
```

Unused: `3Vo`, `SDO`, `CS`.

Observed BME688 I2C address: `0x77`.
