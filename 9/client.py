#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import socket

obj = socket.socket()

obj.connect(("127.0.0.1", 9999))
ret_bytes = obj.recv(1024)
print(str(ret_bytes, encoding="utf-8"))
while True:
    inp = input("请输入：")
    obj.sendall(bytes(inp, encoding="utf-8"))
    ret_bytes = obj.recv(1024)
    print(str(obj.recv(1024), encoding="utf-8"))
