#include <Servo.h>
int button1 = 8;
int button2 = 9;
int press1 = 0;
int press2 = 0;
Servo servo1;
Servo servo2; 

int potpin = 0;  
int val;   
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
   servo1.attach(0);
   servo2.attach(1);  
}
void loop() {

  if(Serial.available()>0){
    instruction = Serial.read();
    if(instruction=="Open Claw"){
      servo2.write(180);
    }
    else{
      servo2.write(0);
    }
    delay(2000);
  }
}
