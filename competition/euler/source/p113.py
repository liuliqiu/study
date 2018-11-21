def g(l):
    re = 0
    for i in l:
        re += i
        yield re


def f(n):
    u = [1 for i in range(10)]
    re = 0
    for i in range(n):
        r = sum(u) * 2 - u[0] - u[-1] - 9
        re = re + r
        u = list(g(u))
    return re


print(f(10))
