#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys

ints = lambda s:map(int, s.strip().split())

def fun(lst, knapsack_size, number_of_items):
    L = [0 for _ in range(knapsack_size + 1)]
    for j, (v, w) in enumerate(lst):
        print j
        for i in range(knapsack_size, w - 1, -1):
            L[i] = max(L[i], v + L[i - w])
    return L[-1]



def main():
    f = sys.stdin
    knapsack_size, number_of_items = ints(next(f))
    vw_list = [ints(line) for line in f]
    print fun(vw_list, knapsack_size, number_of_items)



if __name__ == "__main__":
    main()
