##The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
##Find the sum of all the primes below two million.


def primes(n):
    if n < 2:
        raise StopIteration
    else:
        yield 2
        l = [True for i in range((n - 1) // 2)]
        for i in range(len(l)):
            if l[i]:
                yield 2 * i + 3
                for j in range(3 * i + 3, len(l), 2 * i + 3):
                    l[j] = False


def f(n):
    return sum(primes(n))


print(f(2000000))
