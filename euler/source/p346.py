#!/usr/bin/env python
#-*- coding:utf-8 -*-

def ints_start_from(n):
    while True:
        yield n
        n += 1

def make_num(k, j):
    r = 1
    for _ in range(j):
        r = r * k + 1
    return r


def f(n):
    s = set([1])
    for j in ints_start_from(2):
        if make_num(2, j) >= n:
            break
        for k in ints_start_from(2):
            r = make_num(k, j)
            if r >= n:
                break
            if r not in s:
                s.add(r)
    return s

def main():
    print sum(f(10 ** 12)) # 15864

if __name__ == "__main__":
    main()
