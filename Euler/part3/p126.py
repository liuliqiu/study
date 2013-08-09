from itertools import combinations_with_replacement
from collections import defaultdict
def g(a,b,c):
    i=0
    while True:
        yield 2*(a*b+b*c+c*a)+4*i*(a+b+c)+4*i*(i-1)
        i=i+1
def f(n):
    M=1000
    Re=defaultdict(int)
    for i in combinations_with_replacement(range(1,100),3):
        N=g(*i)
        v=next(N)
        while v<M:
            if v==154:
                print(i)
            Re[v]+=1
            v=next(N)
    return min(i for i in Re if Re[i]==n);
##print(f(10))

from collections import Counter
def S(T):
    l=[]
    for a in range(1,T//2):
        for b in range(1,min(a+1,(T+1)//(a+1))):
            for c in range(1,min(b+1,(T-a*b+a+b)//(a+b))):
                if a*b+b*c+a*c<=10000:
                    l.append((a+b+c,(a*b+b*c+a*c)))
    return Counter(l)
PS=S(10000)
Eq3=lambda x:(x-1)//3+1
def issquare(x):
    t=int(x**0.5)
    if t*t==x:
        return True,t
    else:
        return False,None
def P3(SUM,SUM2):
    '''a+b+c=SUM,a*b+b*c+a*c=SUM2'''
##    for a in range(Eq3(SUM),SUM-1):
##        isP2,b,c=P2(SUM-a,SUM2+a*a-a*SUM)
####        print(isP2,a,b,c)
##        if isP2 and 0<b<=a and 0<c<=a:
##            yield a,b,c
    if (SUM,SUM2) in PS:
        return PS[(SUM,SUM2)]
    else:
        return 0
def P2(SUM,SUM2):
    '''a+b=SUM,a*b=SUM2'''
    S=SUM**2-4*SUM2
    if S<0:
        return False,None,None
    issq,sq=issquare(S)
    if not issq or (SUM-sq)%2!=0 or SUM<=sq:
        return False,None,None
    else:
        return True,(sq+SUM)//2,(SUM-sq)//2
def Q(SUM2):
    '''a*b+b*c+a*c=SUM2'''
##    print(SUM2,Eq3(SUM2),int(Eq3(SUM2)**0.5),(SUM2-1)//2+1)
    for a in range(int(Eq3(SUM2)**0.5),(SUM2-1)//2+1):
##        print(a,(SUM2-a)//(a+1)+2)
        for S2 in range(2,(SUM2-a)//(a+1)+2):
            isP2,b,c=P2(S2,SUM2-a*S2)
##            print(S2,SUM2-a*S2,isP2,b,c)
            if isP2 and 0<b<=a and 0<c<=a:
                yield a,b,c
def C(SUM):
    '''2*i*i+2*i*(a+b+c-1)+a*b+b*c+a*c=SUM'''
    re=len(list(Q(SUM)))#i=0
    i=1
    while 2*i*i+4*i+3<=SUM:
        T=SUM-2*i*(i-1)
        #int((9*i*i+3*T)**0.5)-3*i
        for S3 in range(int((9*i*i+3*T)**0.5)-3*i,(T+4*i-1)//(2*i+2)+1):
##            re+=len(list(P3(S3,T-2*i*S3)))
            re+=P3(S3,T-2*i*S3)
        i+=1
    return re
def test(m):
    for a,b,c in Q(m):
        print(a,b,c)
def f2(n):
    i=0
    while True:
        if i%100==0:
            print(i,C(i))
        if C(i)==n:
            return 2*i
        i+=1
##print(f2(10))
from timeit import Timer
def test():
    print(f2(1000))
t=Timer("test()","from __main__ import test")
print(t.timeit(1))
