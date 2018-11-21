##An irrational decimal fraction is created by concatenating the positive
##integers:
##0.12345678910(1)112131415161718192021...
##It can be seen that the 12th digit of the fractional part is 1.
##If dn represents the nth digit of the fractional part, find the value of the
##following expression.
##d1*d10*d100*d1000*d10000*100000*d1000000

import Crazy


def d(n):
    x = n
    for i in range(1, 10):
        if x > i * (9 * 10 ** (i - 1)):
            x = x - i * (9 * 10 ** (i - 1))
        else:
            z = x % i
            x = (x + i - 1) // i
            x = x + 10 ** (i - 1) - 1
            return int(list(str(x))[(z + i - 1) % i])


def fi():
    return Crazy.muti(d(10 ** i) for i in range(7))


print(fi())
