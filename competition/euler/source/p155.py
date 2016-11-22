#!/usr/bin/env python
#-*- coding:utf-8 -*-

from fractions import Fraction
from collections import defaultdict
from itertools import product


def D(n):
    """
    >>> D(18)
    3857447
    >>> D(1)
    1
    >>> D(2)
    3
    >>> D(3)
    7
    """
    M = defaultdict(set)
    M[1].add(Fraction(1, 1))
    for use_unit in range(2, n + 1):
        for i in range(1, n / 2 + 1):
            for a, b in product(M[i], M[use_unit - i]):
                M[use_unit].update((a + b, (a * b) / (a + b)))
    return len(reduce(set.union, M.values()))

