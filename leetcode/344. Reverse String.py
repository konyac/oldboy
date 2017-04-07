#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
1、切片[::-1]倒序切片
2、jion，生成一个字符串。添加一个可迭代的参数。
    def join(self, iterable): # real signature unknown; restored from __doc__

        S.join(iterable) -> str

        Return a string which is the concatenation of the strings in the
        iterable.  The separator between elements is S.

        return
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".

Subscribe to see which companies asked this question.
"""
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # ret=""
        # r=[i for i in s]
        # r.reverse()
        # for i in r:
        #     ret+=i
        # return s[::-1]
        s=list(s)
        s.reverse()
        return "".join(s)
        # return s[::-1]
obj=Solution()

print(obj.reverseString("a revocation"))

