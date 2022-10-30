#!/usr/bin/python
import time
import sys
import RPi.GPIO as GPIO

VALVE_1 = 32
VALVE_2 = 36
VALVE_3 = 38
VALVE_4 = 40

valves = [VALVE_1, VALVE_2, VALVE_3, VALVE_4]

print("Setting up GPIO")
GPIO.setmode(GPIO.BOARD)
for v in valves:
    GPIO.setup(v, GPIO.OUT)

print("Ensuring all valves are off...")
for v in valves:
    GPIO.output(v, GPIO.HIGH)

for (i, v) in enumerate(valves):
    print("Testing valve " + str(i) + " (output at pin " + str(v) + ")")
    try:
        GPIO.output(v, GPIO.LOW) 
    except KeyboardInterrupt:
        print("QUITING TEST")
        GPIO.cleanup()
    time.sleep(2)
    GPIO.output(v, GPIO.HIGH) 
    
GPIO.cleanup()
