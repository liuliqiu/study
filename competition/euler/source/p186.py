#!/usr/bin/env python
# -*- coding:utf-8 -*-
from itertools import count


def f(end=990000):
    """
        >>> f()
        2325629
    """
    G = LaggedFibonacciGenerator()
    D = {}
    for i in range(0, 1000000):
        D[i] = {i}
    number = 0
    while len(D[524287]) < end:
        caller, called = next(G), next(G)
        if caller != called:
            number += 1
            if len(D[called]) > len(D[caller]):
                caller, called = called, caller
            if called not in D[caller]:
                s = D[called]
                D[caller].update(D[called])
                for v in s:
                    D[v] = D[caller]
    return number


def LaggedFibonacciGenerator():
    L = []
    for i in count(1):
        if i <= 55:
            v = (100003 + (300007 * i * i - 200003) * i) % 1000000
            yield v
            L.append(v)
        else:
            index = (i - 1) % 55
            v = (L[(i - 25) % 55] + L[index]) % 1000000
            yield v
            L[index] = v
