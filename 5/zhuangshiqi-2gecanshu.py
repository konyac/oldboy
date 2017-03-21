#!/usr/bin/env python
# -*- coding:utf-8 -*-
def outer(func):
    def inner(a1,a2):
        print("123")
        r=func(a1,a2)
        print("456")
        return r
    return inner

@outer
def index(a1,a2):
    print("非常复杂")
    return a1+a2

# index(2,6)
r=index(2,7)
# print(r)