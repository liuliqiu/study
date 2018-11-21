##Consider quadratic Diophantine equations of the form:
##x^2 – D*y^2 = 1
##For example, when D=13, the minimal solution in x is 6492 – 131802 = 1.
##
##It can be assumed that there are no solutions in positive integers when D is
##square.
##By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the
##following:
##3^2 – 2*2^2 = 1
##2^2 – 3*1^2 = 1
##9^2 – 5*4^2 = 1
##5^2 – 6*2^2 = 1
##8^2 – 7*3^2 = 1
##
##Hence, by considering minimal solutions in x for D<=7, the largest x is
##obtained when D=5.
##
##Find the value of D<=1000 in minimal solutions of x for which the largest
##value of x is obtained.

from Crazy import divisor
import math


def f(n):
    m = n ** 0.5
    x = []
    y = [1]
    z = [int(m)]
    ss = []
    p, q = 1, int(m)
    i = 0
    while True:
        t1 = n - q ** 2
        s = divisor(t1, p)
        t1 = t1 // s
        t3 = int((p * q) // s)
        s2 = int((m + t3) // t1)
        ##        print(p,q,s,t1,t3,ss)
        ss.append(s2)
        p, q = t1, s2 * t1 - t3
        if s2 == 2 * int(m):
            ##            print(s2,ss)
            break
        i = i + 1
    return (int(m), ss)


def g(n):
    sq, arr = f(n)
    ##    print(sq,arr)
    i = 0
    l = len(arr)
    while True:
        p, q = 0, 1
        for j in range(i, -1, -1):
            p, q = q, q * arr[j % l] + p
        p = p + q * sq
        ##        print(p,q,p*p-n*q*q)
        if p * p - n * q * q == 1:
            return p
        i = i + 1


def fi():
    a, b = 0, 0
    for i in range(2, 1000):
        if int(i ** 0.5) ** 2 != i:
            t = g(i)
            ##            print(i,t)
            if t > b:
                a, b = i, t
    return a


##print(g(2)==3)
##print(g(3)==2)
##print(g(5)==9)
##print(g(6)==5)
##print(g(7)==8)
print(fi())
##print(g(61))
