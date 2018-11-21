##Surprisingly there are only three numbers that can be written as the sum of
##fourth powers of their digits:
##1634 = 1^4 + 6^4 + 3^4 + 4^4
##8208 = 8^4 + 2^4 + 0^4 + 8^4
##9474 = 9^4 + 4^4 + 7^4 + 4^4
##As 1 = 14 is not a sum it is not included.
##The sum of these numbers is 1634 + 8208 + 9474 = 19316.
##Find the sum of all the numbers that can be written as the sum of fifth
##powers of their digits.

import math


def fi(n):
    dn = [i ** n for i in range(10)]

    def f(x):
        return sum(
            [dn[(x // (10 ** i)) % 10] for i in range(math.floor(math.log10(x)) + 1)]
        )

    k = n
    while (9 ** 5) * k > (10 ** (k - 1)):
        k = k + 1
    k = k - 1
    x = [i for i in range(2, (9 ** 5) * k) if f(i) == i]
    print(x)
    return sum(x)


print(fi(5))
