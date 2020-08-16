#!/usr/bin/env python
# -*- coding:utf-8 -*-

import argparse
import json
import SimpleHTTPServer
import BaseHTTPServer

from driver import Moter
from time import sleep

left = Moter("Left", 20, 21)
right= Moter("Right", 27, 22)

def message_handle(message):
    if message['right'] == 'forward':
        right.forward()
    elif message['right'] == 'back':
        right.back()
    elif message['right'] == 'brake':
        right.brake()
    if message['left'] == 'forward':
        left.forward()
    elif message['left'] == 'back':
        left.back()
    elif message['left'] == 'brake':
        left.brake()

class HTTPHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            content_len=int(self.headers.get('content-length'))
            request = json.loads(self.rfile.read(content_len).decode('utf-8'))
            message_handle(request)
            response = {'status':200}
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            responseBody = json.dumps(response)
            self.wfile.write(responseBody.encode('utf-8'))
        except Exception as e:
            print("ERROR!!")
            print(type(e))
            print(e.args)
            print(e)
            response = { 'status' : 500,
                         'msg' : 'Failed to handle message.' }
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            responseBody = json.dumps(response)
            self.wfile.write(responseBody.encode('utf-8'))

def importargs():
    parser = argparse.ArgumentParser("Processing CAM COMTROLLER server")
    parser.add_argument('--server_name', '-s', required=False, default='localhost')
    parser.add_argument('--port', '-p', required=False, type=int, default=8080)
    args = parser.parse_args()
    return args.server_name, args.port

def run(server_class=BaseHTTPServer.HTTPServer, handler_class=HTTPHandler, server_name='localhost', port=8080):
    try:
        server = server_class((server_name, port), handler_class)
        server.serve_forever()
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
    server_name, port = importargs()
    run(server_name=server_name, port=port)

if __name__ == '__main__':
    main()
