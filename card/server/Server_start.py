#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socketserver
from conf import settings
from lib import threading_socket_server

print("starting...")


if __name__ == "__main__":
    server = socketserver.ThreadingTCPServer((settings.BIND_HOST,settings.BIND_PORT),threading_socket_server.MyTCPHandler)
    print("server started")
    server.serve_forever()