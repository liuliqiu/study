def makeU(l):
    def F(x):
        result = 0
        for i in l[:0:-1]:
            result = (result + i) * x
        return result + l[0]

    return F


def f1(L):
    F = makeU(L)
    Values = [F(i) for i in range(1, len(L))]
    X = [1, 1]
    result = 0
    for i in range(1, len(L)):
        print(X, Values)
        result += sum(
            j * k * l
            for j, k, l in zip(
                X[:-1], Values, [(-1) ** (i + t - 1) for t in range(len(L) + 1)]
            )
        )
        Temp = []
        for j in range(len(X) + 1):
            if j == 0 or j == len(X):
                Temp.append(1)
            else:
                Temp.append(X[j] + X[j - 1])
        X = Temp
    print(result)


##f1([0,0,0,1])
f1([(-1) ** i for i in range(11)])
