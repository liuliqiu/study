#!/usr/bin/env python
#-*- coding:utf-8 -*-

import operator
from eulertools import is_prime_fast as is_prime, primes

ADD_List = (1, 3, 7, 9, 13, 27)

def f(n):
    """
    #11914460
    >>> sum(f(15 * (10 ** 7)))
    676333270
    >>> sum(f(2000000))
    1242490
    >>> sum(f(100))
    10
    """
    ps = list(primes(5000))
    steps = list(get_steps(ps, n))
    for i in steps:
        if i >= n:
            break
        sq_i = i * i
        if i< n and all(map(lambda x:is_prime(sq_i + x), ADD_List)) and all(map(lambda x:not is_prime(sq_i + x), [11, 17, 19, 21, 23])):
            yield i


def get_steps(ps, n):
    r = {}
    for p in ps:
        s = set(map(lambda x: (x *(p - 1))% p, ADD_List))
        r[p] = [i for i in range(p) if (i *  i ) % p not in s]
    for i in range(n):
        if all(i %p in r[p] for p in ps if p < i * i):
            yield i

if __name__ == "__main__":
    print list(f(100))
