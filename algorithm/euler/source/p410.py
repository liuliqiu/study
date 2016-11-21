#!/usr/bin/env python
#-*- coding:utf-8 -*-


def satisfies(r, a, b, c):
    y_2 = 4 * a * a + (b - c) ** 2
    return r * r * 4 * y_2 == (a * a + b * b) * 4 * y_2 - (b * b - c * c + y_2) ** 2
