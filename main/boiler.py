#!/usr/bin/env python
import RPi.GPIO as GPIO
import time


class Boiler:
    
    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(12, GPIO.OUT)
        
    def turnOn(self):
        GPIO.output(12, True)
    
    def turnOff(self):
        GPIO.output(12,False)

    def getState(self):
        return GPIO.input(12)