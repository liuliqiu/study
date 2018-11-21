#!/usr/bin/env python
# -*- coding:utf-8 -*-

from eulertools import convergent_continued_fraction, skip


def f(n):
    """
    >>> f(24)
    1
    >>> f(100)
    9
    >>> f(10 ** 8)
    10057761
    """
    s = 0
    for a, b, c in generator():
        x = a + b + c
        if x >= n:
            break
        s += (n - 1) / x
    return s


def generator():
    for b, a in skip(convergent_continued_fraction((1, [2])), 1):
        if a * a * 2 - b * b == 1:
            yield (b - 1) / 2, (b + 1) / 2, a
