#!/usr/bin/env python
#-*- coding:utf-8 -*-

from math import factorial

"""
          1
        1   1
      1   4   1
    1  11  11   1
  1  26  66  26   1
1  57 302 302  57   1

tri(m, n) = tri(m - 1, n - 1) * (m - (n - 1)) + tri(m - 1, n) * n

p(n) = C(26, n) * tri(n, 2)

"""


def f():
    """
        >>> f()
        409511334375L
    """
    return max(p(n) for n in range(2, 26 + 1))


def p(n):
    """
        >>> p(3)
        10400
        >>> p(2)
        325
    """
    return C(26, n) * g(n)

def C(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))


def g(m):
    if m <= 2:
        return 1
    return (m - 1) + g(m - 1) * 2
