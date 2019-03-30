#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO

class Moter:
    def __init__(self, name, pin1, pin2):
        GPIO.setmode(GPIO.BCM)
        self.name = name
        self.pins = [pin1, pin2]
        for pin in range(len(self.pins)):
            GPIO.setup(self.pins[pin], GPIO.OUT)

    def forward(self):
        print("{} forward".format(self.name))
        GPIO.output(self.pins[0], GPIO.HIGH)
        GPIO.output(self.pins[1], GPIO.LOW)

    def back(self):
        print("{} back".format(self.name))
        GPIO.output(self.pins[0], GPIO.LOW)
        GPIO.output(self.pins[1], GPIO.HIGH)

    def brake(self):
        print("{} brake".format(self.name))
        GPIO.output(self.pins[0], GPIO.LOW)
        GPIO.output(self.pins[1], GPIO.LOW)

    def cleanup(self):
        print("{} cleanup".format(self.name))
        GPIO.cleanup(self.pins[0])
        GPIO.cleanup(self.pins[1])
