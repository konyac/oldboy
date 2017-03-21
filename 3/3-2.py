#!/usr/bin/env python
# -*- coding:utf-8 -*-

st=input("str:")
def count_str(a):
    sz=zm=kg=qt=0
    # temp=str(a)
    for i in a:
        # print i
        if i.isdigit():
            sz+=1
        elif i.isalpha():
            zm+=1
        elif i.isspace():
            kg+=1
        else:
            qt+=1
    return (sz,zm,kg,qt)
result=count_str(st)
print(result)
