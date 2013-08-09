#-*- coding:utf-8 -*-
import time
from itertools import cycle
from collections import Counter
from random import randint

# 数学部分

def GCD(*args):
    """
        最大公约数
    """
    y = args[0]
    index = 1
    while index < len(args):
        x = args[index]
        if x > y:
            x, y = y, x
        while x > 0:
            x, y = y % x, x
        index += 1
    return y



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



def is_prime(n):
    if n%2 == 0:
        return n == 2
    i=3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True




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



def primes(n):
    if n<2:
        raise StopIteration
    else:
        yield 2
        l=[True for i in range((n-1)//2)]
        for i in range(len(l)):
            if l[i]:
                yield 2*i+3
                for j in range(3*i+3,len(l),2*i+3):
                    l[j]=False



def big_primes(begin,end,smallprimes=None):
    '''求begin 到end之间的所有素数，使用smallprimes试除'''
    if smallprimes==None:
        smallprimes=list(primes(int(end**0.5)))
    if 2 in smallprimes:
        smallprimes.remove(2)
    if begin<2:
        begin=3
    if begin==2:
        yield 2
    if begin%2==0:
        begin+=1
    if end%2==0:
        end-=1
    B=[True]*((end-begin+2)//2)
    for p in smallprimes:
        temp=((begin+p-1)//p)*p
        if temp%2==0:
            temp+=p
        if temp==p:
            temp+=2*p
        for j in range((temp-begin)//2,len(B),p):
            B[j]=False
    for i in range(len(B)):
        if B[i]:
            yield 2*i+begin



def exp_mod(a, b, p):
    """(a ** b) % p"""
    if b == 0:
        return 1
    elif b % 2 == 0:
        return ((exp_mod(a, b / 2, p) ** 2) % p)
    else:
        return ((exp_mod(a, b / 2, p) ** 2) * a) % p



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

def _f(status, f, g):
    """
        Fibs = _f((1, 1), sum, lambda status, v:status[1], v)
        sum(
            filter(
                itertools.takewhile(lambda x:x < 1000000,
                    itertools.chain((1, 1),
                        _f((1, 1), sum, lambda status, v:status[1], v)))))
    """
    while True:
        new_val = f(status)
        yield new_val
        status = g(status, new_val)


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
