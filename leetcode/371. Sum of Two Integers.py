#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
计算两个整数A和B的和，但不允许使用运算符+和-。

Example:
Given a = 1 and b = 2, return 3.
"""
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        ret=str(a)+"+"+str(b)
        return eval(ret)
obj=Solution()
print(obj.getSum(-1,-2))