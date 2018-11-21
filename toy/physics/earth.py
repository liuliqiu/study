#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __future__ import division


from visual import *
from time import sleep
from collections import defaultdict
from itertools import combinations


G = 6.67e-11  # N * (m ** 2) * (kg ** -2)


def gravitation(m_1, m_2, r):
    return G * m_1 * m_2 / (r * r)


def distance(v_1, v_2):
    return 0


class Vector(object):
    """
        >>> a = Vector(1, 2, 3)
        >>> b = Vector(4, 5, 6)
        >>> a * 2.
        Vector(2., 4., 6.)
        >>> 2 * a
        Vector(2, 4, 6)
        >>> a * b
        32
        >>> b * 2 * a
        64
        >>> a + b
        Vector(5, 7, 9)
        >>> a -b
        Vector(-3, -3, -3)
        >>> abs(a), abs(b)
        3.74165738677 8.77496438739
    """

    def __init__(self, *x):
        self.x = x
        self.dimension = len(x)

    def scale(self, c):
        return Vector(*map(lambda x: x * c, self.x))

    def magnitude(self):
        return sum(a ** 2 for a in self.x) ** 0.5

    def __str__(self):
        return "Vector({0})".format(", ".join(map(str, self.x)))

    __repr__ = __str__

    def __mul__(self, x):
        if isinstance(x, (int, float)):
            return self.scale(x)
        elif isinstance(x, Vector):
            assert self.dimension == x.dimension
            return sum(a * b for a, b in zip(self.x, x.x))
        else:
            raise Exception("Could not mul vector by {0}".format(type(x)))

    __rmul__ = __mul__

    def __add__(self, x):
        assert isinstance(x, Vector), self.dimension == x.dimension
        return Vector(*[a + b for a, b in zip(self.x, x.x)])

    def __sub__(self, x):
        assert isinstance(x, Vector), self.dimension == x.dimension
        return self + -x

    def __neg__(self):
        return -1 * self

    __abs__ = magnitude


def f(O, t):
    D = defaultdict(list)
    for (i_1, (pos_1, m_1, v_1)), (i_2, (pos_2, m_2, v_2)) in combinations(
        enumerate(O), 2
    ):
        V = pos_2 - pos_1
        F = gravitation(m_1, m_2, abs(pos_2 - pos_1))
        a_1, a_2 = F / m_1, F / m_2

        D[i_1].append(a_1 * t * V)
        D[i_2].append(a_2 * t * -V)

    new_O = []

    for i, (pos, m, v) in enumerate(O):
        pos += v * t
        for dv in D[i]:
            v += dv
        new_O.append((pos, m, v))
    return new_O


def main():
    O = [
        (Vector(0, 0, 0), 5e9, Vector(0.2, 0, 0), 1, color.blue),
        (Vector(0, 10, 0), 5e9, Vector(-0.2, 0, 0), 1, color.red),
    ]
    Obj = []
    for pos, m, v, r, c in O:
        ball = sphere(pos=pos.x, radius=r, color=c)
        ball.trail = curve(color=c)
        Obj.append(ball)

    X = [x[:3] for x in O]
    t = 0.01
    while True:
        X = f(X, t)
        for i, (pos, _, _) in enumerate(X):
            Obj[i].pos = pos.x
            Obj[i].trail.append(pos=pos.x)
        sleep(t)


if __name__ == "__main__":
    main()
