#!/usr/bin/env python
# -*- coding:utf-8 -*-
from multiprocessing import Pool
import time
def myFun(i):
    time.sleep(2)
    return i+100

def end_call(arg):
    print("end_call",arg)

if __name__ == "__main__":

    p = Pool(5)

    # print(p.map(myFun,range(10)))

    for i in range(10):
        p.apply_async(func=myFun,args=(i,),callback=end_call)

    print("end")
    p.close()
    p.join()