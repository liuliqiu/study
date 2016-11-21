#-*- coding:utf-8 -*-
import numpy
import math
import time
from itertools import cycle
from collections import Counter


# 数学部分
def GCD(y, *args):
    """
        最大公约数
    """
    for x in args:
        if x > y:
            x, y = y, x
        while x > 0:
            x, y = y % x, x
    return y

def comb(n, k):
    if k > n or k < 0:
        return 0
    k = min(k, n - k)
    r = 1
    for i in range(1, k + 1):
        r = (r * (n - i + 1)) / i
    return r

def extended_eucliean(x, y):
    l = []
    while x > 0:
        l.append(y / x)
        x, y = y % x, x
    a, b, gcd = 0, 1, y
    for d in l[::-1]:
        a, b = b - a * d, a
    return a, b, gcd


def inverse_mod(n, p):
    n = n % p
    a, b, _ = extended_eucliean(n, p)
    return a % p
    #n = n % p
    #if n == 1 or n == p - 1:
    #    return n
    #return ((inverse_mod(p % n, p) * (p - p / n))) % p


def factorize(n):
    """
        分解因数
    """
    k = 2
    while k * k <= n:
        while n % k == 0:
            n /= k
            yield k
        k += 1 if k == 2 else 2
    if n > 1:
        yield n


def factorize_to(n):
    """
        将从 1 到 n 的整数分解因数
    """
    l = [{} for _ in range(n)]
    for i in xrange(2, n + 1):
        d = l[i - 1]
        if len(d) == 0:
            d[i] = 1
            for k in range(1, int(math.log(n, i) + 1)):
                t = i ** k
                for j in range(1, n / t + 1):
                    l[j * t - 1][i] = k
    return l



def LCM(*args):
    """
        最小公倍数
    """
    dct = {}
    result = 1
    for x in args:
        for k, v in Counter(factorize(x)).iteritems():
            if k not in dct or dct[k] < v:
                result *= k ** (v - dct.get(k, 0))
                dct[k] = v
    return result




def exp_mod(a, b, p):
    """(a ** b) % p"""
    if b == 0:
        return 1
    else:
        r = a = a % p
        l = int(math.log(b, 2))
        for i in range(l - 1, -1, -1):
            r = (r * r) % p
            if b >> i & 1 != 0:
                r = (r * a) % p
        return r

def convergent_continued_fraction(x):
    a, l = x
    a, b = a, 1
    old_a, old_b = 1, 0
    for n in cycle(l):
        yield a, b
        a, b, old_a, old_b = a * n + old_a, b * n + old_b, a, b


def is_square(n):
    """
    >>> is_square(144)
    True
    >>> is_square(12)
    False
    >>> is_square(2 ** 64)
    True
    >>> is_square(2 ** 64 - 1)
    False
    """
    return (int(n ** 0.5) ** 2) == n


#工具部分
def func_for(status, update):
    """
        fibs = imap(lambda (x, y):y, func_for((1, 1), lambda (x, y):(y, x + y)))
    """
    while True:
        yield status
        status = update(status)


def timer(func):
    def wraper(*args, **kwargs):
        t = time.time()
        result = func(*args, **kwargs)
        print time.time() - t
        return result
    return wraper


def skip(iter_item, n):
    for i in range(n):
        next(iter_item)
    for item in iter_item:
        yield item

def limit(iter_item, n):
    for i in xrange(n):
        yield next(iter_item)


class memoized(object):
   """Decorator that caches a function's return value each time it is called.
   If called later with the same arguments, the cached value is returned, and
   not re-evaluated.
   """
   def __init__(self, func):
      self.func = func
      self.cache = {}
   def __call__(self, *args):
      try:
         return self.cache[args]
      except KeyError:
         value = self.func(*args)
         self.cache[args] = value
         return value
      except TypeError:
         # uncachable -- for instance, passing a list as an argument.
         # Better to not cache than to blow up entirely.
         return self.func(*args)
   def __repr__(self):
      """Return the function's docstring."""
      return self.func.__doc__
   def __get__(self, obj, objtype):
      """Support instance methods."""


def main():
    print GCD(24, 18, 27)
    print LCM(24, 18, 27)
    print map(is_prime, range(1, 10))

if __name__ == "__main__":
    main()
