#!/usr/bin/env python
#-*- coding:utf-8 -*-

from collections import defaultdict
from fractions import Fraction

def f(n):
    """
    >>> round(float(f(4)), 6)
    0.464399
    """
    statuses = {tuple(1 for i in range(n)) : Fraction(1, 1)}
    result = 0
    for _ in range(2 ** n - 2):
        new_statuses = defaultdict(Fraction)
        for status, p in statuses.iteritems():
            _sum = sum(status)
            if _sum == 1:
                result += p
            for i, v in enumerate(status):
                if v != 0:
                    new_statuses[cut_in_half(status, i)] += p * Fraction(v, _sum)
        statuses = new_statuses

    return result


def cut_in_half(status, use):
    return tuple(v if i < use else v - 1 if i == use else v + 1 for i, v in enumerate(status))

