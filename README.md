![](images/arppy_logo_s.png) # rpiggio_sim 
RPiggio is a RaspberryPi General Purpose Input/Output (GPIO) simulator for Python development


RPiggio is a simulator that behaves much as the RPi.GPIO library that is resident on the RaspberryPi Hardware.

    This software lets you write code for the RaspberryPi hardware, but thoroughly test
    and debug it before you load it onto the hardware. Invariably we have syntax and algorithm
    mistakes during development. This lets you fix those with your favourite editor/IDE before
    the more tedious copy-over to, and cumbersome debugging environment of, the target hardware.
    
License: Creative Commons - Attribution
You are free to use this code but need to retain this license statement and link to the license terms. 
You need to also acknowledge the author in any use or derivative you create.  
** See license terms to which you are agreeing here: https://creativecommons.org/licenses/by/4.0/

There are other very good RPi GPIO emulator/simulators around - better than this one.
The benefit of this one is that it runs under Python 2.7. That's about it at this point.

If you're using Python 3.x or greater, you're better off going for the create.withcode.uk project
which has nice features.

The RPiggio code was created from scratch by the author, purely to reproduce the behaviour of the 
RPi hardware on an independent (MacOSX) development machine. 

It should work fine in Python2.7 on any platform.
