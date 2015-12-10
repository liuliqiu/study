#!/usr/bin/env python
#-*- coding:utf-8 -*-

def _G(n, p = 1000000007):
    a = n ** 0.5
    L = {}
    for i in range(n - int(a) + 1, -1, -1):
        for j in range(int(a), -1, -1):
            if n - i < a * (j + 1):
                L[(i, j)] = 1
            else:
                L[(i, j)] = (L[(i + 1, j)] + L[(i, j + 1)]) % p
    #for j in range(int(a), -1, -1):
    #    print [(i, j, L[(i, j)]) for i in range(n - int(a), -1, -1)]

    return L[(0, 0)]

from eulertools import comb, is_square, big_primes, memoized, inverse_mod, primes

def comb_mod(n, k, m):
    if k > n or k < 0:
        return 0
    k = min(k, n - k)
    r = 1
    s = 1
    for i in range(1, k + 1):
        r = (r * (n - i + 1)) % m
        s = s * i
    return (r * inverse_mod(s, m)) % m


def G(n, p = 1000000007):
    a = n ** 0.5
    result = 0
    flag = is_square(n)
    for i in range(int(a)):
        if flag:
            result += comb_mod(n - int(a * (i + 1)) + i + 1, i + 1, p)
        else:
            result += comb_mod(n - int(a * (i + 1)) + i, i + 1, p)
    return (result + 1) % p

def f():
    m = 1000000007
    return sum(G(p) for p in big_primes(10000000, 10010000)) % m



def main():
    #print G(10 ** 4) # 198888906
    #print G(2 * 10 ** 4) # 47991922
    #print G(10 ** 6) # 361999901
    print f()


if __name__ == "__main__":
    main()
