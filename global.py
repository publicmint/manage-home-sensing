#!/usr/bin/python3
from modules import sendData
from time import sleep
import RPi.GPIO as GPIO
import sys
import os

SET_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(SET_PIN,GPIO.IN,pull_up_down=GPIO.PUD_UP)

SEND_TIME = 60 # seconds

count = 0

def output(channel):
    global count
    print("up!") 
    count = count + 1
    print(count)

if __name__ == '__main__':
    argvs = ["apikey", "url", "name"]
    if len(sys.argv) - 1 == len(argvs):
        timer = 0

        apikey = sys.argv[1]
        url = sys.argv[2]
        name = sys.argv[3]

        GPIO.add_event_detect(SET_PIN,GPIO.BOTH,callback=output,bouncetime=600)

        while True:
            sleep(1)
            timer = timer + 1
            try:
                pass
                if timer > SEND_TIME:
                    print(count)
                    sendData.sendData(base_url=url, api_key=apikey, name=name, value=count)
                    count = 0
                    timer = 0
            except Exception as e:
                print(e)
                print('error')
                GPIO.cleanup()
    else:
        print("{0}:[{1}] [{2}] [{3}] ".format(os.path.basename(__file__), argvs[0], argvs[1], argvs[2]))

GPIO.cleanup()

