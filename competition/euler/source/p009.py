##A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,
##a^2 + b^2 = c^2
##For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.
##There exists exactly one Pythagorean triplet for which a + b + c = 1000.
##Find the product abc.

def square(x):
    return x*x
def fi(x):
    a=1
    b=2
    while a+b<x:
        c=x-a-b
        if square(a)+square(b)==square(c):
            return a*b*c
        b=b+1
        if a+b==x:
            a=a+1
            b=a+1
##print(fi(1000))
from math import ceil
def f(n):
    m=ceil(n/2)
    for b in range(ceil(m/2),m):
        for c in range(b+1,m):
            a=n-b-c
            if a*a+b*b==c*c:
                return a*b*c
def f2(n):
    m=ceil(n/2)
    l=[i*i for i in range(m)]
    for b in range(ceil(m/2),m):
        for c in range(b+1,m):
            a=n-b-c
            if l[a]+l[b]==l[c]:
                return a*b*c
##print(f(1000))
from timeit import Timer
def test():
    f(1000)
t=Timer("test()","from __main__ import test")
print(t.timeit(100))
