#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
    author:         llq<llq17501@gmail.com>
"""
from cProfile import run
import importlib
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='run euler or test')
    parser.add_argument('n', type=int, help='euler problem number.')
    parser.add_argument('--test', action='store_true', help='only test')
    args = parser.parse_args()
    m = importlib.import_module('source.p{0:03}'.format(args.n))
    if args.test:
        if hasattr(m, 'test_case'):
            for inp, outp in m.test_case:
                run('assert m.f(inp) == outp')
    else:
        test = lambda :m.f(m.x)
        run('print(test())')


