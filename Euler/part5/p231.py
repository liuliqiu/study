from collections import Counter
def factors(n):
    factor=2
    while factor**2<=n:
        while n%factor==0:
            n=n//factor
            yield factor
        factor+=1 if factor==2 else 2
    if n>1:
        yield n
def facs(k,n):
    for i in range(k+1,n+1):
        if i%10000==0:
            print(i)
        for j in factors(i):
            yield j
##def f(n,k):
##    if k>n//2:
##        k=n-k
##    c1=Counter(facs(n-k,n))
##    c2=Counter(facs(1,k))
##    c1.subtract(c2)
##    return sum(i*c1[i] for i in c1)
def f(n,k):
    re=0
    if k>n//2:
        k=n-k
    for i in range(n-k+1,n+1):
        if i%10000==0:
            print(i)
        re+=sum(factors(i))
    for i in range(1,k+1):
        if i%10000==0:
            print(i)
        re-=sum(factors(i))
    return re
print(f(20000000,15000000))
#7526965179680
##print(f(10,3))
