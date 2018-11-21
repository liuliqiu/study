Cached = {}


def f(m, n):
    if n < m:
        return 0
    if (m, n) not in Cached:
        Cached[m, n] = f(m, n - 1) + f(m, n - m) + 1
    return Cached[(m, n)]


def g(n):
    return f(2, n) + f(3, n) + f(4, n)


print(g(50))
