#!/usr/bin/env python
# -*- coding:utf-8 -*-
def func(d, a1, a2):
    print(a1, a2)
    if d == 10:
        return a1
    a3 = a1 + a2
    return func(d + 1, a2, a3)


ret = func(1, 0, 1)
print(ret)
