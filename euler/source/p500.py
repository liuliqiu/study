#!/usr/bin/env python
#-*- coding:utf-8 -*-

from eulertools import primes
import math


def f(n, m):
    ps = list(primes(int(math.log(n) + 2) * n + 2))
    result = 1
    possible = {1: 0}
    count = 0
    for p in ps:
        for k, j in possible.items():
            v = ps[j] ** (2 ** k)
            if v < p:
                possible[k] += 1
                if k + 1 not in possible:
                    possible[k + 1] = 0

                result = (result * v) % m
                count += 1
                if count == n:
                    return result

        result = (result * p) % m
        count += 1
        if count == n:
            return result


def main():
    n = 500500
    print f(n, 500500507) # 35407281

if __name__ == "__main__":
    main()
