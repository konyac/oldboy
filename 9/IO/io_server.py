#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket, select,sys

sk1 = socket.socket()
sk1.bind(("127.0.0.1", 8001))
sk1.listen()

# sk2 = socket.socket()
# sk2.bind(("127.0.0.1", 8002))
# sk2.listen()
#
# sk3 = socket.socket()
# sk3.bind(("127.0.0.1", 8003))
# sk3.listen()

# inputs = [sk1, sk2, sk3, ]
inputs = [sk1, ]
outputs = []
message_dict = {}
while True:
    #[sk1,sk2,sk3,],select内部自动监听sk1，sk2，sk3两个对象，一旦某个句柄发生变化
    #如果有人连接sk1,或sk2
    #r_list = [sk1，]
    #如果有人第一次连接，sk1发生变化

    #select内部自动监听socket对象，一旦socket变化感知到有新的连接，或者sk1有另外一个人连接变化
    #例如 A：[sk1,A].B 来连接的时候sk1server对象变化了，把B加进去.[sk1,A,B,]
    #r_list=[sk1,],A,B 连接一次后没发送消息
    #B连接后发生消息了，r_list=[B,] 了
    r_list,w_list,e_list = select.select(inputs,outputs,[],1)
    print("正在监听socketserver对象%d" % len(inputs))
    print(r_list)
    for sk_or_conn in r_list:
        # conn,address = sk.accept()
        # conn.sendall(bytes("hello",encoding="utf-8"))
        # conn.close()
        #每一个连接对象
        if sk_or_conn == sk1:
            #表示新用户连接,将新用户的conn加到inpus里
            conn, address = sk_or_conn.accept()
            message_dict[conn] = []
            inputs.append(conn)
        else:

            #老用户发消息了
            try:
                data_bytes = sk_or_conn.recv(1024)
            except Exception as ex:
                #如果用户中断了连接
                inputs.remove(sk_or_conn)
            else:
                #用户正常发消息
                data_str = str(data_bytes, encoding="utf-8")
                message_dict[sk_or_conn].append(data_str)
                # sk.sendall(bytes(data_str + "好", encoding="utf-8"))
                outputs.append(sk_or_conn)

    #仅仅保存了谁给我发过消息
    for conn in w_list:
        recv_str = message_dict[conn][0]
        del message_dict[conn][0]
        conn.sendall(bytes(recv_str+"hello",encoding="utf-8"))
        outputs.remove(conn)

    for sk in e_list:
        inputs.remove(sk)