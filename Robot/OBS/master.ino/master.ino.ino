#include <Servo.h>
int button1 = 8;
int button2 = 9;
int press1 = 0;
int press2 = 0;
String instruction;
Servo servo2; 

int potpin = 0;  
int val;   
void setup() {
  // put your setup code here, to run once:
   servo2.attach(7);  
}
void loop() {

  if(Serial.available()>0){
    instruction = Serial.read();
    if(instruction=="Open Claw"){
      servo2.write(150);
    }
    else{
      servo2.write(20);
    }
    delay(2000);
  }
}
