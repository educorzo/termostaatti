#!/usr/bin/env python
import RPi.GPIO as GPIO
import time


class boiler:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(12, GPIO.OUT)
        
    def turnOn():
        GPIO.output(12, True)
    
    def turnOff():
        GPIO.output(12,False)