// Written by Jiajer Ho

#include <Wire.h>
#include <LCD.h>
#include <LiquidCrystal_I2C.h>
#include "SevenSegmentTM1637.h"
#include "SevenSegmentExtended.h"
#include "SevenSegmentFun.h"
#define I2C_ADDR          0x27        //Define I2C Address where the PCF8574A is
#define BACKLIGHT_PIN      3
#define En_pin             2
#define Rw_pin             1
#define Rs_pin             0
#define D4_pin             4
#define D5_pin             5
#define D6_pin             6
#define D7_pin             7

long buttonPressed = 0;
long markedNum = 0;
int ledPin = 11;                    // LED connected to digital pin 13
int buttonPin = 7;                  // button on pin 2
int clapperPin = 6;  
int clapperState=0; 
int intfinalMin = 0;
int intfinalSec = 0;
byte bytefinalMin;
byte bytefinalSec;
int value = LOW;                    // previous value of the LED
int buttonState;                    // variable to store button state
int lastButtonState;                // variable to store last button state
int blinking;                       // condition for blinking - timer is timing
int frameRate = 15;                // the frame rate (frames per second) at which the stopwatch runs - Change to suit
long interval = (1000/frameRate);   // blink interval
long previousMillis = 0;            // variable to store last time LED was updated
long startTime ;                    // start time for stop watch
long elapsedTime ;                  // elapsed time for stop watch
int fractional;                     // variable used to store fractional part of Frames
int fractionalSecs;                 // variable used to store fractional part of Seconds
int fractionalMins;                 // variable used to store fractional part of Minutes
int elapsedFrames;                  // elapsed frames for stop watch
int elapsedSeconds;                 // elapsed seconds for stop watch
int elapsedMinutes;                 // elapsed Minutes for stop watch
char buf[10];                       // string buffer for itoa function
String fileName;
String fileNum;
int magicNumber = 1;
int adjustTime = 2;
long action = 0;
LiquidCrystal_I2C      lcd(I2C_ADDR, En_pin,Rw_pin,Rs_pin,D4_pin,D5_pin,D6_pin,D7_pin);
const byte PIN_CLK = 11;   // define CLK pin (any digital pin)
const byte PIN_DIO = 12;   // define DIO pin (any digital pin)
SevenSegmentExtended      display(PIN_CLK, PIN_DIO);
byte byMin;
byte bySec;
int intSec = 88;
int intMin = 88;
byte bytefileNum;
const unsigned int clockSpeed = 10000; 

void setup()
{
   bySec = (int)intSec;
 byMin = (int)intMin;
  display.begin();   
  pinMode(clapperPin, INPUT);
             // intialise the LCD.
  pinMode(ledPin, OUTPUT);         // sets the digital pin as output
  pinMode(buttonPin, INPUT);       // not really necessary, pins default to INPUT anyway
  digitalWrite(buttonPin, HIGH);   // turn on pullup resistors. Wire button so that press shorts pin to ground.
lcd.setBacklightPin(BACKLIGHT_PIN,POSITIVE);
display.setBacklight(100);
  display.printTime(byMin , bySec , false); 
lcd.setBacklight(HIGH);
lcd.begin(16, 2);  
lcd.setCursor(0,0);
lcd.print("SLATE Ver 2.2.5");
  lcd.setCursor(0,1);
 lcd.print("By JIAJER HO"); 
delay(1500);
lcd.clear();
lcd.setCursor(0,0);
lcd.print("DESIGNED FOR");
  lcd.setCursor(0,1);
 lcd.print("ADOBE AUDITION"); 
delay(1500);
  lcd.setCursor(0,0);
 lcd.print("30 FPS TIMECODE");
  lcd.setCursor(0,1);
 lcd.print("CALIBRATING...     "); 
delay(2500);
lcd.clear();
display.setBacklight(0);
}

