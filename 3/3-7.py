#!/usr/bin/env python
# -*- coding:utf-8 -*-
dic = {"k1": "v1v1", "k2": [11,22,33,44],"k3":"ca","k4":[11,22]}
def fun(x):
    di={}
    for i,j in x.items():
        # print i,j
        if len(j)>2:
            di[i] = j[:2]
        else:
            di[i] = j
    return di
ret=fun(dic)
print(ret)

