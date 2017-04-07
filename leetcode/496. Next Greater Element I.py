#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
下一个最大的数
第一个列表元素都在第二个列表里
第一个元素在第二个列表中之后最近的一个大的元素
1、我的方法是先设定一个列表起始ret为-1，每循环一次加一个-1。然后拿第一个列表中元素去第二个列表中比较，切片的应用，从他目前的位置往后面循环。找到大的然后设置最后的ret中-1 为这个值.如果没有就还是是-1
You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.

Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.
Example 2:
Input: nums1 = [2,4], nums2 = [1,2,3,4].
Output: [3,-1]
Explanation:
    For number 2 in the first array, the next greater number for it in the second array is 3.
    For number 4 in the first array, there is no next greater number for it in the second array, so output -1.
Note:
All elements in nums1 and nums2 are unique.
The length of both nums1 and nums2 would not exceed 1000.
Subscribe to see which companies asked this question.
"""


def nextGreaterElement(findNums, nums):
    """
    :type findNums: List[int]
    :type nums: List[int]
    :rtype: List[int]
    """
    ret = []
    for i in findNums:
        ret.append(-1)
        for m in nums[nums.index(i):]:
            if m > i:
                ret[ret.index(-1,-1)] = m
                break
    return ret
print(nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
