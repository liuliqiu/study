#!/usr/bin/env python
# -*- coding:utf-8 -*-
from eulertools import GCD


def f(n):
    """
    >>> f(10000)
    48861552
    >>> f(100)
    2438
    """
    k = 2
    l = (k + 1) * ((k + 1.0) / k) ** k
    result = 0
    for i in range(5, n + 1):
        if i >= l:
            k += 1
            l = (k + 1) * ((k + 1.0) / k) ** k
        result += -i if is_terminating(k / GCD(k, i)) else i
    return result


def is_terminating(k):
    for p in (2, 5):
        while k % p == 0:
            k = k / p
    return k == 1
