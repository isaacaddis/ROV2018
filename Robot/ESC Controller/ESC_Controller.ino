/**
 * @author Jiajer Ho and Alexander Vazquez
 * 
 * ROV ESC Controller Underwater Code (Receiver)  08/03/2018
 * Use ATMEGA1260 or 2560
 * 
 * Takes data from Surface Arduino and determine the ESC control  
 * 
 */
 #include <Servo.h>
 Servo myservo;  // create servo object to control a servo
// twelve servo objects can be created on most boards

int pos = 0;    // variable to store the servo position


char mystr[4]; //Initialized variable to store recieved data
int testOutput = 0;
String str2 = "10";
void setup() {
  myservo.attach(9); 
// Begin the Serial at 9600 Baud
Serial1.begin(9600);
Serial.begin(9600);
pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {

digitalWrite(LED_BUILTIN, LOW); 
Serial1.readBytes(mystr,4); //Read the serial data and store in var
String str(mystr);
testOutput = str.toInt();
 if (testOutput>= 1 and testOutput<= 10) {
    Serial.println("Forwards");  
    pos = map(testOutput, 1, 10, 90, 165);
  myservo.write(pos); 
 }
  if (testOutput>= 11 and testOutput<= 20) {
    Serial.println("Backwards"); 
      pos = map(testOutput, 11, 20, 90, 24);
  myservo.write(pos); 
 }
   if (testOutput<= 1) {
    Serial.println("NONE"); 
  myservo.write(90); 
 }
delay(100);
}
