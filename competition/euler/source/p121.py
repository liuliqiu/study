from functools import reduce
from itertools import combinations


def pr(l):
    if len(l) == 0:
        return 1
    return reduce(lambda x, y: x * y, l)


def f(n):
    x = pr(range(1, n + 2))
    y = sum(pr(f) for i in range((n + 1) // 2) for f in combinations(range(n + 1), i))
    print(x, y)
    return x // y


print(f(15))
