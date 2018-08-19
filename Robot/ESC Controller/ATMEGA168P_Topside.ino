#include "Servo.h"

const int InputA0 = A0;
int PotA0 = 0;        // value read from the pot
int SpeedA0 = 0;
const int InputA1 = A1;
int PotA1 = 0;        // value read from the pot
int SpeedA1 = 0;
int outputValueX = 0;
int outputValueY = 0;
int n = 0;
String str1;
String str2;

Servo f_Left;
Servo f_Right;
Servo b_Left;
Servo b_Right;

void goForward(int param) {
  int percent = abs(param / 10);
  int velocity = percent * 180;
  if(velocity > 150) {
    velocity = 150;
  }
  f_Left.write(velocity * -1);
  f_Right.write(velocity * -1);
  b_Left.write(velocity * -1);
  b_Right.write(velocity * -1);

  Serial.println("Current Command: Move Forward");
  Serial.println(" ");
}

void goBackward(int param) {
  int percent = abs(param / 10);
  int velocity = percent * 180;
  if(velocity > 150) {
    velocity = 150;
  }
  f_Left.write(velocity);
  f_Right.write(velocity);
  b_Left.write(velocity);
  b_Right.write(velocity);

  Serial.println("Current Command: Move Backward");
  Serial.println(" ");
}

void goLeft(int param) {
  int percent = abs(param/10);
  int velocity = percent * 180;
  if(velocity > 150) {
    velocity = 150;
  }
  f_Left.write(velocity);
  f_Right.write(velocity * -1);
  b_Left.write(velocity * -1);
  b_Right.write(velocity);

  
  Serial.println("Current Command: Move Left");
  Serial.println(" ");
}
void goRight(int param) {
  int percent = abs(param/10);
  int velocity = percent * 180;
  if(velocity > 150) {
    velocity = 150;
  }
  f_Left.write(velocity * -1);
  f_Right.write(velocity);
  b_Left.write(velocity);
  b_Right.write(velocity * -1);

  Serial.println("Current Command: Move Right");
  Serial.println(" ");
}

void setup() {
  // Begin the Serial at 9600 Baud
f_Left.attach(8);
f_Right.attach(9);
b_Left.attach(10);
b_Right.attach(11);
 delay(500);
  Serial.begin(9600);
}

void loop() {
  PotA0 = analogRead(InputA0);
  PotA1 = analogRead(InputA1);
  SpeedA0 = map(PotA0, 0, 1023, 0, 100);
  SpeedA1 = map(PotA1, 0, 1023, 0, 100);
  if(SpeedA0 >= 55 and SpeedA0 <= 100)
  {
    //backwards
    outputValueY = map(SpeedA0, 55, 100, 0, -10);
  }
  else if(SpeedA0 >= 0 and SpeedA0 <= 45)
  {
    //forwards
    outputValueY = map(SpeedA0, 0, 45, 0, 10);
  }
  else
  {
    if(SpeedA1 >= 55 and SpeedA1 <= 100)
    {
    outputValueX = map(SpeedA1, 55, 100, 0, 10);
    //right
    }
    else if(SpeedA1 >= 0 and SpeedA1 <= 45)
    {
    outputValueX = map(SpeedA1, 0, 45, 0, -10);
    }
    //left
    else
    {
     outputValueX = 0;
     outputValueY = 0;
     
    }
   }  
   
   if(outputValueY < 0){ 
    goBackward(outputValueY); 
   }
  else if(outputValueY > 0){ 
    goForward(outputValueY); 
   }
   if(outputValueX < 0){ 
    goLeft(outputValueX); 
   }
  else if(outputValueX > 0){ 
    goRight(outputValueX); 
   }
  
  str1=String(outputValueX);
  str2=String(outputValueY); 



  //str.toCharArray(mystr, 4);
  Serial.println("X Position: ");
  Serial.println(str1); //Write the serial data
  Serial.println("Y Position: ");
  Serial.println(str2); //Write the serial data
  Serial.println(" ");
  
  delay(100);
}
