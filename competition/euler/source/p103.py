from itertools import combinations


def g(n):
    m = n // 2
    S = set(range(1, n))
    for l in combinations(S, m - 1):
        a = [0] + list(sorted(l))
        b = list(S.difference(a))
        if any(a[i] > b[i] for i in range(1, m)):
            yield tuple(a), tuple(b)


Cached = {}


def G(l):
    if l not in Cached:
        Cached[l] = list(g(l))
    return Cached[l]


def H(x, y):
    a, b = y
    na = tuple(x[i] for i in a)
    nb = tuple(x[i] for i in b)
    return na, nb


def gen(l):
    if l < 4:
        yield ((), ())
    else:
        U = range(l)
        for i in range(4, l + 1, 2):
            for x in combinations(U, i):
                for y in G(i):
                    yield H(x, y)


def special(a):
    if len(a) == 1:
        return True
    a = list(sorted(a))
    if all(sum(a[: i + 1]) > sum(a[-i:]) for i in range(1, (len(a) + 1) // 2)):
        for s, t in gen(len(a)):
            if s and t:
                if sum(a[i] for i in s) == sum(a[i] for i in t):
                    return False
        return True
    return False


def searchSmallA(ma):
    M = ma
    for a1 in range(17, 38):
        for a2 in range(a1 + 1, 41):
            for a3 in range(a2 + 1, 41):
                print(a1, a2, a3)
                for a4 in range(a3 + 1, 41):
                    for a5 in range(a4 + 1, 42):
                        for a6 in range(a5 + 1, 55):
                            for a7 in range(
                                a6 + 1, M - a1 - a2 - a3 - a4 - a5 - a6 + 1
                            ):
                                a = (a1, a2, a3, a4, a5, a6, a7)
                                if special(a) and sum(a) < M:
                                    print(a)
                                    M = sum(a)


def f():
    a = (11, 18, 19, 20, 22, 25)
    v = a[len(a) // 2]
    a = (v,) + tuple(v + i for i in a)
    searchSmallA(sum(a))
    print(a, sum(a), special(a))


f()
