#!/usr/bin/env python
# -*- coding:utf-8 -*-
from multiprocessing import Process
# from threading import Thread
# import multiprocessing
li = []
def foo(i):
    li.append(i)
    print("say hi",li)

if __name__ == "__main__":
    for i in range(10):
        t = Process(target=foo,args=(i,))
        # p = Thread(target=foo,args=(i,))
        t.start()
        # p.start()
