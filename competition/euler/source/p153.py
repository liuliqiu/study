#!/usr/bin/env python
# -*- coding:utf-8 -*-
from itertools import count
from eulertools import GCD, factorize
from collections import Counter


def Di(n):
    result = 1
    for p, x in Counter(factorize(n)).iteritems():
        result *= (p ** (x + 1) - 1) / (p - 1)
    return result


def f(n):
    """
        if a * a + b * b == n:
            (a, b) in g(k * n) , k in count(1)
            (k * a, k * b) in g(k * n), k in count(1)
        #>>> f(10 ** 8)
        #17971254122360635
        >>> f(5)
        35
        >>> f(10 ** 5)
        17924657155
    """
    result = 0
    di = []
    for i in range(1, n + 1):
        result += Di(i)
        di.append(result)
    for i in count(1):
        if i * i >= n:
            break
        for j in range(1, i + 1):
            if GCD(i, j) == 1:
                v = i * i + j * j
                if v > n:
                    break
                tmp = di[n / v - 1]
                if i == j:
                    result += i * tmp * 2
                else:
                    result += (i + j) * tmp * 2

    return result
