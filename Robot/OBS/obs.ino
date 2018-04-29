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
void takeReading(){
   double runningTotal = 0;
   elapsedMillis timeElapsed;
   unsigned int interval = 10000; 
   while(timeElapsed < interval){
     double volts = getVolts();
     //for testing
     Serial.println("Volts: ");
     Serial.println(volts);
     if(volts > 1 && volts < 2)
      runningTotal +=1;
      Serial.println("Added to running total!");  
     }
  double ratio = runningTotal/timeElapsed;
  if(ratio > .05 && ratio < 1){
    Serial.println("Open Claw");
  }
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
