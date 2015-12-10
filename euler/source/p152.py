#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
    Writing 1/2 as a sum of inverse squares
    How many ways are there to write the number 1/2 as a sum of inverse squares using distinct integers between 2 and 80 inclusive?

    {2,3,4,5,7,12,15,20,28,35}
    {2,3,4,6,7,9,10,20,28,35,36,45}
    {2,3,4,6,7,9,12,15,28,30,35,36,45}

    >>> f(1/2, 2, 80)
    ?
    >>> f(1/2, 2, 45)
    3

"""

from fractions import Fraction
from itertools import combinations
from eulertools import factorize, memoized

FS = [Fraction(1, x * x) for x in range(2, 80 + 1)]

def f(val, min_, max_):
    """
        #>>> f(Fraction(1, 2), 2, 80)
        0
        >>> f(Fraction(1, 2), 2, 45)
        3
    """
    print val, min_, max_
    if val == 0:
        return 1
    elif val < FS[max_ - 2] or max_ < min_:
        return 0
    else:
        return f(val, min_ + 1, max_) + f(val - FS[min_ - 2], min_ + 1, max_)

def all_combinations(l):
    for i in range(1, len(l) + 1):
        for x in combinations(l, i):
            yield x

def g(val, min_, max_):
    median = 7
    for c in all_combinations(range(min_, median)):
        x = sum(Fraction(1, v * v) for v in c)
        if val - x < sum(Fraction(1, v * v) for v in range(median, max_ + 1)):
            print val - x, median, max_
            #g(val - x, median, max_)


def main():
    print g(Fraction(1, 2), 2, 80)

if __name__ == "__main__":
    main()
