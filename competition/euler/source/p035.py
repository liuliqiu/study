##The number, 197, is called a circular prime because all rotations of the digits:
##197, 971, and 719, are themselves prime.
##There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73
##, 79, and 97.
##How many circular primes are there below one million?
import math


def isprime(n):
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i = i + 2
    return True


def number(n):
    z = [1, 3, 7, 9]
    for i in range(n):
        pass


def mov(n):
    x = math.floor(math.log10(n))
    return n // 10 + (n % 10) * (10 ** x)


def circular(n):
    m = n
    x = math.floor(math.log10(n))
    while isprime(m):
        m = m // 10 + (m % 10) * (10 ** x)
        if m == n:
            return True
    return False


def option(n):
    return all([c not in str(n) for c in ["0", "2", "4", "5", "6", "8"]])


def fi():
    return len([i for i in range(11, 1000000, 2) if option(i) and circular(i)]) + len(
        [2, 3, 5, 7]
    )


print(fi())
