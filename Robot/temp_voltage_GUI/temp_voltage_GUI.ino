/*
  * Author: Jiajer Ho and Isaac Addis
  * Smart System Temp and Voltage Sensor
  * 45C Robotics CAMS ROV 2018
  */
 //Voltage Sensor
 //5V READ to A0
 //12V READ to A1
 float vPow = 5;
 float r1 = 100000;
 float r2 = 10000;
  //Temp Sensor
 //TEMPOUT 01 to A2
 //TEMPOUT 02 to A3
int V1;
int V2;
float R1 = 10000;
float logR2, R2, T, Tc, Tf, R21, logR21, T2, Tc2;
float c1 = 1.009249522e-03, c2 = 2.378405444e-04, c3 = 2.019202697e-07;

 void setup() {
   Serial.begin(9600);
 }
 
 void loop() {
  V1 = analogRead(2);
  R2 = R1 * (1023.0 / (float)V1 - 1.0);
  logR2 = log(R2);
  T = (1.0 / (c1 + c2*logR2 + c3*logR2*logR2*logR2));
  Tc = T - 273.15;
    V2 = analogRead(3);
  R21 = R1 * (1023.0 / (float)V2 - 1.0);
  logR21 = log(R21);
  T2 = (1.0 / (c1 + c2*logR21 + c3*logR21*logR21*logR21));
  Tc2 = T2 - 273.15;
   float v = (analogRead(0) * vPow) / 1024.0;
   float v2 = v / (r2 / (r1 + r2));
   float v4 = (analogRead(1) * vPow) / 1024.0;
   float v3 = v4 / (r2 / (r1 + r2));
   Serial.print("V1");
   Serial.println(v2);
   Serial.print("T1");
   Serial.println(Tc);
   Serial.print("V2");
   Serial.println(v3);
   Serial.print("T2");
   Serial.println(Tc2);
   delay(1000);
 }
