##It is possible to write ten as the sum of primes in exactly five different
##ways:
##
##7 + 3
##5 + 5
##5 + 3 + 2
##3 + 3 + 2 + 2
##2 + 2 + 2 + 2 + 2
##
##What is the first value which can be written as the sum of primes in over five
##thousand different ways?
MAX=100
from Crazy import isprime,primes
ps=primes(MAX)
def p77(num):
    def cachnum(n,k):
        return k*(MAX+1)+n
    Cached={}
    for n in range(MAX):
        for k in range(MAX):
            x=cachnum(n,k)
            if n==0:
                Cached[x]=1
            elif n<k:
                Cached[x]=0
            elif n==k:
                Cached[x]=1
            else:
                Cached[x]=sum(Cached[cachnum(n-i,i)]for i in range(k,n+1) if i in ps)
            if Cached[x]-1>num and k==1:
                return n
print(p77(5000))
