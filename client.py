#!/usr/bin/env python
# -*- coding:utf-8 -*-

import argparse
import json
import requests

CTRL_C = 3
KEY_H = 104
KEY_J = 106
KEY_K = 107
KEY_L = 108
KEY_B = 98

def getch():
    import sys
    import tty
    import termios

    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        return sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)

def main():
    print("Welcome to CAM CONTROLLER!!")

    parser = argparse.ArgumentParser("Processing target host host")

    parser.add_argument('--host', '-H', required=False, default='localhost')
    parser.add_argument('--port', '-P', required=False, type=int, default=8080)

    args = parser.parse_args()

    url = "http://" + str(args.host) + ":" + str(args.port)
    print(url)
    response = None

    headers = {'content-type': 'application/json'}

    while True:
        try:
            key = ord(getch())
            if key == CTRL_C:
                break
            print(key)

            if key == KEY_J:
                payload = {"right":"forward", "left":"forward"}
                response = requests.post(url, headers=headers, data=json.dumps(payload))
            
            if key == KEY_K:
                payload = {"right": "back", "left":"back"}
                response = requests.post(url, headers=headers, data=json.dumps(payload))
        
            if key == KEY_H:
                payload = {"right": "breake", "left":"forward"}
                response = requests.post(url, headers=headers, data=json.dumps(payload))
        
            if key == KEY_L:
                payload = {"right": "forward", "left":"breake"}
                response = requests.post(url, headers=headers, data=json.dumps(payload))


            if key == KEY_B:
                payload = {"right": "breake", "left":"breake"}
                response = requests.post(url, headers=headers, data=json.dumps(payload))

        except ValueError:
            print("Exception")
    

if __name__ == "__main__":
    main()
