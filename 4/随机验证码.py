#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 生成随机数字，65-90，
# 数字转化成字母，chr(数字)
import random

# i=random.randrange(65,91)  #65<=i<91
# c=chr(i)
# print(i)
# print(c)
# temp=''
# for i in range(4):
#     n=random.randrange(0,4)
#     if n==3 or n==1:
#         rad1=random.randrange(0,10)
#         temp+=str(rad1)
#     else:
#         rad2 = random.randrange(65, 91)
#         temp+=chr(rad2)
#
# print(temp)

temp = ''
for i in range(4):
    num = random.randrange(0, 4)  # 生成0-4的随机数
    if num == 3 or num == 1:  # 如果随机数是1或3，那么在验证码中就生成0-9的随机数
        rad1 = random.randrange(0, 10)
        temp += str(rad1)  # 字符串转换拼接
    else:
        rad2 = random.randrange(65, 91)  # 否则验证码中产生字母
        temp += chr(rad2)
print(temp)
