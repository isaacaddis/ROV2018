/**
 * @author Jiajer Ho (jh10422)
 * ROV Servo Claw 2.0
*/
// Use 1K Ohm resistor
// Opens when button pressed, close when button not pressed

#include <Servo.h>
int button1 = 4; //button pin, connect to ground to move servo
int press1 = 0;
Servo servo1;
Servo myservo;  // create servo object to control a servo

int potpin = 0;  // analog pin used to connect the potentiometer
int val;    // variable to read the value from the analog pin
void setup()
{
 pinMode(button1, INPUT);
 servo1.attach(7);
   myservo.attach(9);  // attaches the servo on pin 9 to the servo object
 digitalWrite(4, HIGH); //enable pullups to make pin high
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
   val = analogRead(potpin);            // reads the value of the potentiometer (value between 0 and 1023)
  val = map(val, 0, 1023, 0, 180);     // scale it to use it with the servo (value between 0 and 180)
  myservo.write(val);                  // sets the servo position according to the scaled value

}

