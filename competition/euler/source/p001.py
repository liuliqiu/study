"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

from __future__ import division


def _sum_multiples_3_or_5(limit):
    """
        brute force
        循环找出所有符合条件的数，求和。
    """
    return sum(i for i in range(limit) if i % 3 == 0 or i % 5 == 0)


def sum_multiples_3_or_5(limit):
    """
        求出3的倍数的和加上5的倍数的和，减去重复加上的15的倍数的和
        求小于x的k的倍数的和时，先用求余求出数的个数，然后用等差数列的求和公式求出和。
    """
    sum_to = lambda x: (x * x + x) // 2
    sum_divisible_by = lambda k: sum_to((limit - 1) // k) * k
    return sum_divisible_by(3) + sum_divisible_by(5) - sum_divisible_by(15)


def test_sum_multiples():
    assert sum_multiples_3_or_5(10) == 23
    assert sum_multiples_3_or_5(1000) == 233168
