#!/usr/bin/env python
#-*- coding:utf-8 -*-

from eulertools import comb

def _g(k, n, m, p):
    if k * n < p:
        return 0
    return comb(n, k) * _h(k, m, p)


def _h(k, m, p):
    """
        从k个颜色的球，每种球m 个中，取p个，必须每种颜色都有至少一个,取法的数目
    """
    if p < k or p > k * m:
        return 0
    elif k == 1:
        return comb(m, p)
    else:
        return sum(comb(m, j) * _h(k - 1, m, p - j) for j in range(1, m + 1))


def _f(n, m, p):
    L = [_g(k, n, m, p) for k in range(1, n + 1)]
    return sum(L[k - 1] * k for k in range(1, n + 1)) / float(comb(n * m, p))

def main():
    print _f(7, 10, 20) # 6.81874180202

if __name__ == "__main__":
    main()
