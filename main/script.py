#!/usr/bin/env python
from thermometter import Thermometter
from boiler import Boiler

boiler = Boiler()
if boiler.getState() :
    boiler.turnOff()
else:
    boiler.turnOn()

