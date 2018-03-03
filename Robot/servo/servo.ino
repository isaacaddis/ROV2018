/**
 * @author Jiajer Ho (jh10422)
 * ROV Servo Claw 3.0 for 45C CAMS ROV 2018
*/

#include <Servo.h>
int button1 = 8;
int button2 = 9;
int press1 = 0;
int press2 = 0;
Servo servo1;
Servo servo2; 

int potpin = 0;  
int val;   
void setup()
{
 pinMode(button1, INPUT);
 servo1.attach(0);
 servo2.attach(1);  
 digitalWrite(4, HIGH); 
}

void loop()
{
press1 = digitalRead(button1);
 if (press1 == LOW)
 {
   servo1.write(180);
 }
 else {
   servo1.write(0);
 }
press2 = digitalRead(button2);
 if (press2 == LOW)
 {
   servo2.write(180);
 }
 else {
   servo2.write(0);
 }
}
