#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
字符串分隔的用法。lambda函数用法。join用法
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.
"""
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # st=""
        # ret = s.split(" ")
        # r = [i[::-1] for i in ret]
        # for i in r:
        #     st+=i+" "
        # return st.rstrip()
        return " ".join(map(lambda x: x[::-1], s.split()))
        # return ' '.join([i[::-1] for i in s.split()])
obj = Solution()
print(obj.reverseWords("Let's take LeetCode contest"))

print("_".join(["abc","ef"]))
print("_".join("alex li"))