#!/usr/bin/env python
#-*- coding:utf-8 -*-



def T(n):
    a, b, c = 1, 1, 1
    while True:
        yield a, b, c
        a, b, c = b, c, (a + b + c) % n


def f(x):
    count = 0
    n = 3
    while True:
        L = []
        for i, (a, b, c) in enumerate(T(n)):
            L.append((a, b, c))
            if L[-1][-1] == 0:
                break
            elif i > 0 and L[i] == L[i / 2]:
                count += 1
                if count >= x:
                    return n
                break
        n += 2

def main():
    print f(124)

if __name__ == "__main__":
    main()
