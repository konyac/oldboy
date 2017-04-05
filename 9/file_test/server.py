#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket

sk = socket.socket()
sk.bind(("127.0.0.1", 9999))
sk.listen(5)
f = open("new.png", "wb")
while True:
    conn, address = sk.accept()
    conn.sendall(bytes("欢迎", encoding="utf-8"))
    file_size = str(conn.recv(1024), encoding="utf-8")
    file_len = 0
    while True:
        if int(file_size) == file_len:
            break
        file_rev = conn.recv(1024)
        f.write(file_rev)
        file_len += len(file_rev)
    f.close()
