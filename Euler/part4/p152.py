#!/usr/bin/env python
#-*- coding:utf-8 -*-

from fractions import Fraction
from eulertools import factorize


def f(val, min_, max_):
    """
        #>>> f(Fraction(1, 2), 2, 80)
        0
        >>> f(Fraction(1, 2), 2, 45)
        3
    """
    A = []
    tmp = 0
    for v in reversed(range(min_, max_ + 1)):
        tmp += Fraction(1, v * v)
        A.insert(0, tmp)


    next_number = {}
    i = min_
    while i < max_:
        j = i + 1
        while len(set(factorize(j)) - set([2,3,5,7])) != 0:
            j += 1
        if j <= max_:
            next_number[i] = j
        i = j
    queue = [(val, min_)]
    index = 0
    counter = 0
    while index < len(queue):
        val, now = queue[index]
        print now, index
        remain = A[now - min_]
        if val == remain or val == 0:
            counter  += 1

        if val == remain or val == 0:
            counter += 1
        elif 0 < val < remain:
            if val + val > remain:
                val = remain - val
            if now < max_:
                queue.append((val, next_number[now]))
                queue.append((val - Fraction(1, now * now), next_number[now]))

        index += 1

    return counter


def main():
    print f(Fraction(1, 2), 2, 45)

if __name__ == "__main__":
    main()
