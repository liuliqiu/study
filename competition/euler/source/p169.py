#!/usr/bin/env python
# -*- coding:utf-8 -*-

from itertools import count
from eulertools import memoized


@memoized
def f(n):
    """
    >>> f(10 ** 25)
    178653872807L
    >>> f(10)
    5
    """
    if n <= 2:
        return n
    if n % 2 == 1:
        return f(n / 2)
    else:
        return f(n / 2) + f(n / 2 - 1)
