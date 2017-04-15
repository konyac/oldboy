#!/usr/bin/env python
# -*- coding:utf-8 -*-
def square_of_sum(L):
    ret = []
    for i in L:
        ret.append(i*i)
    return sum(ret)


print(square_of_sum([1, 2, 3, 4, 5]))
print(square_of_sum([-5, 0, 5, 15, 25]))