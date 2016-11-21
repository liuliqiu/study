#!/usr/bin/env python
#-*- coding:utf-8 -*-

def M(n):
    return max(a for a in range(n) if (a * a) % n == a)

def f(m):
    return sum(M(n) for n in range(1, m + 1))

def _f(m):
    pass

def main():
    print f(5000) # 8526046
    #print _f(10)

if __name__ == "__main__":
    main()
