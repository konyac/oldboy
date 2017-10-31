#!/usr/bin/env python
# -*- coding:utf-8 -*-
#100-300之间所有能被3和7整除的所有数之和
sum=0
for i in range(100,301):
    if i%3==0 and i%7==0:
        sum+=i
print(sum)