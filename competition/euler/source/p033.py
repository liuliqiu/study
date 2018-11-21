##The fraction 49/98 is a curious fraction, as an inexperienced mathematician in
##attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is
##correct, is obtained by cancelling the 9s.
##We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
##There are exactly four non-trivial examples of this type of fraction, less
##than one in value, and containing two digits in the numerator and denominator.
##If the product of these four fractions is given in its lowest common terms,
##find the value of the denominator.
def finddivisors(x, y):
    if x > y:
        return finddivisors(y, x)
    if x == 0:
        return y
    return finddivisors(y % x, x)


def consider(x, y):
    z = finddivisors(x, y)
    return (x // z, y // z)


def fi():
    a, b = 1, 1
    for i in range(2, 10):
        for j in range(1, i):
            for k in range(i, 10):
                if consider(j * 10 + k, k * 10 + i) == consider(j, i):
                    a, b = a * j, b * i
    a, b = consider(a, b)
    return b


print(fi())
