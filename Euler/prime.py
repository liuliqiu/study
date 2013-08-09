#-*- coding:utf-8 -*-

def isprime(n):
    if n<2:
        return False
    if n==2:
        return True
    if n&1==0:
        return False
    for j in range(3,int(n**0.5)+1,2):
        if n%j==0:
            return False
    return True

def primes(n):
    if n<2:
        return []
    s=[i&1==1 for i in range(n+1)]
    s[2],s[1]=s[1],s[2]
    i=3
    while i*i<n+1:
        if s[i]:
            for j in range(i*i,n+1,i):
                s[j]=False
        i=i+1
    return (x for x in range(n+1) if s[x])


