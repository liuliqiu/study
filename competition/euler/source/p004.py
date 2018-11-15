##A palindromic number reads the same both ways. The largest palindrome made from
##the product of two 2-digit numbers is 9009 = 91  99.
##Find the largest palindrome made from the product of two 3-digit numbers.
from math import ceil
from functools import partial


def largest_palindrome_of_two_number_product(n):
    def make_palindromic(n):
        i = 1
        result = 0
        while n > 0:
            n, d = divmod(n, 10)
            result = result * 10 + (10 ** i + 1) * d
            i += 2
        return result

    def is_product_of_k(n, k):
        i = int(ceil(n ** 0.5))
        while i < 10 ** k:
            if n % i == 0:
                return True
            i += 1
        return False

    return next(
        filter(
            partial(is_product_of_k, k=n),
            map(make_palindromic, range(10 ** n - 1, 10 ** (n - 1) - 1, -1)),
        )
    )


def test_largest_palindrome_of_two_number_product():
    assert largest_palindrome_of_two_number_product(2) == 9009
    assert largest_palindrome_of_two_number_product(3) == 906609


def test_solve():
    assert solve(2) == 9009
    assert solve(3) == 906609


def is_palindromic(n):
    return str(n) == "".join(reversed(str(n)))


def solve_old():
    result = 0
    for i in range(999, 99, -1):
        if i * 999 <= result:
            break
        for j in range(999 if i % 11 == 0 else 990, i - 1, -1 if i % 11 == 0 else -11):
            if i * j <= result:
                break
            if is_palindromic(i * j) and i * j > result:
                result = i * j
    return result


def solve(n):
    N = (10 ** n) - 1
    x, y = (N, N)
    result = 0
    while ((x + y) / 2) ** 2 > result:
        while y <= x:
            temp = x * y
            if is_palindromic(temp) and temp > result:
                result = temp
            x, y = (x - 1, y + 1)
        x, y = (N, x + y - N - 1)
    return result
