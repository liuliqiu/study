##The prime 41, can be written as the sum of six consecutive primes:
##41 = 2 + 3 + 5 + 7 + 11 + 13
##This is the longest sum of consecutive primes that adds to a prime below
##one-hundred.
##The longest sum of consecutive primes below one-thousand that adds to a prime,
##contains 21 terms, and is equal to 953.
##Which prime, below one-million, can be written as the sum of the most consecutive
##primes?


def findprimes(n):
    v = [2]
    for i in range(3, n, 2):
        for j in v:
            if j * j > i:
                v.append(i)
                break
            if i % j == 0:
                break
    return v


def fi(z):
    r = findprimes(z)
    n = 1
    re = 0
    print(953 in r)
    for i in range(len(r)):
        if i + n > len(r):
            return re
        s = sum(r[i + j] for j in range(n))
        m = n
        while s < r[-1]:
            m = m + 1
            s = sum(r[i + j] for j in range(m))
            if s in r:
                re = s
                n = m
                print(s, i, m)


print(fi(1000000))
