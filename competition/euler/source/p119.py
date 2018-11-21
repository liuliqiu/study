def g(n):
    return sum(int(c) for c in str(n))


def f(n):
    result = set()
    for i in range(2, 100):
        for j in range(2, 10):
            if i == g(i ** j):
                result.add(i ** j)
    print(len(result), result)
    return list(sorted(result))[n - 1]


print(f(30))
