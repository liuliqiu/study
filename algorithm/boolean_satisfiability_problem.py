#!/usr/bin/env python
#-*- coding:utf-8 -*-
from sys import stdin
from collections import defaultdict


def guess(determine, i, v, sat):
    re = {i:v}
    L = [(i, v)]
    _i = 0
    while _i < len(L):
        i, v = L[_i]
        _i += 1
        for j, u in sat[i, v]:
            if j in re and re[j] != u:
                return False
            elif j not in re:
                L.append((j, u))
                re[j] = u
    return re



def fn(n, lst):
    sat = defaultdict(list)
    for x, y in lst:
        p, q = x < 0, y > 0
        x, y = map(abs, (x, y))
        sat[x, p].append((y, q))
        sat[y, not q].append((x, not p))

    determine = {}
    while len(determine) < n:
        flag = True
        for i in range(1, n + 1):
            if i not in determine:
                guess_true = guess(determine, i, True, sat)
                guess_false = guess(determine, i, False, sat)
                if guess_true and guess_false:
                    continue
                elif not guess_true and not guess_false:
                    return False
                else:
                    determine.update(guess_true or guess_false)
                    flag = False
        if flag:
            return True






def main():
    f = stdin
    n = int(next(f).strip())
    lst = [tuple(map(int, line.strip().split())) for line in f]
    print fn(n, lst)

if __name__ == "__main__":
    main()
