#-*- coding:utf-8 -*-

from itertools import count, combinations_with_replacement
from prime import primes, isprime

def R(k):
    return sum(10**i for i in range(k))

def A(n):
    if n%2 ==0 or n%5 == 0:
        return 0
    Ri = 0
    ni = 1
    for i in count(1):
        Ri = (ni + Ri) % n
        ni = (ni * 10) % n
        if Ri % n == 0:
            return i

def is_ok(n):
    An = A(n)
    return An != 0 and (n - 1) % An == 0

def f(n):
    result = []
    number = 0
    for i in count(91):
        if i%2 == 0 or i%5 == 0:
            continue
        if (not isprime(i)) and is_ok(i):
            result.append(i)
            number += 1
            if number == n:
                break
    return sum(result)



def main():
    print f(25)
    #149253
    #f(25)
    #print A(7), A(41)
