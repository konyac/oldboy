#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
判断是否符合英文写法。要么都小写，要么都大写，要么首字母大写
str的几个方法。
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital if it has more than one letter, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
Example 1:
Input: "USA"
Output: True
Example 2:
Input: "FlaG"
Output: False
"""

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return word.istitle() or word.isupper() or word.islower()

obj = Solution()
print(obj.detectCapitalUse("FlaG"))