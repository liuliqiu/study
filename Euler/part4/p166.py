#!/usr/bin/env python
#-*- coding:utf-8 -*-

from functools import partial
from itertools import product
from operator import add

L = [
        (1, 0,  0,  0,  0,  0,  0,  0),
        (0, 1,  0,  0,  0,  0,  0,  0),
        (0, 0,  1,  0,  0,  0,  0,  0),
        (0, 0,  0,  1,  0,  0,  0,  0),
        (0, 0,  0,  0,  1,  0,  0,  0),
        (0, 0,  0,  0,  0,  1,  0,  0),
        (0, 0,  0,  0,  0,  0,  1,  0),
        (1, 1,  1,  1, -1, -1, -1,  0),
        (0, 0,  0,  0,  0,  0,  0,  1),
        (1, 0,  0, -1,  1,  0, -1,  1),
        (0, 1,  1,  2, -1, -1,  0, -1),
        (0, 0,  0,  0,  0,  1,  1, -1),
        (0, 1,  1,  1, -1,  0,  0, -1),
        (0, 0,  1,  2, -1, -1,  1, -1),
        (1, 0, -1, -1,  1,  1, -1,  1),
        (0, 0,  0, -1,  1,  0,  0,  1),
    ]

def f():
    """
        >>> f()
        7130034
    """
    re = 0
    for a, b, c, d, e, f, g, h in product(*[range(10) for i in range(8)]):
        lst = [
                a + b + c + d - e - f - g,
                a - d + e - g + h,
                b + c + 2 * d - e -f - h,
                f + g - h,
                b + c + d - e - h,
                c + 2 * d - e - f + g - h,
                a - c - d + e + f - g + h,
                0 - d + e + h,
            ]
        if all(map(lambda x:0<=x<=9, lst)):
            re += 1
    return re

def g(op, args):
    return reduce(partial(map, op), args)

def check():
    for i in range(4):
        print g(add, [L[i * 4 + j] for j in range(4)])
        print g(add, [L[i + j * 4] for j in range(4)])
    print g(add, [L[0], L[5], L[10], L[15]])
    print g(add, [L[3], L[6], L[9], L[12]])


if __name__ == "__main__":
    print f()
