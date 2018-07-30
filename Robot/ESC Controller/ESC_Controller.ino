/**
 * @author Jiajer Ho and Alexander Vazquez
 * 
 * ROV ESC Controller Underwater Code (Receiver)  7/29/2018
 * Use ATMEGA1260 or 2560
 * 
 * Takes data from Surface Arduino and determine the ESC control  
 * 
 */
 
char mystr[4]; //Initialized variable to store recieved data
int testOutput = 0;
String str2 = "10";
void setup() {
// Begin the Serial at 9600 Baud
Serial1.begin(9600);
Serial.begin(9600);
pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {

digitalWrite(LED_BUILTIN, LOW); 
Serial.readBytes(mystr,4); //Read the serial data and store in var
String str(mystr);
testOutput = str.toInt();
 if (testOutput>= 1 and testOutput<= 10) {
    Serial1.println("Forwards");  
  
 }
  if (testOutput>= 11 and testOutput<= 20) {
    Serial1.println("Backwards"); 
  
 }
   if (testOutput<= 1) {
    Serial1.println("NONE"); 
  
 }
delay(100);
}
