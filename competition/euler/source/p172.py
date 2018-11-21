#!/usr/bin/env python
# -*- coding:utf-8 -*-


def f(n):
    """
        >>> f(4)
        8991
        >>> f(5)
        89586
        >>> f(6)
        888570
        >>> f(13)
        6078934461600
        >>> f(14)
        53286368335200
        >>> f(18)
        227485267000992000
    """
    d = {0: 9, 1: 1, 2: 0, 3: 0}
    return 9 * g(n - 1, d)


def g(n, s):
    if n == 1:
        return count_choice(s)
    else:
        return sum(mult * g(n - 1, new_s) for mult, new_s in get_choice(s))


def get_choice(s):
    for k, v in s.iteritems():
        if k < 3 and v > 0:
            _t = s.copy()
            _t[k + 1] += 1
            _t[k] -= 1
            yield v, _t


def count_choice(s):
    return sum(v for k, v in s.iteritems() if k < 3)
