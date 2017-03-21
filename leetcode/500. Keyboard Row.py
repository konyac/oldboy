#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
def findWords(words):
    r1 = "qwertyuiopQWERTYUIOP"
    r2 = "asdfghjklASDFGHJKL"
    r3 = "zxcvbnmZXCVBNM"
    rt=[]
    for i in words:
        if set(i).issubset(set(r1)) or set(i).issubset(set(r2)) or set(i).issubset(set(r3)):
            rt.append(i)
    return rt
print(findWords(["Hello", "Alaska", "Dad", "Peace"]))







