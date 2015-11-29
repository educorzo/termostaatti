#!/usr/bin/env python
from thermometter import Thermometter
from boiler import Boiler
import sys

boiler = Boiler()
thermometter = Thermometter()
themperature = float(sys.argv[1])
if thermometter.getTemp() < themperature:
    boiler.turnOn()
else:
    boiler.turnOff()


