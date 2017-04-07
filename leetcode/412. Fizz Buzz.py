#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
[i for i in n]
利用for循环生成一个列表,列表推导式
字符串+拼接用法
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
"""


def fizzBuzz(n):
    """
    :type n: int
    :rtype: List[str]
    """
    # rt = []
    # for i in range(1, n + 1):
    #     if i % 3 == 0 and i % 15 != 0:
    #         rt.append("Fizz")
    #     elif i % 5 == 0 and i % 15 != 0:
    #         rt.append("Buzz")
    #     elif i % 15 == 0:
    #         rt.append("FizzBuzz")
    #     else:
    #         rt.append(i)
    return [((not i % 3) * "Fizz" + (not i % 5) * "Buzz") or str(i) for i in range(1, n + 1)]


print(fizzBuzz(60))
