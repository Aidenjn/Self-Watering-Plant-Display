#!/usr/bin/python
import time
import yaml

# Function: water
# Parameters:
#   feed: Identification number of feed pipe that will dispense.
#   mL: Quantity of water to be dispensed.
# Description:
#   Procedure for dispensing water out of a feed tube.
def water(feed: int, mL: int) -> bool:
    print("Watering ", mL, " mL from feed tube ", feed, ".")

    dispensedWater = 0
    totalTime = 0
    timeOfLastCheck = 0

    # openFeed(feed)

    # Code structure
    while dispensedWater < mL:
        # need to obtain flow rate from water sensor.
        # currentRate = getFlowRate()
        # Dummy code next line for testing
        currentRate = 1

        totalTime = time.clock()
        timeInterval = totalTime - timeOfLastCheck
        timeOfLastCheck = totalTime

        dispensedWater += timeInterval * currentRate

        #print(dispensedWater)

    # closeFeed(feed)
    return True



