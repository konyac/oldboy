#!/usr/bin/env python
# -*- coding:utf-8 -*-
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2 ** 31 and x > -(2 ** 31):
            s = list(str(x))
            while s[-1] == "0":
                del s[-1]
            list.reverse(s)
            if s[-1] == "-":
                s.pop()
                s.insert(0, "-")
            a = ""
            for i in s:
                a = a + i
            n = int(a)
            if n < 2 ** 31 and n > -(2 ** 31):
                return n
            else:
                return 0
        else:
            return 0
