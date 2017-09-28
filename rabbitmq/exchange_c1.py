#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs',exchange_type='fanout')  # 路由器

result = channel.queue_declare(exclusive=True)  # 生成队列

queue_name = result.method.queue  # 生成队列的名称 自己的规则

channel.queue_bind(exchange='logs',
                   queue=queue_name)  # 将队列名称与路由器绑定

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r" % body)


channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)  # 传入队列名称跟回调函数

channel.start_consuming()