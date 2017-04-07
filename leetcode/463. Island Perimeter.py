#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
1、zip的用法，zip（*agrs）
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have
[[0,1,0,0],

You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:
 [[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16
Explanation: The perimeter is the 16 yellow stripes in the image below:
"""



def islandPerimeter(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """

    sm=yel=0
    # zp=zip(*grid)
    for i in grid + [list(x) for x in zip(*grid)]:
        # print(i)
        sm=sm+i.count(1)
        for j in range(len(i)-1):
            if i[j]+i[j+1]==2:
                yel+=1
    return sm*2-yel*2
print(islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))




