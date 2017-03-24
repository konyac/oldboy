#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
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
obj=Solution()

print(obj.reverseString("a revocation"))

