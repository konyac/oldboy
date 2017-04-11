#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket

ip_port = ('127.0.0.1', 8001)
sk = socket.socket()
sk.connect(ip_port)
while True:
    inp = input(">>>")
    sk.sendall(bytes(inp,encoding="utf-8"))
    print(str(sk.recv(1024),encoding="utf-8"))

