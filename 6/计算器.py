#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re

a = '1 - 2  *((60-30 +(1-40/5*5+3-2*5/3) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2))'
na = a.replace(" ", "")
print(na)


def replace_kh(string):

    li = re.findall(r"\([^()]+\)", string)
    print(li)
    new_li=[]
    for i in li:
        new_li.append(str(eval(i)))
    for i in range(len(li)):
        new_string=string.replace(li[i],new_li[i])
    print(new_li)
    print(new_string)

replace_kh(na)


