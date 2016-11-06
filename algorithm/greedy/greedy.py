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
    """Minimun spanning trees

    >>> mst(3, [(1, 2, 3), (2, 3, 2)])
    5

    >>> mst(6, [(1, 3, 1), (1, 2, 4), (2, 3, 4), (1, 4, 3), (3, 4, 2), (2, 4, 4), (4, 6, 6), (3, 6, 4), (5, 6, 5)])
    16

    """
    sorted_lst = list(sorted(lst, key=lambda x:x[2]))
    tree_nodes = {1}
    result = 0
    while len(tree_nodes) < node_count:
        for n1, n2, c in sorted_lst:
            if (n1 in tree_nodes and n2 not in tree_nodes) or (n1 not in tree_nodes and n2 in tree_nodes):
                result += c
                N = n2 if n1 in tree_nodes else n1
                tree_nodes.add(N)
                break
    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()
