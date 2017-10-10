#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import datetime, time, random


# 10进制转换36进制
def hex36(num):
    # 正常36进制字符应为'0123456789abcdefghijklmnopqrstuvwxyz'，这里我打乱了顺序
    key = 't5hrwop6ksq9mvfx8g3c4dzu01n72yeabijl'
    a = []
    while num != 0:
        a.append(key[int(num) % 36])
        num = num / 36
    a.reverse()
    out = ''.join(a)
    return out


# 获取唯一标识
def getId():
    # 36进制位数对应10进制数范围参考：
    # 1位：0-35
    # 2位：36-1295
    # 3位：1296-46655
    # 4位：46656-1679615
    # 5位：1679616-60466175
    # 6位：60466176-2176782335

    # 只要秒数大于60466175，就可以转换出6位的36进制数，这里从2015年1月1日开始计算，约70年后会变成7位
    d1 = datetime.datetime(2015, 1, 1)
    d2 = datetime.datetime.now()

    # 获取秒数
    s = (d2 - d1).days * 24 * 60 * 60
    # 获取微秒数
    ms = d2.microsecond
    # 随机两位字符串
    id1 = hex36(random.randint(36, 1295))
    # 转换秒数
    id2 = hex36(s)
    # 转换微秒数，加46656是为了保证达到4位36进制数
    id3 = hex36(ms + 46656)

    mId = id1 + id2 + id3
    return mId[::-1]
print(getId())
