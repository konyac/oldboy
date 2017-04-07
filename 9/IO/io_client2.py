#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket

ip_port = ('127.0.0.1', 8002)
sk = socket.socket()
sk.connect(ip_port)
print(str(sk.recv(1024),encoding="utf-8"))
sk.close()
