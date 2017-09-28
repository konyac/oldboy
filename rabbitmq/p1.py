#!/usr/bin/env python
import pika

# ######################### 服务端生产者 #########################

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))  # 链接rabbitmq,封装socket逻辑部分。
channel = connection.channel()  # 生成socket句柄，操作mq的句柄。

channel.queue_declare(queue='hello')  # 创建队列名称为hello 客户端也可以创建，如果服务端没有创建客户端就创建，客户端创建了服务端就不用创建

channel.basic_publish(exchange='',# exchange是个交换机这里的exchange为空时exchange不工作，单独的客户端服务端就只用一个队列来通信
                      routing_key='hello',#队列名字
                      body='Hello World!')  # 这里的exchange为空时exchange不工作，单独的客户端服务端就只用一个队列来通信  注意body主体信息

print(" [x] Sent 'Hello World!'")
connection.close()