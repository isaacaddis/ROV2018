#include <Wire.h>
#include <LCD.h>
#include <LiquidCrystal_I2C.h>
#include <Thermistor.h>
#include <Servo.h>

/**
 * @author tedfoodlin
 * @author Jiajer Ho (jh10422)
 * @author "Neil" (5caryT001sMan)
 * 
 * 45C Robotics Smart System
 * 16x02 Display
 * v1.8
*/

Thermistor temp(0);
#define I2C_ADDR    0x27 // <<- Add your address here.
#define Rs_pin  0
#define Rw_pin  1
#define En_pin  2
#define BACKLIGHT_PIN 3
#define D4_pin  4
#define D5_pin  5
#define D6_pin  6
#define D7_pin  7

int sensorPin = 1;
float vPow = 4.7;
float r1 = 100000;
float r2 = 10000;
int piezoPin = 7;
int button1 = 4; //button pin, connect to ground to activate buzzer
int buttonpin1 = 10; // button pin for alarm
int press1 = 0;
int alarm = 0;
int mute = 0;

#define ECHO_PIN     11  // Arduino pin tied to echo pin on the ultrasonic sensor.
#define TRIGGER_PIN  12  // Arduino pin tied to trigger pin on the ultrasonic sensor.
#define MAX_DISTANCE 500 // Maximum distance we want to ping for (in centimeters). Maximum sensor distance is rated at 400-500cm.
#define SERIESRESISTOR 10000    
#define THERMISTORPIN A0 

LiquidCrystal_I2C lcd(I2C_ADDR,En_pin,Rw_pin,Rs_pin,D4_pin,D5_pin,D6_pin,D7_pin);

void setup()
{
  pinMode(button1, INPUT);
  digitalWrite(button1, HIGH); //enable pullups to make pin high
  Serial.begin(9600);
   
  // Send ANSI terminal codes
  Serial.print("\x1B");
  Serial.print("[2J");
  Serial.print("\x1B");
  Serial.println("[H");
  // End ANSI terminal codes
   
  Serial.println("--------------------");
  Serial.println("DC VOLTMETER");
  Serial.print("Maximum Voltage: ");
  Serial.print((int)(vPow / (r2 / (r1 + r2))));
  Serial.println("V");
  Serial.println("--------------------");
  Serial.println("");
   
  pinMode (buttonpin1, INPUT);
  // initialize serial communication
  
  lcd.begin (16,2);
 
  // LCD Backlight ON
  lcd.setBacklightPin(BACKLIGHT_PIN,POSITIVE);
  lcd.setBacklight(HIGH);

  lcd.home (); // go home on LCD
  lcd.setBacklight(HIGH);

  lcd.home (); // go home on LCD
  lcd.setCursor(0,0);
  lcd.print("45C ROBOTICS  ");
  lcd.setCursor(0,1);
  lcd.print("VERSION: 1.8  ");  
    delay(1500);
    
  lcd.begin (16,2);

  Serial.println(" ");
  Serial.println("Sonar and temperature sensors enabled!");
  Serial.println(" ");
}

void loop()
{
  press1 = digitalRead(button1);

  //tone(piezoPin, 1000, 500);
  //delay(1000);
  
  int reading = analogRead(sensorPin);  
  // converting that reading to voltage, for 3.3v arduino use 3.3
  float voltage = reading * 5.0;
  voltage /= 1024.0; 
  
  // print out the voltage
  Serial.println((String)voltage + " volts");
  
  float temperatureC = (voltage - 0.5) * 100; // converting from 10 mv per degree wit 500 mV offset to degrees ((voltage - 500mV) times 100)
  int temperature = temp.getTemp();
  
  lcd.setCursor (0,0); // go to start of 2nd line
  lcd.print("ALT:102");
  lcd.setCursor(9,0); // go to start of 2nd line

  lcd.print(finalTemperatureDisplay);
    delay(500);
    
  float v = (analogRead(1) * vPow) / 1024.0;
  float v2 = v / (r2 / (r1 + r2));
  
  // Send ANSI terminal codes
  Serial.print("\x1B");
  Serial.print("[1A");
  // End ANSI terminal codes
  
  float v3 = v2+1;
  lcd.setCursor (0,1);
  lcd.print("");
  if (v3 < 11.8) { 
    lcd.setCursor(0,1);
    lcd.print("01 LOW VOLTAGE        ");
    if (mute < 1) {
      tone(piezoPin, 2500);
      delay(500);
      noTone(piezoPin);
      alarm = alarm + 1;
    }
  }
  if (press1 == HIGH) {
    if (mute > 1) {
      mute = 0;
      alarm = 0;
      lcd.setCursor(0,1);
      lcd.print("02 ALARM UNMUTED       ");
      delay(500);
    }
    else if (alarm > 1) {
      mute++;
      lcd.setCursor(0,1);
      lcd.print("02 ALARM MUTED       ");
      delay(500);
    }
    else
    {
      lcd.print("02 ALARM TEST        ");
      tone(piezoPin, 2500);
      delay(500);
      noTone(piezoPin);
    }
  }
  else if (v3 > 11.8) {
    lcd.setCursor(0,1);
    lcd.print("SYSTEM HEALTHY       ");
    Serial.println("Temperature of water: " + String(temperature) + "C");
    Serial.println("Temperature of box:   " + String(temperatureC) + "C");
  }
  
}

