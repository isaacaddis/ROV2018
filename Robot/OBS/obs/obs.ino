//#include <Servo.h>
//Servo servo;
void setup(){
  Serial.begin(9600);
  Serial.println("Start!");
//  servo.attach(0);
}
void loop()
{
  int status;

//  while(Serial.available()) {
      Serial.println("Avail");
      status = Serial.read();
      if(status==49) {
//        servo.write(180);
          Serial.print("yay");
          delay(2000);
      }
      else{
//        servo.write(0);
          Serial.println("nay");
          Serial.println(status);
          delay(100);
      }
  }

//}
