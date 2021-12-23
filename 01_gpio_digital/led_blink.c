#include <wiringPi.h>
#define LED_1 7
#define LED_2 8
#define LED_3 9
 
void LED_LIGHT(int LED)
{
  pinMode (LED , OUTPUT);
  digitalWrite (LED, HIGH); 
  delay(1000);
  digitalWrite (LED,  LOW);
}

int main (void)
{
  wiringPiSetup ();
  LED_LIGHT(LED_1);
  LED_LIGHT(LED_2);
  LED_LIGHT(LED_3);
  
  return 0 ; 
}