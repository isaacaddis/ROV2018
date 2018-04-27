const int sampleWindow = 50; // Sample window width in mS (50 mS = 20Hz)
unsigned int sample;
#include "Timer.h"

Timer t;
void setup() 
{
   Serial.begin(9600);
   t.every(1000,takeReading)
}


void loop() 
{
   t.update()
}
void takeReading(){
   unsigned long startMillis= millis();  // Start of sample window
   unsigned int peakToPeak = 0;   // peak-to-peak level

   unsigned int signalMax = 0;
   unsigned int signalMin = 1024;

   // collect data for 50 mS
   while (millis() - startMillis < sampleWindow)
   {
      sample = analogRead(3);
      if (sample < 1024)  // toss out spurious readings
      {
         if (sample > signalMax)
         {
            signalMax = sample;  // save just the max levels
         }
         else if (sample < signalMin)
         {
            signalMin = sample;  // save just the min levels
         }
      }
   }
   peakToPeak = signalMax - signalMin;  // max - min = peak-peak amplitude
   double volts = (peakToPeak * 5.0) / 1024;  // convert to volts
   
   if(volts < 1.2 && volts > 1.6){
      
   }

   Serial.println(volts);
}
