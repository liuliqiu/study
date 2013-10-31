#!/usr/bin/env python
#-*- coding:utf-8 -*-

floats = lambda line:map(float, line.strip().split())

INF = float("inf")

def get_dist(data, n):
    dist = {}
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            a, b = data[i - 1], data[j - 1]
            dist[i, j] = ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5
    return dist


def bit_iter(n):
    c = 1
    while n > 0:
        if n & 1:
            yield c
        n >>= 1
        c += 1


def dp(data):
    n = len(data)
    dist = get_dist(data, n)
    C = {}
    C[0, 1] = 0
    lay = {0}
    els = {2 ** i for i in range(n - 1)}

    for s in range(2, n + 1):
        print s
        lay = {v ^ el for v in lay for el in els if v & el == 0}
        for S in lay:
            C[S, 1] = INF
            l = list(bit_iter(S))
            for j in l:
                S_j = S ^ (2 ** (j - 1))
                C[S, j] = C[S_j, 1] + dist[1, j + 1]
                for i in l:
                    if i != j:
                        tmp = C[S_j, i] + dist[i + 1, j + 1]
                        if tmp < C[S, j]:
                            C[S, j] = tmp
    #print sorted(C.items())

    return min((C[2**(n -1) - 1, j - 1] + dist[j, 1] for j in range(2, n + 1)))



def get_input(f):
    n = int(next(f).strip())
    lst = map(floats, f)
    print dp(lst)

from random import randint
import cProfile

def test():
    n = 17
    lst = []
    for i in range(n):
        lst.append((randint(1, 100), randint(1, 100)))
    print dp(lst)

def test2():
    print dp([(1, 2), (2, 3), (3, 2)])
    print dp([(1, 2), (2, 3), (3, 4), (3, 2)])
    print dp([(2, 3), (3, 4), (3, 2), (4, 5)])

def profile():
    cProfile.run("test()")


def main():
    #profile()
    #test()
    with open("tsp.txt") as f:
        get_input(f)

if __name__ == "__main__":
    main()
