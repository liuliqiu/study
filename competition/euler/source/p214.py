#!/usr/bin/env python
# -*- coding:utf-8 -*-
from eulertools import primes, GCD, factorize
from itertools import combinations
from operator import add, sub, mul
from collections import defaultdict


def f(n, limit):
    """
        >>> f(25, 40000000)
        1677366278943
        >>> f(4, 30)
        12
        >>> f(10, 4000)
        93430
        >>> f(14, 200000)
        59846083
    """
    re = 0
    L = range(1, limit + 1)  # L[i-1] = fai(i)
    B = [True] * (limit - 1)  # B[i-2] == is_prime i
    V = [1]  # V[i-1] = deep
    for i in range(2, limit + 1):
        if B[i - 2]:
            L[i - 1] -= 1
            for j in range(i * 2, limit + 1, i):
                B[j - 2] = False
                L[j - 1] = L[j - 1] - L[j - 1] / i
        V.append(V[L[i - 1] - 1] + 1)
        if B[i - 2] and V[-1] == n:
            re += i
    return re
