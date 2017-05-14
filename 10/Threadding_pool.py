#!/usr/bin/env python
# -*- coding:utf-8 -*-
import queue, threading
import time


class ThreadPool():
    def __init__(self, max_num):
        self.queue = queue.Queue(max_num)
        for i in range(max_num):
            self.queue.put(threading.Thread)

    def get_thread(self):
        return self.queue.get()

    def add_thread(self):
        self.queue.put(threading.Thread)


def fun(pool, a):
    time.sleep(1)
    print(a)
    pool.add_thread()


p = ThreadPool(5)
for i in range(20):
    ret = p.get_thread()
    t = ret(target=fun, args=(p, i))
    t.start()
    # t.join()
