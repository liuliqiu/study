##A number chain is created by continuously adding the square of the digits in a
##number to form a new number until it has been seen before.
##For example,
##44→32→13→10→1→1
##85→89→145→42→20→4→16→37→58→89
##Therefore any chain that arrives at 1 or 89 will become stuck in an endless
##loop. What is most amazing is that EVERY starting number will eventually
##arrive at 1 or 89.
##How many starting numbers below ten million will arrive at 89?

maxlen = 10000000


def fi():
    v = [False, False, True]

    def f(n):
        if n < len(v):
            return v[n]
        s = int("".join(sorted(str(n))))
        if s < len(v):
            return v[s]
        return f(sum(int(c) ** 2 for c in str(n)))

    for i in range(3, maxlen):
        if i % 100000 == 0:
            print(i)
        v.append(f(i))
    return len([i for i in v if i])


print(fi())
