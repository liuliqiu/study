##Find the number of integers 1  n  107, for which n and n + 1 have the same
##number of positive divisors. For example, 14 has the positive divisors 1, 2, 7,
##14 while 15 has 1, 3, 5, 15.

from Crazy import isprime
def numofdivisors(n):
    S=1
    if n&1==0:
        while n&1==0:
            S=S+1
            n=n>>1
    j=3
    while j*j<=n:
        if n%j==0:
            i=1
            while n%j==0:
                i=i+1
                n=n//j
            S=S*i
        j=j+2
    if n!=1:
        S=S*2
    return S
def p179():
    result=1#2,3
    for i in range(3,10**7,2):
        if i%10000==1:
            print(i)
        if not isprime(i):
            a1=numofdivisors(i-1)
            a2=numofdivisors(i)
            a3=numofdivisors(i+1)
            if a1==a2:
##                print(i-1,i)
                result=result+1
            if a2==a3:
##                print(i,i+1)
                result=result+1
    return result
print(p179())#986262
##for i in range(2,10):
##    print(i,numofdivisors(i))
