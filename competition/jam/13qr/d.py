#!/usr/bin/env python
# -*- coding:utf-8 -*-


def could_apply():
    pass


def app():
    pass


def f(init_keys, chestes):
    change, plus = [], []
    keys = init_keys
    while len(change) > 0:
        for chest in could_apply(plus):
            keys = app(chest, keys)


f([1], [(1, [2]), (1, []), (1, [1, 2]), (2, [1]), (2, [])])