void loop(){

  buttonState = digitalRead(buttonPin); // Check for button press, read the button state and store
 if (buttonState == LOW && lastButtonState == LOW  &&  blinking == false && clapperState == LOW){
 lcd.setBacklightPin(BACKLIGHT_PIN,POSITIVE);
 lcd.setBacklight(HIGH);
 lcd.setCursor(0,0);
 lcd.print("MARKER MUST BE      ");
 lcd.setCursor(0,1);
  lcd.print("CLOSED TO SYNC               ");
 }
if (buttonState == LOW && lastButtonState == LOW  &&  blinking == false && clapperState == HIGH && buttonPressed < 1){
lcd.setCursor(0,0);
   lcd.setBacklightPin(BACKLIGHT_PIN,POSITIVE);
  lcd.print("PRESS BUTTON   ");
  lcd.setCursor(0,1);
  lcd.print("TO SYNC RECORDER");
 }
 if (buttonState == LOW && lastButtonState == LOW  &&  blinking == false && clapperState == HIGH && buttonPressed >= 1){
  lcd.setCursor(0,0);
  lcd.print("STOPPED           ");
  lcd.setCursor(0,1);
  lcd.print(fileName);
lcd.setBacklightPin(BACKLIGHT_PIN,POSITIVE);
lcd.setBacklight(LOW);
 }
// check for a high to low transition if true then found a new button press while clock is not running - start the clock    
   if (buttonState == LOW && lastButtonState == HIGH  &&  blinking == false && clapperState == HIGH){
    startTime = millis();                               // store the start time
      blinking = true;                                  // turn on blinking while timing
      delay(10);                                         // short delay to debounce switch
      lastButtonState = buttonState;                    // store buttonState in lastButtonState, to compare next time 
       buttonPressed = buttonPressed + magicNumber;

      lcd.clear();
 

   }

// check for a high to low transition if true then found a new button press while clock is running - stop the clock and report
   else if (buttonState == LOW && lastButtonState == HIGH && blinking == true && clapperState == HIGH){

   blinking = false;                                    // turn off blinking, all done timing
   lastButtonState = buttonState;                       // store buttonState in lastButtonState, to compare next time

// Routine to report elapsed time            
   elapsedTime =   millis() - startTime;                // store elapsed time
   elapsedMinutes = (elapsedTime / 60000L);
   elapsedSeconds = (elapsedTime / 1000L);              // divide by 1000 to convert to seconds - then cast to an int to print
   elapsedFrames = (elapsedTime / interval);            // divide by 100 to convert to 1/100 of a second - then cast to an int to print
   fractional = (int)(elapsedFrames % frameRate);       // use modulo operator to get fractional part of 100 Seconds
   fractionalSecs = (int)((elapsedSeconds) % 60L);        // use modulo operator to get fractional part of 60 Seconds
   fractionalMins = (int)(elapsedMinutes % 60L);        // use modulo operator to get fractional part of 60 Minutes
   lcd.home();                                        // clear the LDC


 if (fractionalMins < 10){                            // pad in leading zeros
      lcd.print("0");                                 // add a zero
      }

    lcd.print(itoa(fractionalMins, buf, 10));       // convert the int to a string and print a fractional part of 60 Minutes to the LCD
      lcd.print(":");                                 //print a colan. 

 if (fractionalSecs < 10){                            // pad in leading zeros
      lcd.print("0");                                 // add a zero
      }

 lcd.print(itoa(fractionalSecs, buf, 10));          // convert the int to a string and print a fractional part of 60 Seconds to the LCD
   lcd.print(":");                                    //print a colan. 

 if (fractional < 10){                                // pad in leading zeros 
      lcd.print("0");                                 // add a zero
      }     

 lcd.print(itoa(fractional, buf, 10));              // convert the int to a string and print a fractional part of 25 Frames to the LCD
   }

 else{
      lastButtonState = buttonState;                  // store buttonState in lastButtonState, to compare next time
      
   }

// run commands at the specified time interval
// blink routine - blink the LED while timing
// check to see if it's time to blink the LED; that is, the difference
// between the current time and last time we blinked the LED is larger than
// the interval at which we want to blink the LED.

 if ( (millis() - previousMillis > interval) ) {

    if (blinking == true){
      
       previousMillis = millis();                    // remember the last time we blinked the LED

    

       elapsedTime =   millis() - startTime;         // store elapsed time
         elapsedMinutes = (elapsedTime / 60000L);      // divide by 60000 to convert to minutes - then cast to an int to print
         elapsedSeconds = (elapsedTime / 1000L);       // divide by 1000 to convert to seconds - then cast to an int to print
         elapsedFrames = (elapsedTime / interval);     // divide by 40 to convert to 1/25 of a second - then cast to an int to print
         fractional = (int)(elapsedFrames % frameRate);// use modulo operator to get fractional part of 25 Frames
         fractionalSecs = (int)(elapsedSeconds % 60L); // use modulo operator to get fractional part of 60 Seconds
         fractionalMins = (int)(elapsedMinutes % 60L); // use modulo operator to get fractional part of 60 Minutes
         
        lcd.home();   
       if (fractionalMins < 10){                     // pad in leading zeros
         lcd.print("0");                             // add a zero
         }

       lcd.print(itoa(fractionalMins, buf, 10));   // convert the int to a string and print a fractional part of 60 Minutes to the LCD
  
         lcd.print(":");                             //print a colan. 

       if (fractionalSecs < 10){                     // pad in leading zeros 
         lcd.print("0");                             // add a zero
         }

       lcd.print(itoa(fractionalSecs, buf, 10));   // convert the int to a string and print a fractional part of 60 Seconds to the LCD
      
         lcd.print(":");                             //print a colan. 

       if (fractional < 10){                         // pad in leading zeros 
         lcd.print("0");                             // add a zero
    
         }
          lcd.print(itoa((fractional), buf, 10));  // convert the int to a string and print a fractional part of 25 Frames to the LCD
         
         }

    else{
          digitalWrite(ledPin, LOW);                 // turn off LED when not blinking 
          }
 }
 unsigned long intfinalMin = strtoul(itoa(fractionalMins, buf, 10), NULL, 10);
 unsigned long intfinalSec = strtoul(itoa(fractionalSecs, buf, 10), NULL, 10);
 bytefinalSec = (int)intfinalSec;
 bytefinalMin = (int)intfinalMin;

 clapperState = digitalRead(clapperPin);

    // turn LED on:
  
     if (buttonPressed < 10){
     fileName = String("TRACK 1_00")+buttonPressed+String(".WAV");
     fileNum = String("000")+buttonPressed;
     }
     else{
     fileName = String("TRACK 1_0")+buttonPressed+String(".WAV");
     fileNum = String("00")+buttonPressed;
     }

if(clapperState == LOW && blinking == true && buttonState == LOW){
   action = 1;
    lcd.setBacklightPin(BACKLIGHT_PIN,POSITIVE);
    lcd.setBacklight(HIGH); 
   digitalWrite(ledPin, HIGH);  
   display.setBacklight(100);
   display.printTime(bytefinalMin, bytefinalSec, false); 
 }
 
if (clapperState == HIGH && blinking == true){
  if(action == 1){
    markedNum = markedNum + 1;
    lcd.setBacklightPin(BACKLIGHT_PIN,POSITIVE);
    lcd.setBacklight(HIGH);
    action = 0;
    lcd.setCursor(0,1);
    lcd.print("CUE MARKED         ");
       display.setBacklight(100);
       delay(300);
       display.clear();
       display.print(fileNum);
    
       delay(4700); 
  }
    lcd.setCursor(0,1);
    lcd.print(fileName); 
    digitalWrite(ledPin, LOW);  
    display.off();
    lcd.setBacklightPin(BACKLIGHT_PIN,POSITIVE);
    lcd.setBacklight(LOW);
 }
 

}
