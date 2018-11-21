from functools import reduce
from Crazy import primes

ps = primes(1000)


def products(l):
    return reduce(lambda x, y: x * y, l)


def sod(divs):
    return products([(i ** (divs[i] + 1) - 1) // (i - 1) for i in divs])


def g(n):
    divs = {}
    m = n
    for i in ps:
        if i * i > n:
            break
        while n % i == 0:
            n = n // i
            if i in divs:
                divs[i] += 1
            else:
                divs[i] = 1
    if n not in divs and n != 1:
        divs[n] = 1
    return sod(divs) - m


def f1(n):
    t = 1
    for i in range(2, n + 1):
        if i % 10000 == 0:
            print(i)
        m = g(i)
        j = 1
        L = []
        while m > i and m not in L and m <= n:
            L.append(m)
            m = g(m)
            j += 1
        if m == i and j > t:
            t = j
            print(j, i, m)


f1(1000000)
