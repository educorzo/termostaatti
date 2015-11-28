#!/usr/bin/env python
from thermometter import Thermometter
from boiler import Boiler
import sys

boiler = Boiler()
thermometter = Thermometter()
themperature = sys.argv[1]
if thermometter.getTemp() < themperature:
    if !boiler.getState() :
        boiler.turnOn()
else:
    boiler.turnOff()


