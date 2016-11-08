"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

from __future__ import division


def simple_sum_multiples_3_5_to(limit):
    return sum(i for i in range(limit) if i % 3 == 0 or i % 5 == 0)


def sum_multiples_3_5_to(limit):
    """
    >>> sum_multiples_3_5_to(10)
    23
    >>> sum_multiples_3_5_to(1000)
    233168
    """
    sum_to = lambda x: (x * x + x) // 2
    sum_divisible_by = lambda k: sum_to((limit - 1) // k) * k
    return sum_divisible_by(3) + sum_divisible_by(5) - sum_divisible_by(15)

