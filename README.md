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
