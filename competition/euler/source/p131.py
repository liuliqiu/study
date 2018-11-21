from Crazy import isprime


def f(n):
    i = 2
    S = set()
    while i * (3 * i - 3) + 1 < n:
        j = i - 1
        while j > 0:
            t = i ** 3 - j ** 3
            if isprime(t):
                S.add(t)
            if t > n:
                break
            j -= 1
        i += 1
    return len(S)


print(f(1000000))
