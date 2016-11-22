#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
    all-pairs shortest-path problem
"""

ints = lambda x:map(int, x.strip().split())
INF = float("inf")

class Graph(object):
    def __init__(self, n, m, lst):
        self.edges = lst
        self.vectors = range(1, n + 1)
        self.edges_number = m
        self.vectors_number = n

        self._edges = {}
        for i, j, l in lst:
            self._edges[(i, j)] = l

    def vector(self, i, j):
        if i == j:
            return 0
        elif (i, j) in self._edges:
            return self._edges[i, j]
        else:
            return INF


def FloydWarshallAlgorithm(G):
    A = {}
    for i in G.vectors:
        for j in G.vectors:
            A[(i, j)] = G.vector(i, j)

    for k in G.vectors:
        print k
        B = {}
        for i in G.vectors:
            for j in G.vectors:
                B[i, j] = min(A[i, j], A[i, k] + A[k, j])
        A = B
        for i in G.vectors:
            if A[i, i] < 0:
                return "negative-cost cycle"
    return min(A.values())


def BellmanFordAlgorithm(G):
    pass


def JohnsonAlgorithm(G):
    # add point

    # Bellman-ford ALgorithm
    
    # edges parse
    
    for v in G.vectors:
        # dijkstra
        pass

    # result parse
    pass


def main():
    file_name = "g3.txt"
    with open(file_name) as f:
        n,m = ints(next(f))
        lst = [ints(line) for line in f]
        G = Graph(n, m, lst)
        print FloydWarshallAlgorithm(G)


if __name__ == "__main__":
    main()
