#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import random

total = 100
li = [i for i in range(total)]
res = []
num = 20
for i in range(num):
    t = random.randint(i, total - 1)
    res.append(li[t])
    li[t], li[i] = li[i], li[t]
print(res)
