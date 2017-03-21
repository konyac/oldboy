#!/usr/bin/env python
# -*- coding:utf-8 -*-
# a1 = 123
# a2 = 456
# #
# # # temp = a1
# # # a1 = a2
# # # a2 = temp
# # # print(a1, a2)
#
# a1 = a1 + a2
# a2 = a1 - a2
# a1 = a1 - a2
# print(a1, a2)


def BubbleSort(li):
    le = len(li)
    while le > 0:
        for i in range(le - 1):
            if li[i] > li[i + 1]:
                li[i] = li[i] + li[i + 1]
                li[i + 1] = li[i] - li[i + 1]
                li[i] = li[i] - li[i + 1]
        le -= 1
    return li
li = [1, 22, 11, 55, 23, 33, 12, 56, 4, 7]
print(BubbleSort(li))

# for i in range(4):
#     print(i)
