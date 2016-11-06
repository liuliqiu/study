#-*- coding:utf-8 -*-
"""Minimum spanning trees
    Algorithms: Chapter 5.1
"""

def mst(node_count, lst):
    """
    >>> mst(3, [(1, 2, 3), (2, 3, 2)])
    5

    >>> mst(6, [(1, 3, 1), (1, 2, 4), (2, 3, 4), (1, 4, 3),
                (3, 4, 2), (2, 4, 4), (4, 6, 6), (3, 6, 4), (5, 6, 5)])
    16

    """
    sorted_lst = iter(sorted(lst, key=lambda x: x[2]))
    tree_nodes = {1}
    result = 0
    while len(tree_nodes) < node_count:
        for node1, node2, weight in sorted_lst:
            if (node1 in tree_nodes and node2 not in tree_nodes) or \
                    (node1 not in tree_nodes and node2 in tree_nodes):
                result += weight
                node = node2 if node1 in tree_nodes else node1
                tree_nodes.add(node)
                break
    return result
