#!/usr/bin/env python
# -*- coding:utf-8 -*-

from itertools import count


def f(mx):
    """
        >>> sum(f(1000000 - 1)) - 1
        14489159
    """
    s = [dgr(i + 1) for i in range(mx)]
    for i in range(2, mx + 1):
        for j, v in zip(count(2), range(2 * i, mx + 1, i)):
            if s[i - 1] + s[j - 1] > s[v - 1]:
                s[v - 1] = s[i - 1] + s[j - 1]
    return s


def dgr(n):
    re = sum(map(int, str(n)))
    return re if re < 10 else dgr(re)
