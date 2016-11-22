#!/usr/bin/env python
#-*- coding:utf-8 -*-

from operator import mul


def f(n):
    """
    >>> f(10)
    4112
    >>> sum(f(i) for i in range(2, 16))
    371048281
    """
    return int(reduce(mul, ((2. * i / (n + 1)) ** i for i in range(1, n+1))))
