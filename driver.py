#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from time import sleep

class Moter:
    def __init__(self, name, pin1, pin2):
        GPIO.setmode(GPIO.BCM)
        self.name = name
        self.mPin = [pin1, pin2]
        for pin in range(len(self.mPin)):
            GPIO.setup(self.mPin[pin], GPIO.OUT)

    def forward(self):
        print("{} forward".format(self.name))
        GPIO.output(self.mPin[0], GPIO.HIGH)
        GPIO.output(self.mPin[1], GPIO.LOW)

    def back(self):
        print("{} back".format(self.name))
        GPIO.output(self.mPin[0], GPIO.LOW)
        GPIO.output(self.mPin[1], GPIO.HIGH)

    def breake(self):
        print("{} breake".format(self.name))
        GPIO.output(self.mPin[0], GPIO.LOW)
        GPIO.output(self.mPin[1], GPIO.LOW)

    def cleanup(self):
        print("{} cleanup".format(self.name))
        GPIO.cleanup(self.mPin[0])
        GPIO.cleanup(self.mPin[1])        

if __name__ == '__main__':
    right = Moter("Right", 20, 21)
    left = Moter("Left", 4, 17)
    try:
        while True:
            print("right forward")
            left.forward()
            sleep(0.5)
            left.breake()
            print("right back")
            left.back()
            sleep(0.5)
            left.breake()
            print("left forward")
            right.forward()
            sleep(0.5)
            right.breake()
            print("left back")
            right.back()
            sleep(0.5)
            right.breake()
    except KeyboardInterrupt:
        print("\nCtl+C")
    except Exception as e:
        print(str(e))
    finally:
        right.cleanup()
        left.cleanup()
        print("\nexit program")
