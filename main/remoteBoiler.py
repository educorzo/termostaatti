#!/usr/bin/env python
import RPi.GPIO as GPIO
import urllib2


class Boiler:
        
    def turnOn(self):
        urllib2.urlopen("192.168.1.141/on").read()
    
    def turnOff(self):
        urllib2.urlopen("192.168.1.141/off").read()

    def getState(self):
        return urllib2.urlopen("192.168.1.141/check").read()