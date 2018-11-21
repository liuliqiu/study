##2520 is the smallest number that can be divided by each of the numbers
##from 1 to 10 without any remainder.
##What is the smallest positive number that is evenly divisible by all of the
##numbers from 1 to 20?

from math import log
from functools import reduce

from libs.eulertools import LCM
from libs.prime import primes


def f2(x):
    a = 1
    for i in range(2, x + 1):
        a = LCM(a, i)
    return a


def f(n):
    return reduce(lambda x, y: x * y, (i ** int(log(n, i)) for i in primes(n)))


test_case = [(10, 2520)]
x = 20
