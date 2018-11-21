"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

from __future__ import division


def factors(number):
    """
    >>> list(factors(8))
    [2, 2, 2]
    >>> list(factors(3223))
    [11, 293]
    """
    factor = 2
    while factor ** 2 <= number:
        while number % factor == 0:
            number = number // factor
            yield factor
        factor += 2 if factor != 2 else 1
    if number != 1:
        yield number


def largest_prime_factor(number):
    """
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(600851475143)
    6857
    """
    return max(factors(number))


def test_largest_prime_factor():
    assert largest_prime_factor(13195) == 29
    assert largest_prime_factor(600851475143) == 6857
