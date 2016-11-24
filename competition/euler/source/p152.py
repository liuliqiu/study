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
from itertools import count
from collections import defaultdict

from utils.prime import primes
from utils.eulertools import factorize_to


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
    print factorial
    target = (factorial // 2) ** 2
    numbers = tuple(
        (factorial // n) ** 2
        for n in range(3, number + 1)
        if factorial % n == 0
    )
    print len(numbers)
    print target, numbers
    sum_numbers = sum(numbers)
    return find_sum(target, numbers, sum_numbers)



def count_inverse_squares(number):
    prime_list = list(reversed(list(primes(number / 3 + 1))))
    factories = dict(zip(count(2), factorize_to(number)[1:]))

    data = defaultdict(list)
    for n, fact in factories.items():
        data[max(fact.keys())].append(n)

    for p in prime_list:
        choises = data[p]
        print choises

def main():
    # print count_inverse_squares(45) # 27s
    print count_inverse_squares(35) # 27s

if __name__ == "__main__":
    main()

