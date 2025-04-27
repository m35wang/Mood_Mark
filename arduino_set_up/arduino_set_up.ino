#include <Braccio.h>
#include <Servo.h>

Servo base;
Servo shoulder;
Servo elbow;
Servo wrist_rot;
Servo wrist_ver;
Servo gripper;
int speed=20;

int currentPosition[6] = {90, 90, 90, 90, 0, 0};

void setup() { 
  Serial.begin(9600);
  Serial.println("Initializing... Please Wait");

  Braccio.begin();
  Braccio.ServoMovement(speed, currentPosition[0], currentPosition[1], currentPosition[2], currentPosition[3], currentPosition[4], currentPosition[5]);
}

void loop() {
  Serial.println("starting");
  delay(1000);

  int newPosition[7];

  if (Serial.available()) {
    String receivedData = Serial.readStringUntil('\n'); // Read until newline character
    receivedData.trim();   
    
    if (sscanf(receivedData.c_str(), "%d,%d,%d,%d,%d,%d,%d", &newPosition[0], &newPosition[1], &newPosition[2], &newPosition[3], &newPosition[4], &newPosition[5], &newPosition[6]) == 7) {
      // Move the arm to the new position immediately
      speed=newPosition[6];
      Serial.println("this is a new position" + newPosition[1]);
      
      Braccio.ServoMovement(speed,newPosition[0], newPosition[1], newPosition[2], newPosition[3], newPosition[4], newPosition[5]);

      for (int i = 0; i < 7; i++) {
        currentPosition[i] = newPosition[i];
      }
      Serial.print("Moved to new position: ");

       // Clear the serial buffer
      while (Serial.available() > 0) {
        Serial.read();
      }
  } else {
      Serial.println("Error: Invalid data format. Expected six integers separated by commas.");
  }
}
}
