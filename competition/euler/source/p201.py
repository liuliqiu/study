#!/usr/bin/env python
# -*- coding:utf-8 -*-


def f(S, n):
    """
        >>> f({1,3,6,8,10,11}, 3)
        156
        >>> f({i * i for i in range(1, 101)}, 50)
        1
    """
    L = sorted(S)
    Min, Max = sum(L[0:n]), sum(L[-n:0])
    return sum(v for v in range(Min, Max + 1) if is_only_split(v, S, n))


def is_only_split(v, S, n):
    pass
