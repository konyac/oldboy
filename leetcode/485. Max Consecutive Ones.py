#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
1、我的做法，转化列表中的元素成字符串，然后用split("0")分隔。在去最大值的长度。
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
"""


def findMaxConsecutiveOnes(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # ret="".join([str(i) for i in nums])
    # r=ret.split("0")
    return len(max("".join([str(i) for i in nums]).split("0")))


print(findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
