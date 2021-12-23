import RPi.GPIO as GPIO

LED_PIN1 = 8
SWITCH_PIN1 = 9
LED_PIN2 = 3
SWITCH_PIN2 = 10
LED_PIN3 = 2
SWITCH_PIN3 = 7

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN1, GPIO.OUT)
GPIO.setup(SWITCH_PIN1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(LED_PIN2, GPIO.OUT)
GPIO.setup(SWITCH_PIN2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(LED_PIN3, GPIO.OUT)
GPIO.setup(SWITCH_PIN3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        val1 = GPIO.input(SWITCH_PIN1)
        print(val1)
        GPIO.output(LED_PIN1, val1)
        val2 = GPIO.input(SWITCH_PIN2)
        GPIO.output(LED_PIN2, val2)
        val3 = GPIO.input(SWITCH_PIN3)
        GPIO.output(LED_PIN3, val3)       

finally:
    GPIO.cleanup()
    print('cleanup and exit')