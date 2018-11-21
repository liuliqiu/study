def s(n):
    if n == 1:
        yield "0"
        yield "1"
    else:
        for i in s(n - 1):
            yield i + "0"
            yield i + "1"


def f(n):
    S = set(s(n))
    result = []

    def g(now, remainder):
        k = ["0", "1"]
        for c in k:
            if (now + c)[-n:] in remainder:
                if len(remainder) > 1:
                    remainder.remove((now + c)[-n:])
                    g(now + c, remainder)
                    remainder.add((now + c)[-n:])
                else:
                    result.append(now + c)

    def k(s):
        re = 0
        for c in s:
            re = re * 2 + int(c)
        return re

    begin = "0" * n
    S.remove(begin)
    g(begin, S)
    ##    print(result)
    result = map(
        lambda s: s[: 1 - n], filter(lambda s: s[1 - n :] == "0" * (n - 1), result)
    )
    return sum(k(s) for s in result)


print(f(5))
