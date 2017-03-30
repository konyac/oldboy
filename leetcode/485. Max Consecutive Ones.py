#!/usr/bin/env python
# -*- coding:utf-8 -*-
def findMaxConsecutiveOnes(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # ret="".join([str(i) for i in nums])
    # r=ret.split("0")
    return len(max("".join([str(i) for i in nums]).split("0")))

print(findMaxConsecutiveOnes([1,1,0,1,1,1]))