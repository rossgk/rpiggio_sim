# rpiggio_sim  ![Arppy - Project Mascot](images/arppy_logo_s.png) 


## Overview
*_RPiggio_* is a RaspberryPi General Purpose Input/Output (GPIO) simulator for Python development

### Caveat
This *_RPiggio_* project is in a very early form. Documentation and such is in progress. Watch this space 

### Who Would Use This 
If you're writing some code for an RPi board, but want to draft it on your desktop/laptop machine
before you test it on your hardware, *_RPiggio_* will help you out.
*RPiggio* is a simulator that behaves much as the RPi.GPIO library on the RaspberryPi Hardware.

    This software lets you write code for the RaspberryPi hardware, but thoroughly test
    and debug it before you load it onto the hardware. Invariably we have syntax and algorithm
    mistakes during development. This lets you fix those with your favourite editor/IDE before
    the more tedious copy-over to, and cumbersome debugging environment of, the target hardware.
    
License: Creative Commons - Attribution
You are free to use this code but need to retain this license statement and link to the license terms. 
You need to also acknowledge the author in any use or derivative you create.  
** See license terms to which you are agreeing here: https://creativecommons.org/licenses/by/4.0/

There are other very good RPi GPIO emulator/simulators around - much better than *_RPiggio_*.
The benefit of *_RPiggio_* is that it runs under Python 2.7. That's about it at this point.

If you're using Python 3.x or greater, you're better off going for the create.withcode.uk project
which has nice features, like a graphical display for the GPIOs. 

The *_RPiggio_* code was created from scratch by the author, purely to reproduce the behaviour of the 
RPi hardware on an independent (eg MacOSX) development machine. It should work fine in Python2.7 on any platform.

### Arppy – the Project Mascot
He was born in the open clipart pen on Pixbay.

# To Use RPiggio:
Simply put the rpiggio_sim.py file in the same directory as your new Python2.7 code and evoke it with an import:
    from RPiggio import *                     # add the simulator objects etc
    GPIO = RPi_GPIO_Surrogate()               # Standin for the GPIO init
    
    SW1_PIN = 15                              # choose a GPIO pin to attach a switch to
    GPIO.PIN_SIM[ SW1_PIN ] = HI              # set an initial state

The surrogate GPIO object lets you proceed with normal GPIO cmds, like:

    GPIO.setup(SW3_PIN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)       # Set PullDown
    sleep(2)
    print "Our pin sees: " + str(GPIO.input(SW1_PIN))
    
A better approach for code that transports easily between development and target hardware is to 
conditionally load the simulator versus the real GPIO library on the target hardware. 
Use the platform library in Python:

    import platform
    thisBox = platform.system()
     
    SW1_PIN = 15                                  # choose a GPIO pin to attach a switch to
    
    if thisBox == "Darwin":                       # This detects the MacOSX environment
        from RPiggio import *                     # add the objects etc
        GPIO = RPi_GPIO_Surrogate()               # Standin for the GPIO init
        GPIO.PIN_SIM[ SW1_PIN ] = HI              # set an initial state for simulator on pin 15
    elif thisBox == "Linux":
        import RPi.GPIO as GPIO
    
    # then proceed as per normal RPi code...
    GPIO.setup(SW3_PIN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)       # Set PullDown
    sleep(2)
    print "Our pin sees: " + str(GPIO.input(SW1_PIN))
    
Thus the same code can be run on the RPi without any changes and you can test on your Mac.
(If you're on Windows, you just check the documentation for Platform and detect that.) 

You can even do interrupts. The result is a probablistic event-driven, thread-based interrupt
that calls your designated code block just the same way as the real library does. 
Some sample code is likely required for you to try that. 

Basically it uses the call:
    
    GPIO.add_event_detect( SW1_PIN, GPIO.RISING, callback=interruptRoutine)     # call for an interrupt routine

And then your def gets evoked based on some randomness you'll need to tweak in the library. 

    def interruptRoutine( timeStamp):
        ''' Routine called upon interrupt event'''
        print " INTERRUPT called "

Some nice things can be done with the python Queue library to process threaded events.
_More to come on this later_

