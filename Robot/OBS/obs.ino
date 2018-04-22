#include <Adafruit_CircuitPlayground.h>
 
#define BINS   32          // The number of FFT frequency bins
#define FRAMES 4           // This many FFT cycles are averaged 
 
void setup() {
  CircuitPlayground.begin();  // Set up the board library and serial
  Serial.begin(9600);
}
 
void loop() {
  uint8_t i,j;
  uint16_t spectrum[BINS];     // FFT spectrum output buffer
  uint16_t avg[BINS];          // The average of FRAME "listens"
 
  for(j=1; j <= FRAMES; j++) {             // We gather data FRAMES times and average it
     CircuitPlayground.mic.fft(spectrum);  // Here is the CP listen and FFT the data routine
     for(i=0; i < BINS; i++) {             // Add for an average
       if(spectrum[i] > 255) spectrum[i] = 255; // limit outlier data
       if(i == 0)
         avg[i] = spectrum[i];
       else
         avg[i] = avg[i] + spectrum[i];
     }
  } 
  for(i=0; i < BINS; i++) {               // For each output bin average
     avg[i] = avg[i] / FRAMES;            //  divide about the number of values aaveraged
  }
  int maxVal = 0, maxIndex = 0;
  for(i=0; i < BINS; i++) {               // For each output bin average
     if(avg[i] >= maxVal) {               //  find the peak value
       maxVal = avg[i];
       maxIndex = i;                      //  and the bin that max value is in
     }
  }
  for(j=0; j < 32; j++) {           // print spectrum 32 bins
     Serial.print(avg[j]);
     Serial.print(" ");
  }
  Serial.println("");              // and print the highest value and the bin it is in
  Serial.print("Max Value = "); Serial.print(maxVal);
  Serial.print(", Index of Max Value = "); Serial.println(maxIndex);
}