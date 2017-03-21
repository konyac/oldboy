#!/usr/bin/env python
# -*- coding:utf-8 -*-

def hammingDistance(num):
    a=len(bin(num))-2
    sum=0
    for i in range(a):
        sum+=2**i
    return sum^num
print(hammingDistance(1))









