#!/usr/bin/env python
#-*- coding:utf-8 -*-

from random import random, randint

def estimation(D):
    return sum(D)/float(len(D))

def bayes_estimation(D):
    mu = sum(D)/float(len(D))
    L = 1
    for x in D:
        L *= (mu ** x) * ((1- mu) ** (1-x))
    a, b = 0
    m, l = sum(D), len(D) - sum(D)
    return mu

def test(est_func, times = 1000):
    R = []
    for _ in range(times):
        N = randint(30, 50)
        P = random()
        D = [1 if random()<P else 0 for _ in range(N)]
        p = est_func(D)
        R.append(abs(p - P))
    return sum(R)/len(R)

def average(it):
    i, s = 0, 0
    for d in it:
        i += 1
        s += d
    return float(s) / float(i)


def main():
    #print test(estimation)
    print test(bayes_estimation, 1)

if __name__ == "__main__":
    main()
