#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
给定二叉树，求其最大深度。
最大深度是从根节点到最远节点的最长路径的节点数。
递归的用法
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Subscribe to see which companies asked this question.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return 1+max(map(self.maxDepth,(self.left,self.right))) if root else 0
