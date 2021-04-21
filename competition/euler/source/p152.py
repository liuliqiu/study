#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
Writing 1/2 as a sum of inverse squares
How many ways are there to write the number 1/2 as a sum of inverse squares,
using distinct integers between 2 and 80 inclusive?

{2,3,4,5,7,12,15,20,28,35}
{2,3,4,6,7,9,10,20,28,35,36,45}
{2,3,4,6,7,9,12,15,28,30,35,36,45}

Because 1 / 2 > sum(1 / (x * x) for x in count(3)), 2 must in the integers。
so the question equal write the number 1 / 4 as a sum of inverse squares,
using distinct integers between 3 and 80 inclusive?

"""

from itertools import count, chain, product
from collections import defaultdict
from fractions import Fraction

from utils.prime import primes
from utils.eulertools import factorize_to, factorize


def find_sum(target, numbers, sum_numbers, index=0):
    """
    >>> find_sum(8, [1, 2, 3, 4, 5, 6], 21)
    4
    """
    if target > sum_numbers or target < 0:
        return 0
    elif target == sum_numbers:
        return 1
    else:
        first = numbers[index]
        last_sum = sum_numbers - first
        return find_sum(target, numbers, last_sum, index + 1) + find_sum(target - first, numbers, last_sum, index + 1)


def count_inverse_squares_old(number):
    """
    >>> count_inverse_squares(35)
    1
    """
    factorial = 1
    for p, n in [(2, 6), (3, 3), (5, 2), (7, 2), (11, 1), (13, 1)]:
        factorial *= (p ** n)
    target = (factorial // 2) ** 2
    numbers = tuple(
        (factorial // n) ** 2
        for n in range(3, number + 1)
        if factorial % n == 0
    )
    sum_numbers = sum(numbers)
    return find_sum(target, numbers, sum_numbers)


def count_inverse_squares(number):
    prime_list = list(reversed(list(primes(number // 2 + 1))))
    factories = dict(zip(count(3), factorize_to(number)[2:]))

    print(prime_list, factories)

    data = defaultdict(list)
    for n, fact in factories.items():
        data[max(fact.keys())].append((Fraction(1, n * n), (n, )))

    print(data)

    last_choices = [(0, tuple())]
    all_choices = [(0, tuple())]
    for p in prime_list:
        choices = data[p]
        for values, lc in product(power_set(choices, with_empty=False), last_choices):
            values = values + [lc]
            value = sum(v for v, l in values)
            lst = tuple(chain(*[l for v, l in values]))
            if p == 2:
                if value == Fraction(1, 4):
                    print(sorted(lst))
                    assert len(lst) == len(set(lst))
                    yield sorted(lst)
            else:
                if value.denominator % p != 0 and value <= Fraction(1, 4):
                    all_choices.append((value, lst))
        last_choices = all_choices
        all_choices = [(0, tuple())]

def max_factor(number):
    return max(factorize(number))

def power_set(choices, with_empty=True):
    marks = [1<<i for i in range(len(choices))]
    lst = list(zip(marks, choices))
    for i in range(0 if with_empty else 1, 2 ** len(choices)):
        yield [choice for mark, choice in lst if mark & i]


def main():
    # print count_inverse_squares(45) # old 27s

    # number    time        result
    # 45        0.55s       3
    # 55        2.15s       3
    # 65        10.54s      29
    # 70        21.53s      67
    # 80        84.87s      152 <error>
    result = list(count_inverse_squares(72))
    #print(result)
    print(len(result))

if __name__ == "__main__":
    main()

