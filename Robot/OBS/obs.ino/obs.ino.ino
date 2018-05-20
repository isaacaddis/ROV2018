const int sampleWindow = 50; // Sample window width in mS (50 mS = 20Hz)
unsigned int sample;
#include <elapsedMillis.h>

void setup() 
{
  cli();//disable interrupts
  
  //set up continuous sampling of analog pin 0
  
  //clear ADCSRA and ADCSRB registers
  ADCSRA = 0;
  ADCSRB = 0;
  
  ADMUX |= (1 << REFS0); //set reference voltage
  ADMUX |= (1 << ADLAR); //left align the ADC value- so we can read highest 8 bits from ADCH register only
  
  ADCSRA |= (1 << ADPS2) | (1 << ADPS0); //set ADC clock with 32 prescaler- 16mHz/32=500kHz
  ADCSRA |= (1 << ADATE); //enabble auto trigger
  ADCSRA |= (1 << ADIE); //enable interrupts when measurement complete
  ADCSRA |= (1 << ADEN); //enable ADC
  ADCSRA |= (1 << ADSC); //start ADC measurements
  
  sei();//enable interrupts
   Serial.begin(9600);
}

ISR(ADC_vect) {//when new ADC value ready
  sample = ADCH;//update the variable sample with new value from A0 (between 0 and 255)
}
void loop() 
{
  Serial.println(sample);
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
//     if (sample < 1024)  // toss out spurious readings
//     {
//        if (sample > signalMax)
//        {
//           signalMax = sample;  // save just the max levels+
//        }
//        else if (sample < signalMin)
//        {
//           signalMin = sample;  // save just the min levels
//        }
//     }
     sample = (sample+1)/4 -1; //8-bit (0-255)
     if(sample<0){
      sample = 0;
     }
     PORTD = ADCH;
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
  if(ratio > .10){
    Serial.println("Open Claw");
  }
  else{
    Serial.println("Don't open claw");
  }
}
