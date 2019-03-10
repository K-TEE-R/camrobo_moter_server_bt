#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from time import sleep

class Right:
    def __init__(self, pin1, pin2):
        GPIO.setmode(GPIO.BCM)
        self.mPin = [pin1, pin2]
        for pin in range(len(self.mPin)):
            GPIO.setup(self.mPin[pin], GPIO.OUT)

    def forward(self):
        print("Right forward")
        GPIO.output(self.mPin[0], GPIO.HIGH)
        GPIO.output(self.mPin[1], GPIO.LOW)

    def back(self):
        print("Right back")
        GPIO.output(self.mPin[0], GPIO.LOW)
        GPIO.output(self.mPin[1], GPIO.HIGH)

    def breake(self):
        print("Right breake")
        GPIO.output(self.mPin[0], GPIO.LOW)
        GPIO.output(self.mPin[1], GPIO.LOW)

    def cleanup(self):
        print("Right cleanup")
        GPIO.cleanup(self.mPin[0])
        GPIO.cleanup(self.mPin[1])

class Left:
    def __init__(self, pin1, pin2):
        GPIO.setmode(GPIO.BCM)
        self.mPin = [pin1, pin2]
        for pin in range(len(self.mPin)):
            GPIO.setup(self.mPin[pin], GPIO.OUT)

    def forward(self):
        print("Left forward")
        GPIO.output(self.mPin[0], GPIO.HIGH)
        GPIO.output(self.mPin[1], GPIO.LOW)

    def back(self):
        print("Left back")
        GPIO.output(self.mPin[0], GPIO.LOW)
        GPIO.output(self.mPin[1], GPIO.HIGH)

    def breake(self):
        print("Left breake")
        GPIO.output(self.mPin[0], GPIO.LOW)
        GPIO.output(self.mPin[1], GPIO.LOW)

    def cleanup(self):
        print("Left cleanup")
        GPIO.cleanup(self.mPin[0])
        GPIO.cleanup(self.mPin[1])        

if __name__ == '__main__':
    right = Right(20, 21)
    left = Left(4, 17)
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
