#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
    Sum of squares of unitary divisors
    A unitary divisor d of a number n is a divisor of n that has the property gcd(d, n/d) = 1.
    The unitary divisors of 4! = 24 are 1, 3, 8 and 24.
    The sum of their squares is 1^2 + 3^2 + 8^2 + 24^2 = 650.

    Let S(n) represent the sum of the squares of the unitary divisors of n. Thus S(4!)=650.

    Find S(100 000 000!) modulo 1 000 000 009.
"""

"""
    for any 1 <= i, j <= n, gcd(ai, aj) == 1
    S(a1 * a2 * ... * an)
    = 1 + (a1^2 + a2^2 + ... + an^2) + ... + (a1^2 * a2^2 * ... * an^2)
    = (1 + a1^2)(1 +  a2^2)...(1 + an^2)
"""

from eulertools import exp_mod, primes


def prime_count(p, n):
    """
        for all integers below n, the total factor count of p
    """
    result = 0
    while n > 0:
        n = n / p
        result += n
    return result

def S_fac(n, p = 1000000009, primes = primes):
    result = 1
    for v in iter(primes(n)):
        c = prime_count(v, n)
        result = (result * (1 + exp_mod(v , 2 * c, p))) % p
    return result


def main():
    print S_fac(10 ** 7) # 138796677
    #print S_fac(10 ** 5) # 403221585    0.76s
    #print S_fac(10 ** 8) #98792821

if __name__ == "__main__":
    main()
