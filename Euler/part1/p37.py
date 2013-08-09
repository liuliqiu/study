##The number 3797 has an interesting property. Being prime itself, it is possible
##to continuously remove digits from left to right, and remain prime at each
##stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797,
##379, 37, and 3.
##Find the sum of the only eleven primes that are both truncatable from left to
##right and right to left.
##NOTE: 2, 3, 5, and 7 are not considered to be tr

import Crazy
def isprime(n):
    if n==2:
        return True
    if n%2==0:
        return False
    i=3
    while i*i<=n:
        if n%i==0:
            return False
        i=i+2
    return True
def num(n):
    return sum((10**(len(n)-1-i))*j for i,j in enumerate(n))
def isp(n):
    return isprime(num(n))
def istruncatable(n):
    l=len(n)
    return isp(n) and all(isp(n[:i]) and isp(n[l-i:]) for i in range(1,l))
def Searchs():
    v=([2,3,5,7],[3,7])
    while True:
        yield v
        v=v[:1]+([1,3,7,9],)+v[1:]
def fi():
    i=0
    result=0
    for s in Searchs():
        for n in Crazy.MutiS(s):
            if isp(n) and istruncatable(n):
                i=i+1
                result=result+num(n)
                if i==11:
                    return result
print(fi())
