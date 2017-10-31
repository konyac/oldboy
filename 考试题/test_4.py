#!/usr/bin/env python
# -*- coding:utf-8 -*-
#将字符串"老男人"转化成utf-8编码的字节类型
str="老男人"
new_byte=bytes(str,encoding="utf-8")
print(new_byte)