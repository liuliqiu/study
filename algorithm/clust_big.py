#!/usr/bin/env python
# -*- coding:utf-8 -*-

from itertools import combinations, product


def bytes_to_int(s):
    r = 0
    for i in s:
        r = r * 2 + i
    return r


def cl(S, b_l):
    M = [2 ** i for i in range(0, b_l)]
    M2 = {x ^ y for x, y in combinations(M, 2)} | set(M)

    k = 0
    while len(S) > 0:
        k += 1
        A = {S.pop()}
        while len(A) > 0:
            B = {x ^ y for x, y in product(A, M2)}
            A = S & B
            S.difference_update(A)
    return k


def main():
    file_name = "clustering_big.txt"
    # file_name = "cl_b.txt"
    with open(file_name) as f:
        x, b_l = map(int, next(f).strip().split())
        S = {bytes_to_int(map(int, line.strip().split())) for line in f}


if __name__ == "__main__":
    main()
