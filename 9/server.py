#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import socket

ser = socket.socket()  # 创建一个socket对象
ser.bind(("localhost", 9999,))  # server的ip地址和端口
ser.listen(5)  # 监听的次数

while True:
    conn, address = ser.accept()  # accept阻塞。等待获取连接的
    conn.sendall(bytes("欢迎连接", encoding="utf-8"))
    while True:
        ret_bytes = conn.recv(1024)
        send = str(ret_bytes, encoding="utf-8")
        conn.sendall(bytes(send + "好", encoding="utf-8"))
        # print(address, conn)
