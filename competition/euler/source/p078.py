##Let p(n) represent the number of different ways in which n coins can be separated
##into piles. For example, five coins can separated into piles in exactly seven
##different ways, so p(5)=7.
##
##OOOOO
##OOOO   O
##OOO   OO
##OOO   O   O
##OO   OO   O
##OO   O   O   O
##O   O   O   O   O
##Find the least value of n for which p(n) is divisible by one million.


def p78():
    X = [[1]]
    i = 0
    while True:
        if i % 100 == 0:
            print(i)
        while len(X[0]) < (i // 2 + 1):
            X[0].append(1)
        while len(X) < (len(X[0]) + 2):
            X.append([])
        if (sum(X[0]) + 1) % 1000000 == 0:
            return i + 2
        for j in range(len(X[0])):
            X[j + 1].insert(0, (sum(X[0][j:]) + 1) % 1000000)
        del X[0]
        i += 1


def p78_2():
    def pentagonal(n):
        a, b = (n + 2) // 2, n % 2
        return int((3 * a * a + (-1 if b == 0 else 1) * a) / 2)

    penlist = [pentagonal(i) for i in range(1000)]
    L = [1]
    j = 1
    while L[-1] != 0:
        L.append(
            sum(
                (-1 if (i // 2) % 2 == 1 else 1) * L[-k]
                for i, k in enumerate(filter(lambda x: x <= j, penlist))
            )
            % 1000000
        )
        j += 1
        if j % 1000 == 0:
            print(j)
    return j - 1


print(p78_2())
