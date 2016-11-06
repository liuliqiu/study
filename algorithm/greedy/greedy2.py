#!/usr/bin/env python
#-*- coding:utf-8 -*-

from itertools import combinations, product

def clustering(L, N):
    L.sort()
    D = {i:i for i in range(1, N + 1)}
    C = {i:1 for i in range(1, N + 1)}
    def find(i):
        while D[i] != i:
            i = D[i]
        return i
    K = N
    X = {}
    for c, n1, n2 in L:
        X[(n1, n2)] = c
    for c, n1, n2 in L:
        e1, e2 = map(find, (n1, n2))
        if e1 != e2:
            if C[e1] < C[e2]:
                e1, e2 = e2, e1
            D[e2] = e1
            C[e1] += C[e2]
            K -= 1
        if K == 4:
            break
    M = {}
    for i in range(1, N +1):
        c = find(i)
        M.setdefault(c, [])
        M[c].append(i)
    M = M.values()

    for k1, k2 in combinations(range(4), 2):
        print min(X[tuple(sorted((x, y)))] for x, y in product(M[k1], M[k2]))



def main():
    with open("clustering1.txt") as f:
    #with open("cl_test2.txt") as f:
        N = int(next(f).strip())
        L = []
        for line in f:
            n1, n2, c = map(int, line.strip().split())
            L.append((c, n1, n2))
        clustering(L, N)

if __name__ == "__main__":
    main()
