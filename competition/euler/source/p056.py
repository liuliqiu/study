##A googol (10^100) is a massive number: one followed by one-hundred zeros;
##100^100 is almost unimaginably large: one followed by two-hundred zeros.
##Despite their size, the sum of the digits in each number is only 1.
##Considering natural numbers of the form, ab, where a, b  100, what is the
##maximum digital sum?


def sumofdigits(n):
    return sum(int(i) for i in str(n))


def fi():
    return max(sumofdigits(i ** j) for i in range(2, 100) for j in range(2, 100))


print(fi())
