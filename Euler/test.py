#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
    author:         llq<llq17501@gmail.com>
"""
from timeit import Timer
from cProfile import run


from itertools import count
def f():
    d = 312
    for b in range(2, 47):
        for a in range(1, b):
            for c in count(1):
                x = a * a * c + a * c * c * b * b * b
                if x == d * d:
                    return a, b, c
                elif x > d * d:
                    break

def test():
    print f()

if __name__ == "__main__":
    t=Timer("test()","from __main__ import test")
    print(t.timeit(1))
    run('test()')


