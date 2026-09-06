#include <Wire.h>

#define SDA_PIN 8
#define SCL_PIN 9

void setup() {
  Serial.begin(115200);
  delay(2000);
  Serial.println("Starting I2C scanner...");
  Wire.begin(SDA_PIN, SCL_PIN);
}

void loop() {
  byte error;
  int devices = 0;
  Serial.println("Scanning...");

  for (byte address = 1; address < 127; address++) {
    Wire.beginTransmission(address);
    error = Wire.endTransmission();

    if (error == 0) {
      Serial.print("I2C device found at address 0x");
      if (address < 16) Serial.print("0");
      Serial.println(address, HEX);
      devices++;
    }
  }

  if (devices == 0) Serial.println("No I2C devices found.");
  Serial.println();
  delay(3000);
}
