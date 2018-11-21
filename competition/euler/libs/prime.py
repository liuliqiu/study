# -*- coding:utf-8 -*-

from random import randint

from eulertools import exp_mod


def is_prime(n):
    if n == 1:
        return False
    if n % 2 == 0:
        return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def primes(n):
    if n < 2:
        raise StopIteration
    else:
        yield 2
        l = [True for i in range((n - 1) // 2)]
        for i in range(len(l)):
            if l[i]:
                yield 2 * i + 3
                for j in range(3 * i + 3, len(l), 2 * i + 3):
                    l[j] = False


FAST_TEST_COUNT = 10


def _primality_test(n):
    x = randint(2, n - 1)
    k = 0
    q = n - 1
    while q % 2 == 0:
        k += 1
        q /= 2
    j = 0
    y = exp_mod(x, q, n)
    while j < k:
        if y == n - 1 or (y == 1 and j == 0):
            return True
        if y == 1 and j > 0:
            return False
        j += 1
        y = (y * y) % n
    return y == 1


def is_prime_fast(n):
    """
    >>> all(is_prime_fast(p) for p in primes(100000))
    True
    >>> all(not is_prime_fast(p) for p in xrange(2, 100000) if p not in set(primes(100000)))
    True
    """
    if n < 10:
        return n in (2, 3, 5, 7)
    else:
        return all(_primality_test(n) for i in range(FAST_TEST_COUNT))


def big_primes(begin, end, smallprimes=None):
    """求begin 到end之间的所有素数，使用smallprimes试除"""
    if smallprimes == None:
        smallprimes = list(primes(int(end ** 0.5)))
    if 2 in smallprimes:
        smallprimes.remove(2)
    if begin < 2:
        begin = 3
    if begin == 2:
        yield 2
    if begin % 2 == 0:
        begin += 1
    if end % 2 == 0:
        end -= 1
    B = [True] * ((end - begin + 2) // 2)
    for p in smallprimes:
        temp = ((begin + p - 1) // p) * p
        if temp % 2 == 0:
            temp += p
        if temp == p:
            temp += 2 * p
        for j in range((temp - begin) // 2, len(B), p):
            B[j] = False
    for i in range(len(B)):
        if B[i]:
            yield 2 * i + begin
