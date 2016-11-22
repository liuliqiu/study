#!/usr/bin/env python
#-*- coding:utf-8 -*-

import math
import operator
from itertools import product, count, imap
from collections import Counter

from eulertools import factorize, factorize_to, primes, extended_eucliean


def g(n, fac_dict):
    t = reduce(operator.mul, (p ** (c / 2) for p, c in fac_dict.items() if c > 1), 1)
    return t, n / (t * t)

def merge_factors(x, y):
    z = x.copy()
    for k, v in y.items():
        if k in z:
            z[k] += v
        else:
            z[k] = v
    return z

def ad_factorize_to(n, m, a, b):
    """
        factorize [a * x + b for x in range(n, m + 1)]
    """
    l = [{} for _ in range(m - n + 1)]
    ps = primes(int((a * m + b) ** 0.5) + 1)
    for _p in ps:
        for i in range(1, int(math.log(a * m + b + 1, _p)) + 1):
            p = _p ** i
            x, y, z = extended_eucliean(p, a)
            if b % z == 0:
                x, y, z = x * (b / z), y * (b / z), b
                t_start = (a * n + b + a * p - z + a * y - 1) / (a * p)
                t_end = (a * m + b + a * p - z + a * y) / (a * p)
                for t in range(t_start, t_end):
                    l[p * t - y - 1][_p] = i
    for i, d in enumerate(l):
        tmp = (a * i + a + b) / reduce(operator.mul, [p ** c for p, c in d.items()], 1)
        if tmp != 1:
            d[tmp] = 1

    return l

def factors(fac_dict):
    l = [[p ** i for i in range(c + 1)] for p, c in fac_dict.items()]
    return map(lambda z:reduce(operator.mul, z, 1), product(*l))

def f(n):
    result = 0
    L = factorize_to(n / 6)
    L_8_3 = ad_factorize_to(1, n / 6, 8, -3)
    for i in xrange(1, n / 6):
        a = 3 * i - 1
        x, y = g(8 * i - 3, L_8_3[i - 1])
        for b in factors(merge_factors(L[i - 1], L[x - 1])):
            c = ((i * x / b) ** 2) * y
            if a + b + c <= n:
                result += 1
    return result


def main():
    #print f(11 * (10 ** 7)) # 18946051      4881.29s
    print f(11 * (10 ** 5))
    #print f(1000)

if __name__ == "__main__":
    main()
