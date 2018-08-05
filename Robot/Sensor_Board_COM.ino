char mystr[12]; //Initialized variable to store recieved data

void setup() {
  // Begin the Serial at 9600 Baud
  Serial.begin(9600);
  Serial1.begin(9600);
}

void loop() {
  Serial1.readBytes(mystr,12); //Read the serial data and store in var
  Serial.println("Temp 1");
  Serial.print(mystr[0]);
  Serial.print(mystr[1]);
  Serial.print('\n');
  Serial.println("Humidity");
  Serial.print(mystr[3]);
  Serial.print(mystr[4]);
  Serial.print('\n');
  Serial.println("Temp 2");
  Serial.print(mystr[6]);
  Serial.print(mystr[7]);
  Serial.print(mystr[8]);
  Serial.print('\n');
  Serial.println("Depth");
  Serial.print(mystr[10]);
  Serial.print(mystr[11]);
  Serial.print('\n');

  
  delay(1000);
}
