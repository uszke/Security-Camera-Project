// Serial commands
#define CMD_PING        '@'
#define CMD_SERVO_PIN_2       '0'
#define CMD_SERVO_PIN_3       '1'
#define CMD_RD_PIN      'r'
#define PI 3.14115134234
#include <Servo.h>

//const int pirSensor = 7;



Servo pan,tilt;  // create servo object to control a servo
// twelve servo objects can be created on most boards



void setup ()
{

  Serial.begin (9600) ;
  Serial.println ("DRC Arduino 1.0") ;
  pan.attach(2);  // attaches the servo on pin 2 to the servo object
  tilt.attach(3);  // attaches the servo on pin 3 to the servo object
//  pinMode(pirSensor, INPUT);
}

int myGetchar ()
{
  int x ;
  while ((x = Serial.read ()) == -1)
    ;
  return x ;
}

void loop ()
{
  unsigned int pin ;
  unsigned int aVal, dVal ;
  int pos ;
 // int pirState = digitalRead(pirSensor);
 // Serial.println(pirState);
  for (;;)
  {
    if (Serial.available () > 0)
    {
      switch (myGetchar ())
      {
        case CMD_PING:
          Serial.write (CMD_PING) ;
          continue ;
                    

        case CMD_SERVO_PIN_2: //pan
          pos  = myGetchar () ;
          if ((pos >= 0) && (pos <= 180))
            pan.write(pos);
          continue ;


        case CMD_SERVO_PIN_3:  //tilt
          pos  = myGetchar () ; 
          if ((pos >= 0) && (pos <= 180))
            tilt.write(pos);
          continue ;    


      //  case CMD_RD_PIN:
      //    pin = myGetchar () ;
      //    if ((pin >= MIN_DPIN) && (pin <= MAX_DPIN))
      //      dVal = digitalRead (7) ;
      //    else
      //      dVal = LOW ;
      //    Serial.write ((dVal == HIGH) ? '1' : '0') ;
      //    continue ;


      }
    }
  }
}
