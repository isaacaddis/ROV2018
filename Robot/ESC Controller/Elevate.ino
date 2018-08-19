#include "Servo.h"

const int InputA0 = A0;
int PotA0 = 0;        // value read from the pot
int SpeedA0 = 0;
const int InputA1 = A1;
int PotA1 = 0;        // value read from the pot
int SpeedA1 = 0;
int outputValue = 0;
String str;

Servo z1;
Servo z2;

void goAbove(int param){
  int percent = abs(param / 10);
  int velocity = percent * 180;
  if(velocity > 150) {
    velocity = 150;  
  }
  z1.write(velocity);
  z2.write(velocity);
  Serial.println("Current Command: Going Up");
}

void goBelow(int param){
  int percent = abs(param / 10);
  int velocity = percent * 180;
  if(velocity > 150) {
    velocity = 150;
  }
  z1.write(velocity * -1);
  z2.write(velocity * -1);
  Serial.println("Current Command: Going Below");
}
void setup() {
  // Begin the Serial at 9600 Baud
z1.attach(9);
z2.attach(10);
delay(500);
Serial.begin(9600);
}


void loop() {
  PotA0 = analogRead(InputA0);
  SpeedA0 = map(PotA0, 0, 1023, 0, 100);
  if(SpeedA0 >= 55 and SpeedA0 <= 100)
  {
    //backwards
    outputValue = map(SpeedA0, 55, 100, 0, -10);
  }
  else if(SpeedA0 >= 0 and SpeedA0 <= 45)
  {
    //forwards
    outputValue = map(SpeedA0, 0, 45, 10, 0);
  }
  else {
     outputValue = 0;
    }
  if(outputValue < 0) {
    goBelow(outputValue);    
  }
  if(outputValue > 0) {
    goAbove(outputValue);    
  }

  str=String(outputValue); 
  //str.toCharArray(mystr, 4);
  Serial.println("Direction: ");
  Serial.println(str);
  delay(100);

}  
