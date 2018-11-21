from collections import Counter

l = [i for i in range(1, 21)]
ls = l + [25]
ld = list(map(lambda x: x * 2, ls))
lt = list(map(lambda x: x * 3, l))
lall = list(sorted(ls + ld + lt))
lCounter = Counter(lall)


def g(n):
    re = 0
    for i in ld:
        if i == n:
            re += 1
        elif i < n:
            for j, a in enumerate(lall):
                if i + a == n:
                    re += 1
                elif i + a < n:
                    for k in range(j, len(lall)):
                        if lall[k] + i + a == n:
                            re += 1
                        if lall[k] + i + a > n:
                            break
    return re


def f():
    return sum(g(i) for i in range(1, 100))


print(f())
