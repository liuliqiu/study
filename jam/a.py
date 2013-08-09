#!/usr/bin/env python
#-*- coding:utf-8 -*-

def g(DI, D):
    pass


def f():
    with open("a.txt") as f:
        T = int(next(f))
        for i in range(T):
            N = int(next(f))
            DI = [map(int, (next(f)).split()) for _ in range(N)]
            D = int(next(f))
            print i + 1, g(DI, D)


f()
