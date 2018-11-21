#!/usr/bin/env python
# -*- coding:utf-8 -*-
from itertools import islice
from eulertools import skip


def Agx_gener():
    """
    >>> list(islice(Agx_gener(), 20))[-1]
    211345365
    """
    for a, b in skip(g(), 1):
        if b % 5 == 2:
            yield (b - 7) / 5


def g():
    x = h(1, 7, -2)
    y = h(2, 8, -1)
    while True:
        yield next(x)
        yield next(y)


def h(a, b, old_a):
    while True:
        yield a, b
        a, b, old_a = a * 3 - old_a, a * 4 + b - old_a, a


def f(n):
    """
    >>> f(50)
    1298321769070310598775L
    """
    return sum(islice(Agx_gener(), n))
