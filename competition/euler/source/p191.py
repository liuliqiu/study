def f(n):
    N3A = [1, 2, 4]
    while len(N3A) < n + 1:
        N3A.append(N3A[-1] + N3A[-2] + N3A[-3])
    return N3A[n] + sum(N3A[i] * N3A[n - 1 - i] for i in range(n))


print(f(30))
