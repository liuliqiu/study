#!/usr/bin/env python
#-*- coding:utf-8 -*-

from eulertools import primes
from itertools import count
from operator import add, sub, mul


def f(LIMIT = 2 ** 50):
    Ps = list(primes(int(LIMIT ** 0.5) + 1))
    result = LIMIT
    for k in count(1):
        op = sub if k % 2 == 1 else add
        if reduce(mul, Ps[:k]) ** 2 > LIMIT:
            break
        for ps in get_sub(Ps, k, LIMIT):
            result = op(result, LIMIT / (reduce(mul, ps) ** 2))
    return result

def get_sub(Ps, k, LIMIT):
    status = range(k)
    while True:
        if reduce(mul, map(lambda i:Ps[i], status)) ** 2 >= LIMIT:
            if k == 1:
                return
            else:
                for j in range(k -1, 1, -1):
                    if status[j] - status[j-1] > 1:
                        status[j-1:] = range(status[j-1] + 1, status[j-1] + k - j + 1)
                else:
                    return
        yield tuple(map(lambda i:Ps[i], status))
        status[-1] += 1
        if status[-1] >= len(Ps):
            return

print f(2 ** 50)
#print f(40)
