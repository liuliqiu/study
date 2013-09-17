#!/usr/bin/env python
#-*- coding:utf-8 -*-


def find_sum2(S, t):
    for v in S:
        if t - v in S:
            return True


def main():
    with open("algo1-programming_prob-2sum.txt", "r") as f:
        S = {int(line.strip()) for line in f}
        r = 0
        for t in range(-10000, 10000 + 1):
            if find_sum2(S, t):
                print t
                r += 1
        print r


if __name__ == "__main__":
    main()
