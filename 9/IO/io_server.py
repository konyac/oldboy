#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket, select

sk1 = socket.socket()
sk1.bind(("127.0.0.1", 8001))
sk1.listen()

sk2 = socket.socket()
sk2.bind(("127.0.0.1", 8002))
sk2.listen()

sk3 = socket.socket()
sk3.bind(("127.0.0.1", 8003))
sk3.listen()

inputs = [sk1, sk2, sk3, ]
while True:
    #[sk1,sk2,sk3,],select内部自动监听sk1，sk2，sk3两个对象，一旦某个句柄发生变化
    #如果有人连接sk1,或sk2
    #r_list = [sk1，sk2]
    r_list,w_list,e_list = select.select(inputs,[],[],1)
    for sk in r_list:
        conn,address = sk.accept()
        conn.sendall(bytes("hello",encoding="utf-8"))
        conn.close()
