#!/usr/bin/env python
# -*- coding:utf-8 -*-
from multiprocessing import Process


def fun(name):
    print("hello", name)


if __name__ == "__main__":
    t = Process(target=fun, args=("bob",))
    t.start()
    t.join()
