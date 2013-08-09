#!/usr/bin/env python
#-*- coding:utf-8 -*-

from itertools import count
from eulertools import is_square

def f(n):
    """
    c^2d, cbd, b^2d (c < b)
    cb^3d^2 + c^2b=m^2
    求出所有x = m^2 = cb^3d^2 + c^2b < n (c, b, d, m 为整数)
    >>> sum(set(f(10 ** 5)))
    124657
    >>> sum(set(f(10 ** 12)))
    878454337159
    """
    for b in count(2):
        b3 = b ** 3
        if b3 > n:
            break
        for c in range(1, b):
            for d in count(1):
                x = c * b3 * d * d + c * c * d 
                if x > n:
                    break
                if is_square(x):
                    yield x

