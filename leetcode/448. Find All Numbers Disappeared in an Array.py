#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""


def findDisappearedNumbers(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    s = set([i for i in range(1,len(nums)+1)])
    return list(s.difference(set(nums)))

print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))