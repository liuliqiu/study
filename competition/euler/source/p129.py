#!/usr/bin/env python
#-*- coding:utf-8 -*-

from itertools import count
from functools import partial




def first(values, f):
    for i in values:
        if f(i):
            return i



def R(k):
    return sum(10 ** i for i in xrange(k))


def A(n):
    if n%2 ==0 or n%5 == 0:
        return 0
    return first(count(1), lambda i:R(i) % n == 0)

def f1(x):
    return first(count(1), lambda i:A(i) > x)

def f2(x):
    return first(count(x), lambda i:A(i) > x)

def A2(n):
    if n%2 == 0 or n % 5 == 0:
        return 0
    return first(count(1), partial(is_Rk_mod_n, n))

def f3(x):
    return first(count(x), lambda i:A2(i) > x)

def is_Rk_mod_n(n, k):
    left = 1
    s = left
    for i in range(k):
        left = (left * 10) % n
        s += left
    return s % n == 0

def f(x):
    for i in count(x):
        if i%2 ==0 or i % 5 == 0:
            continue
        left = 1
        s = left
        for j in range(i + 2):
            left = (left * 10) % i 
            s = (s + left) % i
            if s == 0:
                break
        if j + 2 > x:
            return i


# if R(k) % n == 0: R(i * k) % n == 0
# A(m) = x, A(n) = y, => R(x)% m == 0, R(y) % n == 0 => R(x * y) %m == 0, R(x * y) % n == 0, R(x* y) % (m * n) == 0, A(m * n) <= x * y if gcd(m, n) == 1
# R(x * x) 
# => A(n) <= n


def main():
    test_num = 1000000
    print f(test_num)
    #print f(10)

if __name__ == "__main__":
    main()
