#!/usr/bin/env python
# -*- coding:utf-8 -*-

from eulertools import convergent_continued_fraction, skip


def f(n):
    """
    >>> f(12)
    1118049290473932
    """
    s, index = 0, 0
    for a, b in skip(convergent_continued_fraction((2, [4])), 1):
        if b * b * 5 - a * a == 1:
            s += b
            index += 1
            if index >= n:
                return s
