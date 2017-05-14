#!/usr/bin/env python
# -*- coding:utf-8 -*-
from multiprocessing import Process,Value,Array

def fun(n,a):
    n.value = 3.14159
    for i in range(len(a)):
        a[i] = -a[i]

if __name__ == "__main__":
    num = Value("d",0.0)
    arr = Array("i",range(10))

    p = Process(target=fun,args=(num,arr,))
    a = Process(target=fun, args=(num, arr,))
    p.start()
    a.start()
    p.join()
    a.join()
    print(num.value)
    print(arr[:])
    # print(type(arr))