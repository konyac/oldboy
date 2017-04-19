#!/usr/bin/env python
# -*- coding:utf-8 -*-
import queue
import threading


message = queue.Queue(10)


def producer(i):#生产者
    # while True:
    #     message.put(i)
    print("put:",i)
    message.put(i)


def consumer(i):#消费者
    # while True:
    #     msg = message.get()
    while True:
        msg = message.get()
        print(msg)


for i in range(12):
    t = threading.Thread(target=producer, args=(i,))
    t.start()

for i in range(10):
    t = threading.Thread(target=consumer, args=(i,))
    t.start()