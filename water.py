#!/usr/bin/python
import time
import sys
import RPi.GPIO as GPIO


# Global variables
FLOW_SENSOR_GPIO = 7
VALVE_1 = 40
VALVE_2 = 38
VALVE_3 = 32
VALVE_4 = 36
valves = [VALVE_1, VALVE_2, VALVE_3, VALVE_4] 

def print_usage():
    print("USAGE:")
    print("python3 water.py [valve number]  [mL of water]")
    print("EXAMPLE:")
    print("python3 water.py 1 100")
    print("The command above will dispense 100 ml of water from valve 1")
    print("[valve number] must be 1, 2, 3, or 4.")
    print("[mL of water] must be greater than 0.")
    exit()

def check_args():
   try:
       sys.argv[1] = int(sys.argv[1])
       sys.argv[2] = int(sys.argv[2])
   except:
       print("Error occured.")
       print_usage()
    
   if len(sys.argv) != 3:
        print_usage()
   elif sys.argv[1] < 1:
        print_usage()
   elif sys.argv[1] > 4:
        print_usage()
   elif sys.argv[2] <= 0:
        print_usage()
        
def main():
    check_args()

    selected_valve = valves[sys.argv[1] - 1]
    dispense_limit = sys.argv[2]

    print("Setting up GPIO")
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(FLOW_SENSOR_GPIO, GPIO.IN)
    for v in valves:
        GPIO.setup(v, GPIO.OUT)

    print("Ensuring all valves are off...")
    for v in valves:
        GPIO.output(v, GPIO.HIGH)


    global count
    global water_dispensed
    count = 0
    water_dispensed = 0

    def countPulse(channel):
       global count
       if start_interval_counter == True:
          count = count + 1

    GPIO.add_event_detect(FLOW_SENSOR_GPIO, GPIO.FALLING, callback=countPulse)

    print("Opening valve...")
    try:
        GPIO.output(selected_valve, GPIO.LOW)
    except KeyboardInterrupt:
        print("QUITING PROGRAM")
        GPIO.cleanup()

    start_time = time.time()

    while water_dispensed <= dispense_limit:
        interval_start = time.time()
        start_interval_counter = True
        time.sleep(1)
        start_interval_counter = False
        interval = time.time() - interval_start
        flow = (count / 36) # Pulse frequency (Hz) = 36 * Q, Q is flow rate in L/min. Number obtained from flow sensor specs.
        flow = flow * 1.5 # Adjustment (recommended by Amazon reviewer)
        #print("Interval: %.3f seconds" % (interval))
        #print("The flow is: %.3f Liter/min" % (flow))
        flow_converted = (flow / 60) * 1000
        #print("The flow is: %.3f mL/sec" % (flow_converted))
        water_dispensed += flow_converted * interval
        #print("Dispensed: %.3f mL" % (water_dispensed))
        time_elapsed = time.time() - start_time
        #print("time elapsed %.3f" % (time_elapsed))
        count = 0

    # Turn off valve
    GPIO.output(v, GPIO.HIGH) 
    GPIO.cleanup()

    print("Dispensed: %.3f mL" % (water_dispensed))


try:
    main()
finally:
    print("Ensuring all valves are off...")
    GPIO.setmode(GPIO.BOARD)
    for v in valves:
        GPIO.setup(v, GPIO.OUT)
        GPIO.output(v, GPIO.HIGH)
    GPIO.cleanup()

