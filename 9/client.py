#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket


ip_port = ('127.0.0.1',9999)
sk = socket.socket()
sk.connect(ip_port)
sk.settimeout(5)
data = str(sk.recv(1024),encoding="utf-8")
print('receive:',data)
while True:
    inp = input('please input:')
    sk.sendall(bytes(inp,encoding="utf-8"))
    if inp == 'exit':
        print(str(sk.recv(1024),encoding="utf-8"))
        break
    else:
        print(str(sk.recv(1024), encoding="utf-8"))
sk.close()



