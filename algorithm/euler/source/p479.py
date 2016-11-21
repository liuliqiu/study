#!/usr/bin/env python
#-*- coding:utf-8 -*-


"""
Roots on the Rise

Let ak, bk, and ck represent the three solutions (real or complex numbers) to the expression 1/x = (k/x)^2(k+x^2) - kx.

For instance, for k = 5, we see that {a5, b5, c5} is approximately {5.727244, -0.363622+2.057397i, -0.363622-2.057397i}.

Let S(n) = Σ (ak+bk)^p(bk+ck)^p(ck+ak)^p for all integers p, k such that 1 ≤ p, k ≤ n.

Interestingly, S(n) is always an integer. For example, S(4) = 51160.

Find S(10^6) modulo 1 000 000 007.

"""

"""
    1/x = (k/x)^2(k+x^2) - kx
=>  x^3 - k(x^2) + (1/k)x - k^3 = 0
=>  ak + bk + ck = k
    ak*bk + bk*ck + ck*ak = (1/k)
    ak*bk*ck = k^2

    (ak+bk)(bk+ck)(ck+ak)
=>  (ak + bk + ck) (ak * bk + bk * ck + ck * ak) - ak * bk * ck 
=>  k * (1/k) - k^2
=>  1 - k^2

    Σ(ak+bk)^p(bk+ck)^p(ck+ak)^p
=>  Σ(1-k^2)^p
=>  ((1 - k^2) ^ (p + 1) - 1) / (1 - k ^ 2 - 1) - 1

"""


from eulertools import exp_mod, inverse_mod

def f(k, n, p):
    """
        (k ** 1 + ... + k ** n) % p
    """
    if (k % p) == 1:
        return n % p
    else:
        t1 = exp_mod(k, n + 1, p) - k % p
        t2 = inverse_mod(k - 1, p)
        return (t1 * t2) % p


def S(n, p):
    result = 0
    for k in range(1, n + 1):
        t = 1 - k * k
        result = (result + f(t, n, p)) % p
    return result


def main():
    print S(10 ** 6, 1000000007) # 191541795    42.91s

if __name__ == "__main__":
    main()
