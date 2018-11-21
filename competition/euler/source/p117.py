Cached = {}


def f(n):
    if n < 2:
        return 1
    if n not in Cached:
        Cached[n] = f(n - 1) + f(n - 2)
        if n >= 3:
            Cached[n] += f(n - 3)
        if n >= 4:
            Cached[n] += f(n - 4)
    return Cached[n]
