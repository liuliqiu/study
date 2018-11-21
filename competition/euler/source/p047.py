##The first two consecutive numbers to have two distinct prime factors are:
##14 = 2*7
##15 = 3*5
##The first three consecutive numbers to have three distinct prime factors are:
##644 = 2²*7*23
##645 = 3*5*43
##646 = 2*17*19.
##Find the first four consecutive integers to have four distinct primes factors.
##What is the first of these numbers?
from Crazy import primes


def factornum(x, ps):
    if x in ps:
        return 1
    re = 0
    for i in ps:
        if i * i > x:
            re = re + 1
            break
        if x % i == 0:
            re = re + 1
        while x % i == 0:
            x = x // i
    return re


def isresult(x, ps):
    mi = 2 * x
    ma = 2 * x
    while factornum(mi - 1, ps) == 4:
        mi = mi - 1
    if 2 * x - mi >= 3:
        return mi
    while factornum(ma + 1, ps) == 4 and ma - mi < 4:
        ma = ma + 1
    if ma - mi >= 3:
        return mi
    else:
        return False


def fi(n):
    v = primes(int(n ** 0.5) + 1)
    for i in range(3, n + 1, 2):
        if factornum(i, v) == 3:
            x = isresult(i, v)
            if x:
                return x


print(fi(100000))
