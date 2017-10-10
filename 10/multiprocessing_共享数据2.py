#!/usr/bin/env python
# -*- coding:utf-8 -*-

from multiprocessing import Process,Manager



def f(i,dic):
    dic[i] = 100  + i
    for k,v in dic.items():
        print(k,v)
    print("end")

if __name__ == "__main__":
    manage = Manager()
    dic = manage.dict()
    for i in range(2):
        p = Process(target=f, args=(i,dic))
        p.start()
        p.join()

