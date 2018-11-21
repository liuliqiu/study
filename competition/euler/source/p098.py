from itertools import permutations
from collections import Counter, defaultdict

issquare = lambda x: int(x ** 0.5) ** 2 == x


def g(s1, s2):
    s = list(set(s1))
    l = len(s)
    m = 0
    X = 1
    for x in permutations("0123456789", l):
        if X % 100000 == 0:
            print(X)
        X += 1
        t1, t2 = s1, s2
        for i in range(l):
            t1 = t1.replace(s[i], x[i])
            t2 = t2.replace(s[i], x[i])
        if t1[0] != "0" and t2[0] != "0" and issquare(int(t1)) and issquare(int(t2)):
            if int(t1) > m:
                m = int(t1)
            if int(t2) > m:
                m = int(t2)
    return m


def f1():
    txt = map(lambda x: x.strip('"'), open("txt/words.txt").read().strip().split(","))
    txt = sorted(txt, key=len, reverse=True)
    p = defaultdict(list)
    for s in txt:
        p[hash(str(Counter(s)))].append(s)
    for i in p:
        x = p[i]
        if len(x) == 2:
            print(x[0], x[1], g(x[0], x[1]))


f1()
##print(g('INTRODUCE','REDUCTION'))
