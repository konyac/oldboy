#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import pika

# ########################## 客户端消费者 ##########################

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))  # 客户端链接 rabbitmq
channel = connection.channel()  # 客户端创建句柄

channel.queue_declare(queue='hello')  # 客户端创建，如果服务端没有的话就生效


def callback(ch, method, properties, body):  # 回调函数，这里的参数body是服务端的body内容主体
    print(" [x] Received %r" % body)


channel.basic_consume(callback,#取到这个函数之后。自动执行的。
                      queue='hello',#队列名
                      no_ack=True)  # noack是当客户端取出消息时候 回调函数处理数据时候如果时间长，我们这个参数就是不让其等待，数据不再队列，出问题，数据就没了。如果要求数据性高我们就设置为false 可以让回调函数处理完了，即使中间崩溃了，下次启动取数据还会取的到。

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()