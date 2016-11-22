#!/usr/bin/env python
#-*- coding:utf-8 -*-

def dijkstra(Graph, start_point):
    D = {start_point:0}
    W = set(Graph[start_point].keys())
    all_points = Graph.keys()
    while len(all_points) > len(D.keys()):
        min_distance, min_w = None, None
        for v, d in D.items():
            for w in W:
                if w in Graph[v]:
                    if min_distance is None or d + Graph[v][w] < min_distance:
                        min_distance, min_w = d + Graph[v][w], w
        D[min_w] = min_distance
        W.remove(min_w)
        W.update(set(Graph[min_w]) - set(D.keys()))

    return D

def main():
    with open("dijkstraData.txt") as data:
        Graph = {}
        for line in data:
            lst = line.split()
            v = int(lst.pop(0))
            Graph[v] = {}
            for w, l in [map(int, item.split(",")) for item in lst]:
                Graph[v][w] = l
        D = dijkstra(Graph, 1)
        print ",".join(str(D[w]) for w in [7,37,59,82,99,115,133,165,188,197])

if __name__ == "__main__":
    main()
