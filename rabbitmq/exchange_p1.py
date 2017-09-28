#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#发布者


import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs',exchange_type='fanout')
# exchange交换机，起个名字logs我们来命名的。订阅发布模式 ，由路由器名称logs来选择队列分发消息

message = ' '.join(sys.argv[1:]) or "info: Hello World!"
# sys.argv命令行参数List，第一个元素是程序本身路径
# 消息为实行脚本或者不跟参数
channel.basic_publish(exchange='logs',  # 交换机的名字。
                      routing_key='',  # 不需要队列名字了
                      body=message)  # 绑定路由器 跟发送信息
print(" [x] Sent %r" % message)

connection.close()