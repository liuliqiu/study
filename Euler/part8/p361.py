#-*- coding:utf-8 -*-

from itertools import count

def to_2(n):
    return map(int, "{0:b}".format(n))

def g(n):
    bn = to_2(n)
    for i in range(0, len(bn), 2):
        if i + 1 < len(bn) and bn[i] == bn[i + 1]:
            break
    else:
        return True
    for i in range(1, len(bn), 2):
        if i + 1 < len(bn) and bn[i] == bn[i + 1]:
            break
    else:
        return True
    return False

def f(x):
    j = 0
    for i in count(0):
        if g(i):
            j += 1
            if j == x:
                return i

def main():
    #print g(7)
    #print filter(g, range(20))

    #3251
    print f(100)
    #TODO Wrong Answer
