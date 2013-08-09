#!/usr/bin/env python
#-*- coding:utf-8 -*-

from eulertools import primes, exp_mod, timer

@timer
def f(n):
    """
    >>> f(100000)
    453647705
    """
    return sum(p for p in primes(n) if not is_factor_R_10_n(p))


def is_factor_R_10_n(p):
    """测试p是否是R(10**n) {n 为自然数}的因子
    >>> is_factor_R_10_n(3)
    False
    >>> is_factor_R_10_n(11)
    True
    >>> is_factor_R_10_n(17)
    True
    >>> is_factor_R_10_n(41)
    True
    >>> is_factor_R_10_n(73)
    True
    """
    print p
    # g(k) = sum(a[k] ** i for i in range(10)) % p
    # a[0] = 10
    # a[n] = 10 ** (10 ** n)
    # a[n + 1] = 10 ** (10 ** (n + 1)) = 10 ** ((10 ** n) * 10) = a[n] ** 10
    a = 10
    is_cycle = set()
    while True:
        if sum(exp_mod(a, i, p) for i in range(10)) % p== 0:
            return True
        if a % p in is_cycle:
            return False
        is_cycle.add(a % p)
        a = exp_mod(a, 10, p)
