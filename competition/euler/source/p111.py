from Crazy import isprime
from itertools import *


def factors(n):
    if n < 2:
        raise StopIteration
    factor = 2
    while factor ** 2 <= n:
        while n % factor == 0:
            n = n // factor
            yield factor
        factor += 1 if factor == 2 else 2
    if n != 1:
        yield n


def S(n, d, a):
    islongN = lambda x: 10 ** (n - 1) <= x < 10 ** (n)
    alld = sum(10 ** i for i in range(n)) * d
    for i in product(range(10), repeat=a):
        for j in combinations(range(n), a):
            t = alld
            for k in range(a):
                t = t - (d - i[k]) * 10 ** j[k]
            if islongN(t) and isprime(t):
                yield t


def f(n):
    result = 0
    for i in range(10):
        j, l = 1, 0
        while l == 0:
            ls = list(S(n, i, j))
            l = len(ls)
            j += 1
        result += sum(ls)
    return result


print(f(10))
