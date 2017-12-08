#  A Library file to emulate the RPi's GPIO library with Python 2.7
#
#    RPiggio - Written and tested on MacOSX
#
#    Author: Ross Kouhi   Created Date: December 2017
#
#  License: Creative Commons - Attribution
#  You are free to use this code but need to acknowledge the author in any use or derivative.
#  ** See license terms to which you are agreeing here: https://creativecommons.org/licenses/by/4.0/
#
#    This software lets you write code for the RaspberryPi hardware, but thoroughly test
#    and debug it before you load it onto the hardware. Invariably we have syntax and algorithm
#    mistakes during development. This lets you fix those with your favourite editor/IDE before
#    the more tedious copy-over to, and cumbersome debugging environment of, the target hardware.
#
#     
#

import threading, time
from Queue import Queue
from random import randint

class SimTrigThread(threading.Thread):
    ''' We're going to use threading to simulate changing inputs that trigger action '''
    # See the detailled examples in the documentation.

    #def __init__(self, evtQueue, event2Call):
    def __init__(self,  event2Call):
        super(SimTrigThread, self).__init__()         # super() will call Thread.__init__ for you
        #self.evtQueue = evtQueue
        self.event2Call = event2Call


    def run(self):
        # Using a probabalistic event triggering approach.
        # We simulate an input change by generating a random number within a range, and acting
        # when that number matches certain values.
        data = ''
        minT = 0
        maxT = 9                                    # min/max times before next event. Random.
        while 1:
            time.sleep(1)                           # waste some time
            nowTime = int(time.time())              # grab clock
            rndValue = randint(minT, maxT)          # random int less than 10

            # choose some arbitrary values, upon which we test for a match
            # If the number matches, we generate an input event.
            if rndValue == 5 or rndValue == 6: # or rndValue == 7:  # three options = 30% chance
                # statistically random event occurs
                print("      *EVT* " )
                #self.event2Call(self.evtQueue, nowTime)            # simulate a callback for queuestuffing
                self.event2Call(nowTime)                            # simulate a callback for queuestuffing



class RPi_GPIO_Surrogate(object):
    ''' The stand-in for the RPi's GPIO interface'''

    INPUT_MODE = 0
    OUTPUT_MODE = 1
    BCM = "BCM Setting"                 # These settings allow the running code to update you on what is happening
    BOARD = "BOARD Setting"
    OUT = "Output mode"
    IN  = "Input mode"
    HIGH = "High state"
    LOW = "Low state"
    FALLING = "FallingEdge"
    RISING = "RisingEdge"
    PUD_UP = 1
    PUD_DOWN = 0

    ActiveInterrupt = False
    InterruptType = None
    PIN_SIM = {1:0, 2:0, 3:0, 4:0, 5:0, 6:1, 7:1, 8:1}              # For setting INPUT values, read by INPUT calls
    PIN_MODES= { }                                                  # will keep modes here, as dictionary
    PIN_UPDOWNS = { }                                               # Pull up or pull down values for pins in this dictionary

    def setmode(self, chosenMode):
        '''Surrogate for pin mode set'''
        if chosenMode == self.BCM or chosenMode == self.BOARD:
            self.mode = chosenMode
            print "    RPi GPIO set to " + chosenMode
        else:
            print "     *** ERROR - no such mode on RPi GPIO"


    def setup(self, pinNumb, pinMode, pull_up_down = None):
        '''Surrogate for the pin direction call'''
        #print "         -> RPi pinSetup with: " + str(pinNumb) + ", " + str(pinMode) + ", " + str(pull_up_down)

        # check for valid pin numbers and valid modes

        print "    RPi pin " + str(pinNumb) + " was set to " + pinMode

        if pinMode == self.IN:
            self.PIN_MODES[pinNumb] = self.INPUT_MODE
        else:
            self.PIN_MODES[pinNumb] = self.OUTPUT_MODE

        if not pull_up_down == None:
            #user is specifying pull-up/pull-dn choices
            self.PIN_UPDOWNS[pinNumb] = pull_up_down              # it's just 1 for up, a 0 for down.
            if pull_up_down == self.PUD_UP:
                print "        ...with a pull_up"
            elif pull_up_down == self.PUD_DOWN:
                print "        ...with a pull_down"
            else:
                print "     *** ERROR unknown pin configuration"


    def output(self, pinNumb, pinState):
        '''Set the initial state for an output pin'''

        # As surrogate for a real RPi, we let writes to an input be used to simulate an input change
        # thus we won't fault a write to an input; But we do flag it and report the input change

        if self.PIN_MODES[pinNumb] == self.INPUT_MODE:
            print "    **EVENT** RPi input pin " + str(pinNumb) + " just changed to: " + str(pinState)
        else:
            print "    RPi output pin " + str(pinNumb) + " was set to: " + str(pinState)

        if pinState == self.HIGH:
            self.PIN_SIM[pinNumb] = 1
        elif pinState == self.LOW:
            self.PIN_SIM[pinNumb] = 0


    def input(self, pinNumb):
        ''' Check the input value and return a value for that input pin
            INPUT pin values get hard coded in debug mode, and changed similarly with an "GPIO.output" cmd'''

        try:
            pinValue = self.PIN_SIM[pinNumb]         # it's one or zero - return what we have
        except:
            self.PIN_SIM[pinNumb] = 0                # if it wasn't defined before, we set it to a zero now
            pinValue = 0                             # use a low value arbitrarily
            print "     ** UNSET PIN was arbitrarily set to 0 upon read attempt"   # Tell us we've arbitrarily set it.

        print "     RPi pin " + str(pinNumb) + " read occurs getting " + str(pinValue)

        return pinValue

    def cleanup(self):
        '''Simulate the clean-up function of the Raspberry Pi'''
        print "    RPi CLEAN-UP called for GPIO functions\n"
        if self.ActiveInterrupt:
            print " Interrupt Cleared "
            self.ActiveInterrupt = False
            # Also kill the thread here... TBD

    def wait_for_edge(self, pinNumb, thisEdge):
        '''Block until falling or rising edges'''
        print "    RPi pin " + str(pinNumb) + " blocking until " + thisEdge

    #def add_event_detect(self, pinNumb, thisEdge, callback, queueName):
    def add_event_detect(self, pinNumb, thisEdge, callback):
        '''Upon this event, run this code - emulates an interrupt  - THREADED'''
        print "    RPi pin " + str(pinNumb) + " triggers routine upon " + thisEdge
        ActiveInterrupt = True
        InterruptType = thisEdge

        evtThread = SimTrigThread(callback)                   # our threaded input event simulator runs in background.
        evtThread.setDaemon(True)
        evtThread.start()                                     # thread is launched - do we need a .join() somewhere near the end below?
