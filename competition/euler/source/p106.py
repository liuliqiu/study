from itertools import combinations

Cached = {}


def Fraction(n):
    if n <= 1:
        return 1
    elif n in Cached:
        return Cached[n]
    else:
        Cached[n] = n * Fraction(n - 1)
        return Cached[n]


def C(n, k):
    return Fraction(n) // (Fraction(k) * Fraction(n - k))


def L(n):
    m = n // 2
    S = set(range(2, n + 1))
    result = 0
    for l in combinations(S, m - 1):
        a = [1] + list(sorted(l))
        b = list(S.difference(a))
        if any(a[i] > b[i] for i in range(1, m)):
            ##            print(a,b)
            result += 1
    return result


def f1(n):
    return sum(L(i) * C(n, i) for i in range(4, n + 1, 2))
