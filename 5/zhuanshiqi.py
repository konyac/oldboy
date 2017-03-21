#!/usr/bin/env python
# -*- coding:utf-8 -*-
def outer(func):
    def inner():
        print("hello")
        print("hello")
        print("hello")
        r=func()-1
        print("end")
        print("end")
        print("end")
        return r
    return inner

@outer
def f1():
    print("F1")
    return 12
#func=f1
#f1=inner
a=f1()
print(a)
