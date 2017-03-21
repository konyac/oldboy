#!/usr/bin/env python
# -*- coding:utf-8 -*-

def n2(start,stop):
    start = start
    while stop:
        yield start
        start +=1
def xrange2(start,stop):
    obj = n2(start,stop)
    for i in range(start,stop):
        j = obj.__next__()
        print(j)
def n1(stop):
    start = 0
    while stop:
        yield start
        start +=1
def xrange1(stop):
    obj = n1(stop)
    for i in range(stop):
        j = obj.__next__()
        print(j)

def xrange(*args):
    if len(args) == 1:
        xrange1(*args)
    elif len(args) == 2:
        xrange2(*args)
    else:
        print("参数不对 1 or 2")

if __name__ == "__main__":
    xrange(2,11)