##145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
##
##Find the sum of all numbers which are equal to the sum of the factorial of their digits.
##
##Note: as 1! = 1 and 2! = 2 are not sums they are not included.
v = [1]
for i in range(1, 10):
    v.append(v[-1] * i)


def cu(x):
    return sum([v[ord(i) - 48] for i in str(x)])


def fi():
    return sum([x for x in range(10, v[-1] * 6) if cu(x) == x])


def dig(i1, i2, i3, i4, i5, i6):
    return i1 * 100000 + i2 * 10000 + i3 * 1000 + i4 * 100 + i5 * 10 + i6


def s(i1, i2, i3, i4, i5, i6):
    return v[i1] + v[i2] + v[i3] + v[i4] + v[i5] + v[i6]


x = sum(
    [
        s(i1, i2, i3, i4, i5, i6)
        for i1 in range(10)
        for i2 in range(10)
        for i3 in range(10)
        for i4 in range(10)
        for i5 in range(10)
        for i6 in range(10)
        if dig(i1, i2, i3, i4, i5, i6) == s(i1, i2, i3, i4, i5, i6)
        and dig(i1, i2, i3, i4, i5, i6) in range(10, v[-1] * 6)
    ]
)
print(x)
