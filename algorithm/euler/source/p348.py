#!/usr/bin/env python
#-*- coding:utf-8 -*-

from itertools import imap
from eulertools import memoized, is_square

def cube(n):
    return n ** 3

def square(n):
    return n * n

def integets_from(n):
    while True:
        yield n
        n += 1

def reverse(n):
    r = 0
    while n > 0:
        r = r * 10 + n % 10
        n = n / 10
    return r

def palindromic_numbers():
    for i in integets_from(0):
        l = range(10 ** i, 10 ** (i + 1))
        for j in l:
            yield j * (10 ** i) + reverse(j / 10)
        for j in l:
            yield j * (10 ** (i + 1)) + reverse(j)

def g(n):
    c = 0
    for a in imap(cube, integets_from(2)):
        if a > n:
            break
        if is_square(n - a):
            c += 1
    return c



def f():
    c, s = 0, 0
    for n in palindromic_numbers():
        if g(n) == 4:
            #print n
            s += n
            c += 1
            if c == 5:
                break
    return s

def main():
    print f()

if __name__ == "__main__":
    main()
