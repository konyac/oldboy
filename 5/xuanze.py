#!/usr/bin/env python
# -*- coding:utf-8 -*-
s = [3, 4, 1, 6, 2, 9, 7, 0, 8, 5]

for i in range(len(s)-1):
    index=i                     #选定当前值的索引，作为最小值得索引
    for j in range(i+1,len(s)):    #将这个值以后的值做循环
        if s[index]>s[j]:          #与之后的值一一对比
            index=j                #记下最小元素的下标
    s[i],s[index]=s[index],s[i]    #将最小元素放到列表起始位置
print(s)

# select_sort
# for i in range(0, len(s) - 1):
#     index = i
#     for j in range(i + 1, len(s)):
#         if s[index] > s[j]:
#             index = j
#     s[i], s[index] = s[index], s[i]
#
# # print sort result.
# for m in range(0, len(s)):
#     print(s[m])