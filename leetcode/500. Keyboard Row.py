#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
* set的使用
* set子集
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.
Example 1:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
"""


def findWords(words):
    r1 = "qwertyuiopQWERTYUIOP"
    r2 = "asdfghjklASDFGHJKL"
    r3 = "zxcvbnmZXCVBNM"
    rt = []
    for i in words:
        if set(i).issubset(set(r1)) or set(i).issubset(set(r2)) or set(i).issubset(set(r3)):
            rt.append(i)
    return rt


print(findWords(["Hello", "Alaska", "Dad", "Peace"]))
