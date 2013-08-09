#!/usr/bin/env python
#-*- coding:utf-8 -*-

from itertools import count
from bisect import insort_left
from Crazy import divisor

def f(n):
    """5a^2-b^2=1
    >>> f(1)
    2
    >>> f(2)
    15
    >>> f(3)
    104
    >>> f(4)
    714
    >>> f(10)
    74049690
    >>> f(15)
    1120149658760
    """
    c, x, c_p  = 5, 11, 1
    for i in range(n - 1):
        c, c_p = 3 * x + c_p, c
        x = int((c * c * 5 - 4) ** 0.5)
        assert x * x + 4 == c * c * 5
    return (x - 1) / 5




