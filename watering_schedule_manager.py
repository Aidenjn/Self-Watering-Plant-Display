#!/usr/bin/python
import time
import yaml
import sys

# Global variables
configFile = "config.yaml"

# Class: WateringTask
# Description:
#   Information necessary to perform a scheduled water
#   dispense task.
class WateringTask:
    def __init__(self, feedNumber, taskNumber, GPIO, timeOfDay, mL, daySkip):
        self.feedNumber = feedNumber
        self.taskNumber = taskNumber
        self.GPIO = GPIO
        self.timeOfDay = timeOfDay
        self.mL = mL
        self.daySkip = daySkip


# Function: getTaskObjects
# Description:
#   Reads configuration file and generates a task list for
#   dispensing water from feed tubes.
def getTaskObjects() -> [WateringTask]:
    tasks = []
    with open(configFile) as file:
        feedData = yaml.safe_load(file)
    try:
        for feedNumber in range(0, len(feedData["Feeds"])):
            if ("Tasks" in feedData["Feeds"][feedNumber]):
                print("Feed tube ", feedNumber, " has ", len(feedData["Feeds"][feedNumber]["Tasks"]), " tasks assigned to it.")
                for taskNumber in range(0, len(feedData["Feeds"][feedNumber]["Tasks"])):
                    tasks.append(WateringTask(
                        feedNumber,
                        taskNumber,
                        feedData["Feeds"][feedNumber]["RaspberryPiGPIO"],
                        feedData["Feeds"][feedNumber]["Tasks"][taskNumber]["TimeOfDay"],
                        feedData["Feeds"][feedNumber]["Tasks"][taskNumber]["mL"],
                        feedData["Feeds"][feedNumber]["Tasks"][taskNumber]["DaySkip"]
                        ))
            else:
                print("Feed tube ", feedNumber, " has no tasks assigned to it.")
    except:
        print("Failed to parse config.yaml.")
        print("Make sure that this file follows the required structure.")
        errorInfo = sys.exc_info()[0]
        print("Error:\n", errorInfo)
    return tasks


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



getTaskObjects()



