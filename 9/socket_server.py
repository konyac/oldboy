#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socketserver


class Myserver(socketserver.BaseRequestHandler):
    def handle(self):
        print(self.request, self.client_address, self.server)
        conn = self.request
        conn.sendall(bytes('欢迎致电 10086，请输入1xxx,0转人工服务.', encoding="utf-8"))
        Flag = True
        while Flag:
            data = conn.recv(1024)
            data = str(data, encoding="utf-8")
            if data == 'exit':
                Flag = False
            elif data == '0':
                conn.sendall(bytes('通过可能会被录音.balabala一大推', encoding="utf-8"))
            else:
                conn.sendall(bytes('请重新输入.', encoding="utf-8"))


if __name__ == "__main__":
    #socket+select+多线程
    #ip和端口，类名
    #Myserver==>RequestHandlerClass
    #obj=self.RequestHandlerClass()
    #obj.handle()  执行我们写的方法
    #ThreadingTCPServer.init=>TCPServer.init()=>BaseTCPServer.init()
    #1、创建server对象
    #   self.server_address         ("127.0.0.1", 9999)
    #   self.RequestHandlerClass    MyServer
    #   self.socket                 创建服务端socket对象
    server = socketserver.ThreadingTCPServer(("127.0.0.1", 9999), Myserver)
    # 2、server对象的server_forever()方法
    #   在BaseServer中
    server.serve_forever()
