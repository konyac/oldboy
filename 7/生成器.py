#!/usr/bin/env python
# -*- coding:utf-8 -*-
def consumer():
    r = 'here'
    for i in range(3):
        yield r
        r = '200 OK'+ str(i)
c = consumer()
n1 = c.__next__()
n2 = c.__next__()
n3 = c.__next__()
print(n1,n2,n3)
