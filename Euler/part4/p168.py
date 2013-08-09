#!/usr/bin/env python
#-*- coding:utf-8 -*-


def f():
    result = 0
    count = 0
    for a in range(1, 10):
        for b in range(1, 10):
            p = 0
            re = v = a
            for i in range(99):
                l_v = v
                p, v = divmod(v * b + p, 10)
                if v == a and p == 0 and l_v != 0 and re > 10:
                    result += re
                    count += 1
                re += v * 10 ** (i + 1)
    return str(result)[-5:]

print f()
