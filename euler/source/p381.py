
#-*- coding:utf-8 -*-

"""
(prime-k) factorial
For a prime p let S(p) = (∑(p-k)!) mod(p) for 1 ≤ k ≤ 5.

For example, if p=7,
(7-1)! + (7-2)! + (7-3)! + (7-4)! + (7-5)! = 6! + 5! + 4! + 3! + 2! = 720+120+24+6+2 = 872.
As 872 mod(7) = 4, S(7) = 4.

It can be verified that ∑S(p) = 480 for 5 ≤ p < 100.

Find ∑S(p) for 5 ≤ p < 10**8.
"""

from eulertools import primes, skip, inverse_mod


def S(p):
    l = [(p - 2), (p - 2) * (p - 3), (p - 2) * (p - 3) * (p - 4)]
    return sum(inverse_mod(i, p) for i in l) % p

def f(n):
    return sum(map(S, skip(primes(n), 2)))


def main():
    #print f(100) # 480
    print f(10 ** 5) # 226591981 time:0.09s
    #print f(10 ** 8) # 139602943319822  time: 84.00s


if __name__ == "__main__":
    main()
