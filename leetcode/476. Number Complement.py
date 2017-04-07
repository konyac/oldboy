#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
给定一个正整数，输出它的补码数。补码策略是翻转二进制表示的位。
1、先计算一个数的2进制位数，然后全部位，在执行异或操作。
Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

Note:
The given integer is guaranteed to fit within the range of a 32-bit signed integer.
You could assume no leading zero bit in the integer’s binary representation.
Example 1:
    Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
Example 2:
Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
"""
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        a=len(bin(num))-2
        sum=0
        for i in range(a):
            sum+=2**i
        return sum^num
r= Solution()
print(r.findComplement(5))