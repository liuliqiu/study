#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
from operator import mul
from itertools import product
from collections import Counter
from math import factorial

def get_input(f):
    T = int(next(f))
    for _ in range(T):
        R, N, M, K = map(int, next(f).strip().split(' '))
        yield N, M, K
        for i in range(R):
            ints = map(int, next(f).strip().split(' '))
            yield ints

class Model(object):
    def __init__(self, N, M, K):
        self.all_item = []
        self.values = {}
        count = {}
        F = map(factorial, range(N + 1))
        item = tuple(2 for _ in range(N))
        end = tuple(M for _ in range(N))
        while True:
            count[item] = F[N]
            for v, c in Counter(item).items():
                count[item] /= F[c]
            if item == end:
                break
            for i, v in reversed(list(enumerate(item))):
                if v < M:
                    item = tuple(item[j] if j < i else v + 1 for j in range(len(item)))
                    break

        for item, c in count.items():
            self.all_item.append(item)
            for flags in product(*[range(2) for _ in range(N)]):
                p = reduce(mul, [v ** f for v, f in zip(item, flags)])
                self.values[(item,p)] = c * p



    def best(self, products):
        _v, _i = 0, None
        for item in self.all_item:
            v = reduce(mul, (self.values.get((item, p), 0) for p in products))
            if v > _v:
                _v, _i = v, item
        return _i


def main():
    i = get_input(sys.stdin)
    N, M, K = next(i)
    m = Model(N, M, K)
    print "Case #1:"
    for j, ints in enumerate(i):
        #print m.best(ints), ints
        print ''.join(map(str, m.best(ints)))

if __name__ == "__main__":
    main()
