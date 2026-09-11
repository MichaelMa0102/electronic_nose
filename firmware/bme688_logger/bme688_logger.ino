#include <Wire.h>
#include <Adafruit_Sensor.h>
#include "Adafruit_BME680.h"

#define SDA_PIN 8
#define SCL_PIN 9
#define BME_ADDR 0x77

Adafruit_BME680 bme;

unsigned long startMs = 0;

void setup() {
  Serial.begin(115200);
  delay(2000);

  Wire.begin(SDA_PIN, SCL_PIN);

  if (!bme.begin(BME_ADDR, &Wire)) {
    Serial.println("# ERROR: BME688 not found");
    while (1) {
      delay(1000);
    }
  }

  bme.setTemperatureOversampling(BME680_OS_8X);
  bme.setHumidityOversampling(BME680_OS_2X);
  bme.setPressureOversampling(BME680_OS_4X);
  bme.setIIRFilterSize(BME680_FILTER_SIZE_3);
  bme.setGasHeater(320, 150);

  startMs = millis();

  Serial.println("elapsed_ms,temp_c,humidity_pct,pressure_hpa,gas_ohm");
}

void loop() {
  if (!bme.performReading()) {
    Serial.println("# WARNING: reading failed");
    delay(1000);
    return;
  }

  unsigned long elapsed = millis() - startMs;

  Serial.print(elapsed);
  Serial.print(",");
  Serial.print(bme.temperature, 3);
  Serial.print(",");
  Serial.print(bme.humidity, 3);
  Serial.print(",");
  Serial.print(bme.pressure / 100.0, 3);
  Serial.print(",");
  Serial.println(bme.gas_resistance);

  delay(1000);
}
