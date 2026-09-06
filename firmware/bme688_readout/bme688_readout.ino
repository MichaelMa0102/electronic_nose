#include <Wire.h>
#include <Adafruit_Sensor.h>
#include "Adafruit_BME680.h"

#define SDA_PIN 8
#define SCL_PIN 9
#define BME_ADDR 0x77

Adafruit_BME680 bme;

void setup() {
  Serial.begin(115200);
  delay(2000);
  Wire.begin(SDA_PIN, SCL_PIN);

  if (!bme.begin(BME_ADDR, &Wire)) {
    Serial.println("Could not find BME688.");
    while (1) delay(1000);
  }

  bme.setTemperatureOversampling(BME680_OS_8X);
  bme.setHumidityOversampling(BME680_OS_2X);
  bme.setPressureOversampling(BME680_OS_4X);
  bme.setIIRFilterSize(BME680_FILTER_SIZE_3);
  bme.setGasHeater(320, 150);

  Serial.println("BME688 found.");
}

void loop() {
  if (!bme.performReading()) {
    Serial.println("Reading failed.");
    delay(1000);
    return;
  }

  Serial.print("Temperature: ");
  Serial.print(bme.temperature);
  Serial.println(" C");

  Serial.print("Humidity: ");
  Serial.print(bme.humidity);
  Serial.println(" %");

  Serial.print("Pressure: ");
  Serial.print(bme.pressure / 100.0);
  Serial.println(" hPa");

  Serial.print("Gas resistance: ");
  Serial.print(bme.gas_resistance / 1000.0);
  Serial.println(" kOhm");

  Serial.println("---------------------");
  delay(2000);
}
