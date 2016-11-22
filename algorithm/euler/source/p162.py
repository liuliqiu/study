#!/usr/bin/env python
#-*- coding:utf-8 -*-
from math import factorial

def f(n, is_begin = True, contain_zero = True, number = 3):
    """
    >>> f(3)
    4
    >>> f(4)
    258
    >>> hex(sum(f(i) for i in range(3, 16 + 1)))[2:].upper()
    '3D58725572C62302'
    """
    assert n >= number, "Error"
    if n == 0:return 1
    if n > number:
        x, y = f(n - 1, False, False, number), f(n - 1, False, False, number - 1)
        #print x, y
        if contain_zero:
            result = (16 - number) * x + (number - 1 if is_begin else number) * y
        else:
            result = (15 - number if is_begin else 16 - number) * x + number * y
    else:
        if contain_zero:
            result = factorial(n - 1) * (n - 1)
        else:
            result = factorial(n)
    #print n, contain_zero, number, result
    return result
