/**
 * @author Jiajer Ho and Alexander Vazquez
 * 
 * ROV ESC Controller Top Side Code (Transmitter)  7/29/2018
 * Use ATMEGA168P
 * 
 * Takes data from Joystick and output TX data  
 * 
 */
 
const int analogInPin = A0;
int sensorValue = 0;        // value read from the pot
int outputValue = 0;
int outputValue2 = 0;
int n =0;
String str;
String str2;
char mystr[5];
void setup() {
  // Begin the Serial at 9600 Baud
  Serial.begin(9600);
}

void loop() {
  sensorValue = analogRead(analogInPin);
  outputValue2 = map(sensorValue, 0, 1023, 0, 100);
  if(outputValue2 >= 55 and outputValue2 <= 100){
    outputValue = map(outputValue2, 55, 100, 0, 10);
  }
    if(outputValue2 >= 0 and outputValue2 <= 45){
    outputValue = map(outputValue2, 0, 45, 20, 11);
  }
      if(outputValue2 >= 45 and outputValue2 <= 55){
    outputValue = 0;
  }
  str=String(outputValue);

  str.toCharArray(mystr, 4);
  Serial.write(mystr, 4); //Write the serial data

  delay(100);
}
