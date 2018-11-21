##Euler published the remarkable quadratic formula:
##n² + n + 41
##It turns out that the formula will produce 40 primes for the consecutive values
##n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is
##divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible
##by 41.
##Using computers, the incredible formula  n²  79n + 1601 was discovered, which
##produces 80 primes for the consecutive values n = 0 to 79. The product of the
##coefficients, 79 and 1601, is 126479.
##Considering quadratics of the form:
##n² + an + b, where |a|  1000 and |b|  1000
##where |n| is the modulus/absolute value of n
##e.g. |11| = 11 and |4| = 4
##Find the product of the coefficients, a and b, for the quadratic expression that
##produces the maximum number of primes for consecutive values of n,
##starting with n = 0.


def fi():
    primes = [2]
    for i in range(3, 1000, 2):
        for j in primes:
            if j * j > i:
                primes.append(i)
                break
            if i % j == 0:
                break

    def isprime(n):
        if n < 1000:
            return n in primes
        elif n % 2 == 0:
            return False
        else:
            x = 3
            while x * x <= n:
                if n % x:
                    return False
                x = x + 1
            return True

    def f(a, b):
        for n in range(1, 1000):
            if not isprime(n * n + a * n + b):
                return n

    re = 0
    z = 0
    for a in range(-999, 1000):
        for b in primes:
            if f(a, b) > re:
                re = f(a, b)
                z = a * b
    return z


print(fi())
