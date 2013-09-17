#!/usr/bin/env python
#-*- coding:utf-8 -*-
from __future__ import division




def greedy(lst, F):
    L = sorted([(F(w, l), l, w) for w,l in lst], reverse = True)
    result = 0
    c = 0
    for _, l, w in L:
        c += l
        result += c * w
    return result

def mst(node_count, lst):
    D = {}
    for i in range(1, node_count + 1):
        D[i] = []
    for n1, n2, c in lst:
        D[n1].append((c, n2))
        D[n2].append((c, n1))
    S = {1}
    result = 0
    while len(S) < 500:
        C, N = None, None
        for n1, n2, c in lst:
            if (n1 in S and n2 not in S) or (n1 not in S and n2 in S):
                if C is None or c < C:
                    C = c
                    if n1 in S:
                        N = n2
                    else:
                        N = n1
        S.add(N)
        result += C
    return result




def main():
    with open("jobs.txt") as f:
        next(f)
        lst = [map(int, line.strip().split(" ")) for line in f]
        #lst = [(2, 1), (5, 3)]
        print greedy(lst, lambda w,l:w/l)
        print greedy(lst, lambda w,l:w-l)

    with open("edges.txt") as f:
        node_count, edges_count = map(int, next(f).strip().split(" "))
        lst = [map(int, line.strip().split(" ")) for line in f]
        print mst(node_count, lst)


if __name__ == "__main__":
    main()
