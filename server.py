#!/usr/bin/env python
# -*- coding:utf-8 -*-

import argparse
import json
import SimpleHTTPServer
import BaseHTTPServer

from driver import Moter
from time import sleep

left = Moter("Left", 20, 21)
right= Moter("Right", 4, 17)

def message_handle(message):
    if message['right'] == 'forward':
        right.forward()
    elif message['right'] == 'back':
        right.back()
    elif message['right'] == 'breake':
        right.breake()

    if message['left'] == 'forward':
        left.forward()
    elif message['left'] == 'back':
        left.back()
    elif message['left'] == 'breake':
        left.breake()


class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    """
    Received the request as json, send the response as json
    please you edit the your processing
    """
    def do_POST(self):
        try:
            content_len=int(self.headers.get('content-length'))
            request = json.loads(self.rfile.read(content_len).decode('utf-8'))

            message_handle(request)
            
            response = { 'status' : 200,
                         'result' : { 'hoge' : 100,
                                      'bar' : 'bar' }
                        }
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            responseBody = json.dumps(response)

            self.wfile.write(responseBody.encode('utf-8'))
        except Exception as e:
            print("An error occured")
            print("The information of error is as following")
            print(type(e))
            print(e.args)
            print(e)
            response = { 'status' : 500,
                         'msg' : 'An error occured' }

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            responseBody = json.dumps(response)

            self.wfile.write(responseBody.encode('utf-8'))


def importargs():
    parser = argparse.ArgumentParser("Processing CAM COMTROLLER server")

    parser.add_argument('--host', '-H', required=False, default='localhost')
    parser.add_argument('--port', '-P', required=False, type=int, default=8080)

    args = parser.parse_args()

    return args.host, args.port

def run(server_class=BaseHTTPServer.HTTPServer, handler_class=MyHandler, server_name='localhost', port=8080):

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
    right.breake()
    left.breake()
    host, port = importargs()
    run(server_name=host, port=port)

if __name__ == '__main__':
    main()
