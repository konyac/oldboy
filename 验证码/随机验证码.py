#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import random

def random_code():
    code = ''
    for i in range(4):
        current = random.randrange(0,4)
        if current != i:
            temp = chr(random.randint(65,90)) #字母
        else:
            temp = random.randint(0,9)#数字
        code += str(temp)
    return code
print(random_code())