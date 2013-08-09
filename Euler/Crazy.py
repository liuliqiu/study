#-*- coding:utf-8 -*-

from functools import reduce, partial

def splitnumber(n,i=10):
    c=n
    re=[]
    while c>0:
        re.append(c%i)
        c=c//i
    return re

def Factorial(n):
    v=[1]
    for i in range(2,n+1):
        v.append(v[-1]*i)
    return v[-1]

def divisors(n):
    if n<=1:
        return [1]
    v=[1,n]
    i=2
    while i*i<=n:
        if i*i==n:
            v.append(i)
            return v
        if n%i==0:
            v.append(i)
            v.append(n//i)
        i=i+1
    return v

def divisor(m,n):
    if m>n:
        return divisor(n,m)
    if m==0:
        return n
    return divisor(n%m,m)

def Reducible(a,b):
    c=divisor(a,b)
    return (a//c,b//c)

def MutiS(a):
    if len(a)==1:
        for i in a[0]:
            yield (i,)
    else:
        for i in a[0]:
            for j in MutiS(a[1:]):
                yield (i,)+j

def MutiR(*arg):
    for x in MutiS(arg):
        yield x

def muti(s):
    return reduce(lambda x,y:x*y,s)

