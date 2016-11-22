##It is well known that if the square root of a natural number is not an integer,
##then it is irrational. The decimal expansion of such square roots is infinite
##without any repeating pattern at all.
##
##The square root of two is 1.41421356237309504880..., and the digital sum of the
##first one hundred decimal digits is 475.
##
##For the first one hundred natural numbers, find the total of the digital sums of
##the first one hundred decimal digits for all the irrational square roots.

def sumdicemal(a,b):
    result,a=str(a//b),a%b
    while len(result)<100:
        a=a*10
        result+=str(a//b)
        a=a%b
    return sum(int(i) for i in result)
def decimal(p,l):
    if l==[]:
        return 0
    a,b=0,1
    while b<10**101:
        for i in range(len(l)):
            a,b=b,l[len(l)-1-i]*b+a
    return sumdicemal(a+p*b,b)
def HCF(a,b):
    if a<b:
        return HCF(b,a)
    if b==0:
        return a
    return HCF(b,a%b)
def H(m,n):
    k=HCF(m,n)
    return m//k,n//k
def ContinuedFraction(x):
    y=x**0.5
    p=int(y)
    if p*p==x:
        return p,[]
    c,a,d,L=1,p,1,[]
    while True:
        m=int(d*d*x-a*a)
        c,m=H(c,m)
        l=int(c*(d*y+a))
        k=l//m
        L.append(k)
        c,a,d=m,k*m-c*a,c*d
        if c==1 and a==p:
            break
    return p,L
def S(x):
    p,L=ContinuedFraction(x)
    return decimal(p,L)
def p80():
    return sum(S(i) for i in range(2,100))
print(p80())
