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
  while(Serial.available()>0){
    if(String(Serial.read())=="Ready"){
      Serial.write(sample);
      Serial.println(sample);
    }
  }
  Serial.println("No serial comms");
}
