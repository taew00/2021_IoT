import RPi.GPIO as GPIO
import time


Red_Led = 4
Yellow_Led = 17
Green_Led = 27
GPIO.setmode(GPIO.BCM) #GPIO.BCM or GPIO.BOARD
def onoff(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(pin, GPIO.LOW)

print("Red Led on")
onoff(Red_Led)


print("Yellow Led on")
onoff(Yellow_Led)

print("Green Led on")
onoff(Green_Led)

GPIO.cleanup()