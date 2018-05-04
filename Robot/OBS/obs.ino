const int sampleWindow = 50; // Sample window width in mS (50 mS = 20Hz)
unsigned int sample;
#include <elapsedMillis.h>

void setup() 
{
   Serial.begin(9600);
}


void loop() 
{
  takeReading();
}
double getVolts(){
  unsigned long startMillis= millis();  // Start of sample window
  unsigned int peakToPeak = 0;   // peak-to-peak levelunsigned int signalMax = 0;
  unsigned int signalMin = 1024;
  unsigned int signalMax = 0;
  // collect data for 50 mS
  while (millis() - startMillis < sampleWindow)
  {
     sample = analogRead(3);
     if (sample < 1024)  // toss out spurious readings
     {
        if (sample > signalMax)
        {
           signalMax = sample;  // save just the max levels+
        }
        else if (sample < signalMin)
        {
           signalMin = sample;  // save just the min levels
        }
     }
  }
  peakToPeak = signalMax - signalMin;  // max - min = peak-peak amplitude
  double volts = (peakToPeak * 5.0) / 1024;  // convert to volts
  return volts;

}
void takeReading(){
   double loops = 0;
   double runningTotal = 0;
   elapsedMillis timeElapsed;
   unsigned int interval = 10000; 
   while(timeElapsed < interval){
     loops = loops +1;
     double volts = getVolts();
     //for testing
 
     Serial.println("Volts: ");
     Serial.println(volts);
     if(volts > 1.2 && volts < 1.8){
      runningTotal +=1;
      Serial.println("Added to running total! with runningTotal " + String(runningTotal)+" and Loops " + loops);
     }
     else{
      Serial.println("COULDN'T ADD TO RUNNING TOTAL. Voltage was : "+ String(volts));
     }
     Serial.println("Time Ellapsed: " +String(timeElapsed) + "ms");
   }
  double ratio = runningTotal/loops;
  Serial.println("Ratio is currently: "+ String(ratio));
  if(ratio > .05){
    Serial.println("Open Claw");
  }
  else{
    Serial.println("Don't open claw");
  }
    delay(5000);

}
