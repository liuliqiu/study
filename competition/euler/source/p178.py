def tran(l, v):
    if v == 0:
        return (0, l[0] + l[1], 0, l[2] + l[3])
    elif v == 9:
        return (0, 0, l[0] + l[2], l[1] + l[3])
    else:
        return l


def f(n):
    S = [(0, 1, 0, 0)] + [(1, 0, 0, 0) for i in range(8)] + [(0, 0, 1, 0)]
    R = {}
    for i in range(10):
        if i == 0:
            R[i] = [1]
        elif i == 9:
            R[i] = [8]
        else:
            R[i] = [i - 1, i + 1]
    re = 0
    for i in range(n - 1):
        ##        print(S)
        T = [(0, 0, 0, 0) for i in range(10)]
        for j in range(10):
            for v in R[j]:
                T[j] = tuple(i + j for i, j in zip(T[j], tran(S[v], j)))
        re += sum(i[3] for i in T[1:])
        S = T
    ##    print(S)
    return re


print(f(40))
