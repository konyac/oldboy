#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket, os

obj = socket.socket()
obj.connect(("127.0.0.1", 9999))
ret_bytes = obj.recv(1024)
print(str(ret_bytes, encoding="utf-8"))
file_len = os.stat("icon8.png").st_size
print(file_len)
obj.sendall(bytes(str(file_len), encoding="utf-8"))
print(str(obj.recv(1024),encoding="utf-8"))
with open("icon8.png", "rb") as f:
    for line in f:
        obj.sendall(line)
obj.close()
