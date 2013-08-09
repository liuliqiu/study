#!/usr/bin/env python
#-*- coding:utf-8 -*-

from itertools import imap, count, takewhile

square = lambda x:x*x

def f():
    T = 20
    L = map(square, range(1, 10))
    for i in takewhile(lambda x:x< 81 * T, imap(square, count(1))):
        print i
