from collections import defaultdict
from Crazy import isprime
from eulertools import primes, big_primes


def g(n):
    if n % 16 == 0:
        m = n // 16
        if m == 1 or isprime(m):
            return True
        else:
            return False
    elif n % 4 == 0:
        m = n // 4
        if m == 1 or isprime(m):
            return True
        else:
            return False
    else:
        return isprime(n)


def f(n):
    Re = defaultdict(int)
    for a in range(1, (n + 1) // 4 + 2):
        if a % 1000 == 0:
            print(a)
        if 4 * a * a < n:
            Re[4 * a * a] += 1
        y = 3 * a
        if 3 * a * a >= n:
            y = 2 * a + int((4 * a * a - n) ** 0.5)
            while (4 * a - y) * y >= n:
                y += 1
        while y < 4 * a:
            m = (4 * a - y) * y
            if 0 < m < n:
                Re[m] += 1
            y += 1
    T = [v for v in Re if Re[v] == 1]
    ##    print(T)
    T = list(filter(g, T))
    ##    print(T)
    return len(T)


def f2():
    N = 5 * 10 ** 7
    l = list(primes(7100))
    step = 500000
    re = 0
    re += len(l) * 2
    re += len([i for i in l if i % 4 == 3])
    begin = 7100
    while begin + step < N:
        print(begin)
        b = list(big_primes(begin, begin + step, l))
        if (begin + step) * 16 < N:
            re += len(b)
        elif begin * 16 < N:
            re += len([i for i in b if i * 16 < N])
        if (begin + step) * 4 < N:
            re += len(b)
        elif begin * 4 < N:
            re += len([i for i in b if i * 4 < N])
        re += len([i for i in b if i % 4 == 3])
        begin += step
    b = list(big_primes(begin, N, l))
    re += len([i for i in b if i % 4 == 3])
    return re


print(f2())
