#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
自己的方法意思一样但是复杂了。
直接取4的余数，如果余数为0，则不可能赢。如果余数不为0，则能赢
You are playing the following Nim Game with your friend: There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. You will take the first turn to remove the stones.

Both of you are very clever and have optimal strategies for the game. Write a function to determine whether you can win the game given the number of stones in the heap.

For example, if there are 4 stones in the heap, then you will never win the game: no matter 1, 2, or 3 stones you remove, the last stone will always be removed by your friend.

Hint:

If there are 5 stones in the heap, could you figure out a way to remove the stones such that you will always be the winner?
"""


def canWinNim(n):
    """
    :type n: int
    :rtype: bool
    """
    # return True if 0 in [(n-i)%4 for i in range(1,4)] else False
    return bool(n%4)

print(canWinNim(9))