#!/usr/bin/env python
# -*- coding:utf-8 -*-
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
    return [((not i%3)*"Fizz" + (not i%5)*"Buzz") or str(i) for i in range(1, n+1)]


print(fizzBuzz(60))

