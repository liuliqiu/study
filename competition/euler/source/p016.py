##2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
##What is the sum of the digits of the number 2^1000?
v = {0: 1, 1: 2}


def square(x):
    return x * x


def exp2(x):
    if x in v:
        return v[x]
    elif x % 2 == 0:
        return square(exp2(x // 2))
    else:
        return exp2(x // 2) * exp2(x // 2 + 1)


def fi(x):
    c = exp2(x)
    d = []
    while c > 0:
        d.append(c % 10)
        c = c // 10
    return lsum(d)


def lsum(l):
    s = 0
    for i in l:
        s = s + i
    return s


print(fi(1000))
