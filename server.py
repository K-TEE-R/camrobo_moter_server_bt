#!/usr/bin/env python
# -*- coding:utf-8 -*-

import argparse
import os
from time import sleep

from driver import Moter

left = Moter("Left", 20, 21)
right= Moter("Right", 27, 22)

def handle_message(message):
    if message == 'forward':
        right.forward()
        left.forward()
    elif message == 'back':
        right.back()
        left.back()
    elif message =='right':
        right.brake()
        left.forward()
    elif message =='left':
        right.forward()
        left.brake()
    elif message =='brake':
        right.brake()
        left.brake()

def importargs():
    parser = argparse.ArgumentParser("Processing CAM COMTROLLER server")
    parser.add_argument('--port', '-p', required=False, default='/dev/rfcomm0')
    args = parser.parse_args()
    return args.port

def run(port='/dev/rfcomm0'):
    while True:
        if os.path.exists(port):
            print('Found port {}'.format(port))
            break
        else:
            sleep(1)
    try:
        with open(port) as p:
            while True:
                message = p.readline().strip()
                print('received message {}'.format(message))
                handle_message(message)
    except KeyboardInterrupt:
        print("\nCtl+C")
    except Exception as e:
        print(str(e))
    finally:
        left.cleanup()
        right.cleanup()
        print("\nexit program")

def main():
    right.brake()
    left.brake()
    port = importargs()
    run(port=port)

if __name__ == '__main__':
    main()
