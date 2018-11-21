#!/usr/bin/env python
# -*- coding:utf-8 -*-
from eulertools import is_square
from collections import defaultdict


def f(n):
    """
    >>> sum(set(map(sum,f(120000))))
    30758397
    >>> sum(map(sum,f(20000)))
    679255
    >>> map(sum, f(1000))
    [784]
    """
    d = defaultdict(set)
    for r in range(2, n):
        for q in range(1, min(r, n - r)):
            if is_square(r * r + r * q + q * q):
                for p in d[q] & d[r]:
                    if p < q and p + q + r <= n:
                        yield p, q, r
                        assert p < q < r
                d[q].add(r)
                d[r].add(q)
