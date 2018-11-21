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


def f():
    result = 0
    for line in open("txt/sets.txt"):
        t = tuple(int(i) for i in line.strip().split(","))
        if special(t):
            result += sum(t)
    return result
