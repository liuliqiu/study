#!/usr/bin/env python
#-*- coding:utf-8 -*-

from itertools import product, combinations
from eulertools import GCD

def _helper(m):
    for x, y in combinations(range(1, m + 1), 2):
        yield x, y, 2
    for x in range(1, m + 1):
        yield x, x, 1


def all_quadrilateral(m):
    for a, c, r1 in _helper(m):
        for b, d, r2 in _helper(m):
            yield a, b, c, d, r1 * r2


gcd = {}
def is_ok(a, b, c, d):
    t = (a + c ) * (b + d ) - gcd[(a, b)] - gcd[(a, d)] - gcd[(c, b)] - gcd[(c, d)]
    x = t / 2. + 1
    return(int(x ** 0.5) ** 2) == x


def f(m):
    for i, j in product(range(1, m + 1), range(1, m + 1)):
        gcd[(i, j)] = GCD(i, j)
    count = sum(r for a, b, c, d, r in all_quadrilateral(m) if is_ok(a, b, c, d))
    print count
    return count

def main():
    #f(4) # 42
    #f(35) # 30747
    f(100) # 694687

if __name__ == "__main__":
    main()
