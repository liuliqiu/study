#!/usr/bin/env python
#-*- coding:utf-8 -*-

import bisect

def main():
    with open("Median.txt") as f:
        i = 0
        r = 0
        L = []
        for line in f:
            n = int(line.strip())
            i += 1
            bisect.insort(L, n)
            r += L[(i - 1)/2]
            r %= 10000
        print r


if __name__ == "__main__":
    main()
