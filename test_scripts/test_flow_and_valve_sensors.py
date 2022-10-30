#!/usr/bin/python
import time
import sys
import RPi.GPIO as GPIO

FLOW_SENSOR_GPIO = 7

VALVE_1 = 40
VALVE_2 = 38
VALVE_3 = 32
VALVE_4 = 36

#valves = [VALVE_1, VALVE_2, VALVE_3, VALVE_4]
valves = [VALVE_1]



print("Setting up GPIO")
GPIO.setmode(GPIO.BOARD)
GPIO.setup(FLOW_SENSOR_GPIO, GPIO.IN)
for v in valves:
    GPIO.setup(v, GPIO.OUT)


global count
count = 0

def countPulse(channel):
   global count
   if start_counter == 1:
      count = count+1

GPIO.add_event_detect(FLOW_SENSOR_GPIO, GPIO.FALLING, callback=countPulse)

print("Ensuring all valves are off...")
for v in valves:
    GPIO.output(v, GPIO.HIGH)

valve_open_time = 10

for (i, v) in enumerate(valves):
    print("Testing valve " + str(i) + " (output at pin " + str(v) + ")")
    try:
        GPIO.output(v, GPIO.LOW) 
    except KeyboardInterrupt:
        print("QUITING TEST")
        GPIO.cleanup()

    start_counter = 1
    time.sleep(valve_open_time)
    start_counter = 0
    #flow = (count / 7.5) # Pulse frequency (Hz) = 7.5Q, Q is flow rate in L/min.
    flow = (count / 36) # Pulse frequency (Hz) = 7.5Q, Q is flow rate in L/min.
    flow = flow / 7
    print("The flow is: %.3f Liter/min" % (flow))
    test_val = count * 2.28e-2 * 1.5
    print("The adjusted flow is: %.3f Liter/min" % (test_val))
    dispensed_water = (flow / 60) * valve_open_time * 1000 
    print("Dispensed: %.3f mL" % (dispensed_water))
    count = 0

    # Turn off valve
    GPIO.output(v, GPIO.HIGH) 
    
GPIO.cleanup()
