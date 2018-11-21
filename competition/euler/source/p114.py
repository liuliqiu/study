Cached = {}


def f(n):
    if n < 3:
        return 1
    if n in Cached:
        return Cached[n]
    Cached[n] = f(n - 1) + sum(f(i - 1) for i in range(n - 2))
    return Cached[n]


print(f(50))


def g(m, n):
    if n < m:
        return 1
    if (m, n) in Cached:
        return Cached[(m, n)]
    Cached[(m, n)] = g(m, n - 1) + sum(g(m, i - 1) for i in range(n + 1 - m))
    return Cached[(m, n)]


def h(m):
    i = 1
    while g(m, i) < 1000000:
        i = i + 1
    return i
