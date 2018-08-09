/**
 * @author Jiajer Ho and Alexander Vazquez
 * 
 * ROV ESC Controller Topside Code (Transmitter)  7/29/2018
 * Use ATMEGA168P
 * 
 * Takes data from Joystick and output TX data  
 * 
 */
 
const int InputA0 = A0;
int PotA0 = 0;        // value read from the pot
int SpeedA0 = 0;
const int InputA1 = A1;
int PotA1 = 0;        // value read from the pot
int SpeedA1 = 0;
int outputValue = 0;
int n = 0;
String str;
String str2;
char mystr[5];
void setup() {
  // Begin the Serial at 9600 Baud
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
    outputValue = map(SpeedA0, 55, 100, 0, 10);
  }
  else if(SpeedA0 >= 0 and SpeedA0 <= 45)
  {
    outputValue = map(SpeedA0, 0, 45, 20, 11);
  }
  else
  {
    if(SpeedA1 >= 55 and SpeedA1 <= 100)
    {
    outputValue = map(SpeedA1, 55, 100, 0, 10);
    }
    else if(SpeedA1 >= 0 and SpeedA1 <= 45)
    {
    outputValue = map(SpeedA1, 0, 45, 20, 11);
    }
    else
    {
     outputValue = 0;
    }
   }

  
  str=String(outputValue);

  str.toCharArray(mystr, 4);
  Serial.write(mystr, 4); //Write the serial data

  delay(100);
}
