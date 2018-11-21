#!/usr/bin/env python
# -*- coding:utf-8 -*-

from itertools import count
from eulertools import memoized


def max_sub_triangle(triangle):
    """
    >>> max_sub_triangle(data(1000))
    -271248680
    >>> max_sub_triangle([15, -14, -7, 20, -13, -5, -3, 8, 23, -26, 1, -4, -5, -18, 5, -16, 31, 2, 9, 28, 3])
    -42
    """
    triangle = tuple(triangle)
    for i, v in enumerate(count_triangle_number(), 1):
        if v == len(triangle):
            n = i + 1
            break
        elif v > len(triangle):
            raise Exception()
    result = 0
    for deep, v in enumerate(count_triangle_number(), 1):
        if deep >= n:
            break
        for j in range(deep):
            i = v - deep + j
            tmp = triangle[i]
            for high in range(2, n - deep + 1):
                tmp += sum(
                    triangle[
                        triangle_number(deep + high - 2)
                        + j : triangle_number(deep + high - 2)
                        + j
                        + high
                    ]
                )
                result = min(result, tmp)

    return result


triangle_number = memoized(lambda x: (x * (x + 1)) / 2)


def count_triangle_number():
    for i in count(1):
        yield triangle_number(i)


def data(n):
    """
    >>> list(data(2))
    [273519, -153582, 450905]
    """
    b19 = 2 ** 19
    b20 = b19 * 2
    t = 0
    for i in range(triangle_number(n)):
        t = (615949 * t + 797807) % b20
        yield t - b19
