##By replacing the 1st digit of *3, it turns out that six of the nine possible
##values: 13, 23, 43, 53, 73, and 83, are all prime.
##By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit
##number is the first example having seven primes among the ten generated numbers,
##yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993.
##Consequently 56003, being the first member of this family, is the smallest
##prime with this property.
##Find the smallest prime which, by replacing part of the number (not necessarily
##adjacent digits) with the same digit, is part of an eight prime value family.
from Crazy import isprime
from Crazy import MutiR
from Crazy import primes


def maketem():
    def m(x, y):
        if x == 0 and y == 0:
            yield ()
        if x > 0:
            for i in m(x - 1, y):
                yield (True,) + i
        if y > 0:
            for i in m(x, y - 1):
                yield (False,) + i

    for i in m(3, 2):
        yield i + (False,)


def ft(tem, s):
    a = b = 0
    j = 0
    for i in range(len(tem)):
        if tem[i]:
            b = b + 10 ** (len(tem) - i - 1)
        else:
            a = a + s[j] * 10 ** (len(tem) - i - 1)
            j = j + 1
    return lambda x: b * x + a


def f(s):
    ##    if s[2]==s[3]==0 and s[4]==1:
    ##        print(s)
    for tem in maketem():
        f = ft(tem, s)
        if tem[0]:
            mr = 1
        else:
            mr = 0
        if len([i for i in range(mr, 10) if isprime(f(i))]) >= 8:
            print(tem, s)
    return False


def fi():
    return [f(s) for s in MutiR(range(1, 10), range(10), [1, 3, 7, 9])]


fi()
