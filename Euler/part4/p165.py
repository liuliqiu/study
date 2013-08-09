#!/usr/bin/env python
#-*- coding:utf-8 -*-

from fractions import Fraction
from itertools import combinations

def f(n):
    """
        >>> f(5000)
        2868868
        >>> f(1000)
        113849
        >>> f(500)
        29496
    """
    t = gen()
    lines = [(next(t), next(t), next(t), next(t)) for i in range(n)]
    return len({inter_sective(seg, seg2) for seg, seg2 in combinations(lines, 2)}) - 1

def inter_sective(seg, seg2):
    """
        >>> inter_sective((27, 44, 12, 32), (46, 53, 17, 62)) is not None
        False
        >>> inter_sective((27, 44, 12, 32), (46, 70, 22, 40)) is not None
        False
        >>> inter_sective((46, 53, 17, 62), (46, 70, 22, 40)) is not None
        True
        >>> inter_sective((0, 1, 2, 1), (2, 2, 0, 0)) is not None
        True
        >>> inter_sective((0, 1, 2, 1), (3, 2, 1, 0)) is not None
        False
        >>> inter_sective((0, 3, 0, 5), (1, 3, -1, 5)) is not None
        True
        >>> inter_sective((0, 3, 0, 5), (1, 5, -1, 4)) is not None
        True
    """
    A = (seg2[0] - seg[0]) * (seg[3] - seg[1]) * (seg2[3] - seg2[1])
    B = (seg[2] - seg[0]) * (seg2[3] - seg2[1])
    C = (seg[3] - seg[1]) * (seg2[2] - seg2[0])
    if B != C:
        tmp = (A + B * seg[1] - C * seg2[1])
        tmp2 = B - C
        y = Fraction(tmp, tmp2)
        if seg[1] != seg[3]:
            in_seg = (seg[1] * tmp2 - tmp) * (seg[3] * tmp2 - tmp) < 0
            p = seg[0] + Fraction((y - seg[1]) * (seg[2] - seg[0]), seg[3] - seg[1]), y
        else:
            x = seg2[0]  * (seg2[3] - seg2[1]) + (seg[1] - seg2[1]) * (seg2[2] - seg2[0])
            in_seg = (x - seg[0] * (seg2[3] - seg2[1])) * (x - seg[2] * (seg2[3] - seg2[1])) < 0
            p = Fraction(x, seg2[3] - seg2[1]), seg[1]

        if seg2[1] != seg2[3]:
            in_seg2 = (seg2[1] * tmp2 - tmp) * (seg2[3] * tmp2 - tmp) < 0
        else:
            x = seg[0]  * (seg[3] - seg[1]) + (seg2[1] - seg[1]) * (seg[2] - seg[0])
            in_seg2 = (x - seg2[0] * (seg[3] - seg[1])) * (x - seg2[2] * (seg[3] - seg[1])) < 0
            p = Fraction(x, seg[3] - seg[1]), seg2[1]

        if in_seg and in_seg2:
            return p

def gen():
    s = 290797

    while True:
        s = (s * s) % 50515093
        yield s % 500
