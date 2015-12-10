#!/usr/bin/env python
#-*- coding:utf-8 -*-

from eulertools import exp_mod
from functools import partial

def h(lst):
    if not lst:
        return 1
    return reduce(lambda a,b:g(a*b), lst)

def g(v):
    while v % 10 == 0:
        v = v / 10
    return v % 100000

V = h(filter(lambda x:x%10!=0, range(1, 100000)))
_f = partial(filter, lambda x:x%5!=0)

def f(n):
    """
        >>> f(9)
        36288
        >>> f(10)
        36288
        >>> f(20)
        17664
        >>> f(25)
        85984
        >>> f(50)
        60512
    """
    if n <= 10 ** 5:
        return h(range(1, n + 1))
    elif n % 10 == 0:
        x,y = exp_mod(V, (n / (5 ** 5)), 100000) , f(n / 5)
        print x,y
        return g(x * y)

def ff(n):
    """
        >>> ff(1000000)
        12544
        >>> f(1000000000000)
        16576
    """
    if n <= 5 :
        return h(range(1, n + 1))

    k = (n / 20) * 5 + (n / 5) % 4 + 1
    m = (k - 1) * 2
    print k, m
    return int((ff(n / 5) * fg(1, k)* fg(1, m , 2) * fg(m + 1, n  + 1)) % 100000)

def fg(begin, end, step = 1):
    assert end > begin
    assert step in (1, 2)
    if begin > 100000:
        a = begin / 100000
        begin = begin - a * 100000
        end = end - a * 100000
    result = 1
    if end - begin > 100000:
        result *= exp_mod(h(_f(range(begin, begin + 100000, step))), (end - begin) / 100000, 100000)
    return result * h(_f(range(begin, end - (((end - begin) / 100000) * 100000), step)))
