#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket
cli = socket.socket()
cli.connect(("127.0.0.1",9999))
rev = str(cli.recv(1024),encoding="utf-8")
print(rev)
while True:
    inp = input("请输入：")
    cli.sendall(bytes(inp,encoding="utf-8"))
    rev = str(cli.recv(1024),encoding="utf-8")
    if rev =="exit":
        print(rev)
        break
    else:
        print(rev)
cli.close()