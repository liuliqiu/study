from Crazy import primes
from math import log
def g(a,b,m):
    l=[]
    while True:
        a1,b1=a%m,b%m
        if a1>m/2:
            a1-=m
        if b1>m/2:
            b1-=m
        if a1==1:
            re=b1
            for C in reversed(l):
                re=(C[0]*re+C[2])//C[1]
            return re
        l.append((m,a1,b1))
        a,b,m=m,-b1,a1
def f():
    ps=primes(1000100)
    i=2
    re=0
    while ps[i]<=1000000:
        p=ps[i]
        t=10**(int(log(p,10))+1)
        m=ps[i+1]
        j=g(t,m-p,m)%m
##        print(t*j+p)
        re+=t*j+p
        i+=1
    return re
print(f())
##print(g(10,2,7)%7)
##print(g(10,4,11)%11)
