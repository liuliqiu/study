#!/usr/bin/env python
# -*- coding:utf-8 -*-
from itertools import combinations_with_replacement, product


def f(m, n):
    """
    >>> f(3, 3)
    87
    >>> f(1, 1)
    1
    >>> f(2, 1)
    4
    >>> f(3, 1)
    8
    >>> f(2, 2)
    18
    >>> f(3, 2)
    37
    """
    if n > m:
        return f(n, m)
    result = 0
    for a, b in combinations_with_replacement(range(1, 2 * n), 2):
        if a > n:
            continue
        o_num, e_num = odd_even_count(a, 2 * n - b)
        tmp_o = o_num * ((2 * m + 1 - (a + b)) / 2)
        tmp_p = e_num * (m - (a + b - 1) / 2)
        tmp = tmp_o + tmp_p
        result += tmp
        if a != b:
            result += tmp
    result += g(m, n)
    return result


def h(m, n):
    """
    >>> h(47, 43)
    846910284
    >>> h(3, 2)
    72
    """
    return sum(f(a, b) for a, b in product(range(1, m + 1), range(1, n + 1)))


def g(m, n):
    return sum((m - i) * (j + 1) for i in range(m) for j in range(n))


def odd_even_count(a, b):
    if b < a:
        return 0, 0
    e_a = (a - 1) / 2
    o_a = e_a + (a - 1) % 2
    e_b = b / 2
    o_b = e_b + b % 2
    return o_b - o_a, e_b - e_a
