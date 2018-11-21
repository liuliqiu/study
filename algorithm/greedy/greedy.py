# -*- coding:utf-8 -*-


def greedy(lst, F):
    L = sorted([(F(w, l), l, w) for w, l in lst], reverse=True)
    result = 0
    c = 0
    for _, l, w in L:
        c += l
        result += c * w
    return result
