#!/usr/bin/python
import time
import sys
import RPi.GPIO as GPIO

FLOW_SENSOR_GPIO = 7 

print("Setting up GPIO")
GPIO.setmode(GPIO.BOARD)
GPIO.setup(FLOW_SENSOR_GPIO, GPIO.IN)


while True:
    try:
        print(GPIO.input(FLOW_SENSOR_GPIO))
    except KeyboardInterrupt:
        print('\nkeyboard interrupt!')
        GPIO.cleanup()
        sys.exit()
