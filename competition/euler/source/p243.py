#!/usr/bin/env python
#-*- coding:utf-8 -*-

import operator

from eulertools import primes


def g(s, k):
    for n in k:
        s = (s * (n - 1)) / n
    return s

def h(n):
    ps = primes(n)
    for i in range(1, len(ps)):
        p = ps[i]
        fs = ps[:i]
        base = reduce(operator.mul, fs)
        for j in range(1, p):
            yield g(base * j, fs), base * j - 1

def f(_a, _b):
    for a, b in h(100):
        if _a * b > a * _b:
            return b + 1



def main():
    print f(15499, 94744)

if __name__ == "__main__":
    main()
