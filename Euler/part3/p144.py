#!/usr/bin/env python
#-*- coding:utf-8 -*-
import math

def f():
    """
    >>> f()
    354
    """
    point0 = (0, 10.1)
    point = (1.4, -9.6)
    line = ((point[1] - point0[1])/point[0],10.1)
    index = 0
    while not can_out(point):
        index += 1
        line = refract_line(line, point)
        point = cross_point(line, point)
    return index

def refract_line(line, point):
    x, y = point
    m = (-4 * x) / y
    new_m = math.tan(2 * math.atan(m) - math.atan(line[0]))
    return (new_m, y - new_m * x)

def cross_point(line, point):
    b = 2 * line[0] * line[1]
    a = 4 + line[0] * line[0]
    c = line[1] * line[1] - 100
    tmp = (b * b - 4 * a * c) ** 0.5
    x1, x2 = (-b + tmp) / (2 * a), (-b - tmp) / (2 * a)
    x, y = point
    if abs(x2 - x) < abs(x1 - x):
        x1, x2 = x2, x1
    assert abs(x1 - x) < 0.0001
    return x2, line[0] * x2 + line[1]

def can_out(point):
    return -0.01 <= point[0] <= 0.01 and point[1] > 0

