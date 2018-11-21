def GaussianElimination(M, m, n):
    i, j = 0, 0
    while i < m and j < n:
        maxi = i
        for k in range(i + 1, m):
            if abs(M[k][j]) > abs(M[maxi][j]):
                maxi = k
        if M[maxi][j] != 0:
            M[i], M[maxi] = M[maxi], M[i]
            for k in range(n - 1, j - 1, -1):
                M[i][k] = M[i][k] / M[i][j]
            for k in range(i + 1, m):
                for l in range(n - 1, j - 1, -1):
                    M[k][l] = M[k][l] - M[k][j] * M[i][l]
            i = i + 1
        j = j + 1
    i = m - 1
    while i > -1:
        if M[i][i] == 1:
            for k in range(i):
                M[k][n - 1] = M[k][n - 1] - M[k][i] * M[i][n - 1]
                M[k][i] = 0
        i -= 1
    return [line[n - 1] for line in M]


def test1():
    M = [[2, 1, -1, 8], [-3, -1, 2, -11], [-2, 1, 2, -3]]
    print(GaussianElimination(M, 3, 4))
    M2 = [
        [-1, 0, 0.5, 0.5, 0],
        [0.5, -1, 0, 0.5, 0],
        [0.5, 0.5, -1, 0, 0],
        [1, 1, 1, 1, 1],
    ]
    print(GaussianElimination(M2, 4, 5))


def printM(M):
    for x in M:
        print(x)


def p84(n):
    l = list(range(1, n + 1)) + list(reversed(range(1, n)))
    for i in range(n):
        l[2 * i] -= 1 / (n * n)

    def ft(x):
        if x < 2 * n - 1:
            return l[x] / (n * n)
        else:
            return 0

    M = [[ft((j - i + 2 * n) % 40) for j in range(40)] for i in range(40)]
    for i in range(40):
        M[10][i] += M[30][i]
        M[30][i] = 0
        M[0][i] += (M[2][i] + M[17][i] + M[33][i] + M[7][i] + M[22][i]) / 16 + M[36][
            i
        ] / 15
        M[10][i] += (M[2][i] + M[17][i] + M[33][i] + M[7][i] + M[22][i]) / 16 + M[36][
            i
        ] / 15
        M[2][i] *= 7 / 8
        M[17][i] *= 7 / 8
        M[33][i] *= 7 / 8
        M[11][i] += (M[7][i] + M[22][i] + M[36][i]) / 16
        M[24][i] += (M[7][i] + M[22][i] + M[36][i]) / 16
        M[39][i] += (M[7][i] + M[22][i] + M[36][i]) / 16
        M[5][i] += (M[7][i] + M[22][i] + M[36][i]) / 16 + M[36][i] / 8
        M[15][i] += M[7][i] / 8
        M[25][i] += M[22][i] / 8
        M[12][i] += (M[7][i] + M[36][i]) / 16
        M[33][i] += M[36][i] * (13 / (16 * 15))
        M[4][i] += M[7][i] / 16
        M[28][i] += M[22][i] / 16
        M[19][i] += M[22][i] / 16
        M[7][i] *= 3 / 8
        M[22][i] *= 3 / 8
        M[36][i] *= 3 / 8
        M[10][i] += 1 / (n ** 3)
    for i in range(40):
        (M[i]).append(0)
    for i in range(40):
        M[i][i] -= 1
    for i in range(41):
        M[39][i] = 1
    result = GaussianElimination(M, 40, 41)
    result = sorted(
        [(i, j) for i, j in enumerate(result)], key=lambda x: x[1], reverse=True
    )
    print(result)


p84(6)
