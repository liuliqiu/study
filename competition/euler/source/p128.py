from Crazy import isprime


def ne(l):
    return list(range(2 * l[-1] - l[-2], 8 * l[-1] - 7 * l[-2] + 6, l[-1] - l[-2] + 1))


def prnums(l):
    return len([i for i in l if isprime(i)])


def f(n):
    num = 1
    l = [i for i in range(2, 8)]
    t = [1 for i in range(6)], l, ne(l)
    ##    print(t)
    while num < n:
        for i in range(6):
            v = t[1][i]
            temp = t[2][i] - t[1][i]
            if i == 0:
                l = [temp - 1, temp + 1, t[2][5] * 2 - t[2][4] - 1 - v]
            else:

                l = [v - t[0][i], temp - 1, temp + 1]
            if prnums(l) == 3:
                num += 1
                if num % 100 == 0:
                    print(num, v)
                ##                print(num,v,l)
                if num == n:
                    return v
        v = t[2][0] - 1
        l = [
            t[2][5] * 2 - t[2][4] - 1 - v,
            t[2][5] * 2 - t[2][4] - 2 - v,
            v - t[0][0],
            v - t[1][0],
            v - t[1][0] - 1,
        ]
        if prnums(l) == 3:
            num += 1
            if num % 100 == 0:
                print(num, v)
            ##            print(num,v,l)
            if num == n:
                return v
        t = t[1], t[2], ne(t[2])


print(f(2000))
