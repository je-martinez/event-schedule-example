import sched
import time
from logic_1 import logic_1
from logic_2 import logic_2

# Create Scheduler
event_schedule = sched.scheduler(time.time, time.sleep)

# Function Definitions


def doLogic1():
    logic_1()
    event_schedule.enter(1, 1, doLogic1)


def doLogic2():
    logic_2()
    event_schedule.enter(1, 1, doLogic2)


event_schedule.enter(1, 1, doLogic1)
event_schedule.enter(1, 1, doLogic2)
event_schedule.run()
