import time
import RPi.GPIO as GPIO

SET_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(SET_PIN,GPIO.IN)

if(GPIO.input(18) == GPIO.HIGH):
    print('ok')
else:
    print('ng')