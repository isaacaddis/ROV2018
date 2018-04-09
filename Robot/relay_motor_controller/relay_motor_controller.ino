/**
 * @author jiajerho
 * 
 * ROV relay motor controller v2.4
 * 4/8/2018
 */
 
// Motors
#define M1 9 //MOTOR 1
#define MM1 2 //MOTOR 1
#define M2 3 //MOTOR 2
#define MM2 4 //MOTOR 2
#define M3 5 //MOTOR 3
#define MM3 6 //MOTOR 3
#define M4 7 //MOTOR 4
#define MM4 8 //MOTOR 4

// Speed pins
int speed0 = 170; 
int speed3 = 170;
int speed1 = 170; 
int speed2 = 170; 
const int knob = 0; // Pin for Speed
const int knob3 = 3; // Pin for Speed
const int knob1 = 1; // Pin for Speed
const int knob2 = 2; // Pin for Speed

void setup() {
  // set up serial
  Serial.begin(9600);

  pinMode(M1, OUTPUT); //MOTOR 1 OUTPUT
  pinMode(MM1, OUTPUT); // MOTOR 1 OUTPUT
  pinMode(M2, OUTPUT); //MOTOR 2 OUTPUT
  pinMode(MM2, OUTPUT); // MOTOR 2 OUTPUT
  pinMode(M3, OUTPUT); //MOTOR 3 OUTPUT
  pinMode(MM3, OUTPUT); // MOTOR 3 OUTPUT
  pinMode(M4, OUTPUT); //MOTOR 4 OUTPUT
  pinMode(MM4, OUTPUT); // MOTOR 4 OUTPUT
}

/**
 * note: all turning is with regards to the center of the robot
 * the joystick controls the robot based on the camera view
 * this is because the driver can't see the actual robot in water, they have to rely on the camera vision
 */
void loop()
{
  // Joystick power
  speed0 = analogRead(knob)/2; //vertical y-axis
  speed3 = analogRead(knob3)/2; // vertical x-axis
  speed1 = analogRead(knob1)/2; //lateral y-axis
  speed2 = analogRead(knob2)/2; //lateral x-axis
  
  /**
   * right and left motors
   */
  // if y-axis power is negative
  if (speed1 < 50)
  {
    allForwards();
  }
  // if y-axis power is positive
  else if (speed1 > 400)
  {
    allReverse();
  } 
  // if y-axis power is at resting state (for the sake of brevity we're calling it zero from now on)
  else 
  
    // if x-axis power is negative (left direction)
    if (speed2 < 50){
      turnLeft();
    } 
    // if x-axis power is positive (right direction)
    else if (speed2 > 400){
      turnRight();
    } 
    // if x-axis power is zero 
    else {
      allZero();
    }
  

/**
 * vertical motors
 */
  // if y-axis power is negative
  if (speed0 < 50) 
  {
    goDown();
  }
  // if y-axis power is positive
  else if (speed0 > 400) 
  {
    goUp();
  }
  // if y-axis power is zero
  else 
  {
    if (speed3 < 50){
      pitchFwd();
    }
    else if (speed3 > 400){
      pitchBack();
    }
    else {
      verticalZero();
    }
  }
}

// vertical motor functions and motion 
void goUp(){
  digitalWrite(MM3, HIGH); //MOTOR 3 CLOCKWISE
   digitalWrite(MM4, HIGH); // MOTOR 4 CLOCKWISE
//  Serial.println("Go Up");
}
void goDown(){
    digitalWrite(M3, HIGH); //MOTOR 3 COUNTER CLOCKWISE
   digitalWrite(M4, HIGH); // MOTOR 4 COUNTER CLOCKWISE
//  Serial.println("Go Down");
}
void pitchFwd(){
  digitalWrite(M3, HIGH); 
   digitalWrite(MM4, HIGH);
//  Serial.println("Pitch fowards");
}
void pitchBack(){
  digitalWrite(MM3, HIGH);
   digitalWrite(M3, HIGH);
//  Serial.println("Pitch backwards");
}
void verticalZero(){
   digitalWrite(M3, LOW); //MOTOR 3 STOP
   digitalWrite(MM3, LOW); // MOTOR 3 STOP
   digitalWrite(M4, LOW); //MOTOR 4 STOP
  digitalWrite(MM4, LOW); // MOTOR 4 STOP
//  Serial.println("Vertical zero");
}

// lateral motion functions
void allForwards(){
  digitalWrite(M1, HIGH); //MOTOR 1 CLOCKWISE
  digitalWrite(M2, HIGH); //MOTOR 2 CLOCKWISE
//  Serial.println("All forwards");
}
void allReverse(){
  digitalWrite(MM1, HIGH); //MOTOR 1 COUNTER CLOCKWISE
  digitalWrite(MM2, HIGH); //MOTOR 2 COUNTER CLOCKWISE
//  Serial.println("All reverse");
}
void allZero(){
  digitalWrite(M1, LOW); //MOTOR 1 STOP
  digitalWrite(MM1, LOW); // MOTOR 1 STOP
  digitalWrite(M2, LOW); //MOTOR 2 STOP
  digitalWrite(MM2, LOW); // MOTOR 2 STOP
  digitalWrite(M3, LOW); //MOTOR 3 STOP
  digitalWrite(MM3, LOW); // MOTOR 3 STOP
  digitalWrite(M4, LOW); //MOTOR 4 STOP
  digitalWrite(MM4, LOW); // MOTOR 4 STOP
//  Serial.println("All zero");
}
void turnLeft(){
  digitalWrite(M1, HIGH); //MOTOR 1 CLOCKWISE
  digitalWrite(MM2, HIGH); //MOTOR 2 COUNTER CLOCKWISE
//  Serial.println("Turn left");
}
void turnRight(){
  digitalWrite(MM1, HIGH); //MOTOR 1 COUNTER CLOCKWISE
  digitalWrite(M2, HIGH); //MOTOR 2 CLOCKWISE
//  Serial.println("Turn right");
}
