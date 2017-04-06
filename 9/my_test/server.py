#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket

ser = socket.socket()
ser.bind(("127.0.0.1", 9999))
ser.listen(5)

while True:
    conn, addr = ser.accept()
    conn.sendall(bytes("欢迎链接，请输入：q退出：",encoding="utf-8"))
    while True:
        rev = str(conn.recv(1024),encoding="utf-8")
        if rev == "q":
            conn.sendall(bytes("exit", encoding="utf-8"))
            break
        else:
            conn.sendall(bytes("继续输入：",encoding="utf-8"))
    conn.close()
