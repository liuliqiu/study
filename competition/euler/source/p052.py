##It can be seen that the number, 125874, and its double, 251748, contain
##exactly the same digits, but in a different order.
##Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
##contain the same digits.
def norptnumber(x):
    return len(str(x)) == len(set(str(x)))


def samedigits(x):
    return (
        set(str(x)) == set(str(2 * x))
        and set(str(x)) == set(str(3 * x))
        and set(str(x)) == set(str(4 * x))
        and set(str(x)) == set(str(5 * x))
        and set(str(x)) == set(str(6 * x))
    )


def fi():
    for i in range(2, 1000000):
        if norptnumber(i) and samedigits(i):
            return i


print(fi())
