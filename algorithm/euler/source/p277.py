#!/usr/bin/env python
#-*- coding:utf-8 -*-

def f_D(status):
    """ (3, 0) -> (1, 0) """
    a, b, c, d = status
    if c % 3 == 0 and d % 3 == 0:
        return a, b, c / 3, d / 3
    else:
        return 3 * a, 3 * b, c, d


def f_d(status):
    """ (3, 2) -> (2, 1) """
    a, b, c, d = status
    if c % 3 == 0 and d % 3 == 2:
        return a, b, 2 * (c / 3), 2 *(d / 3) + 1
    else:
        assert ((2 * d + 2) * a) % c == 0
        return 3 * a, ((2 * d + 2) * a) / c + b, 2 * c, 2 * d + 1

def f_U(status):
    """ (3, 1) -> (4, 2) """
    a, b, c, d = status
    if c % 3 == 0 and d % 3 == 1:
        return a, b, 4 * (c / 3), 4 *(d / 3) + 2
    else:
        print d * 2 + 1, a, c
        assert ((2 * d + 1) * a) % c == 0
        return 3 * a, ((2 * d + 1) * a) / c + b, 4 * c, 4 * d + 2

def f(seq, n):
    status = (1, 0, 1, 0)
    f_map = {"D" : f_D, "d" : f_d, "U" : f_U}
    for s in reversed(seq):
        status = f_map[s](status)
        print status

def main():
    #f("DdDddUUdDD", 10 ** 6) # 1004064
    #f("DdDddUUdDD", 1) # 231
    #f("DdDddUUdDD", 1)
    #f("DUdD", 1)
    #f("UD", 1)
    f("Dd", 1)
    f("dD", 1)

if __name__ == "__main__":
    main()
