#!/usr/bin/env python
# -*- coding:utf-8 -*-
def nextGreaterElement(findNums, nums):
    """
    :type findNums: List[int]
    :type nums: List[int]
    :rtype: List[int]
    """
    for i in findNums:
        del nums[:findNums.index(i)]
        while i < findNums[findNums.index(i)]:
            i += 1

            list.pop()

    return findNums


print(nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
