##The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases
##by 3330, is unusual in two ways: (i) each of the three terms are prime, and,
##(ii) each of the 4-digit numbers are permutations of one another.
##There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
##exhibiting this property, but there is one other 4-digit increasing sequence.
##What 12-digit number do you form by concatenating the three terms in this
##sequence?
from Crazy import primes
from Crazy import isprime
from Crazy import MutiR
def m(s):
    return s[0]*1000+s[1]*100+s[2]*10+s[1]
def f(s):
    if len(s)==1:
        return [s[0]]
    else:
        v=[]
        for i in range(len(s)):
            for j in f(s[:i]+s[i+1:]):
                v.append(s[i]*10**(len(s)-1)+j)
        return v
def f2(s):
    r=f(s)
    for i in r:
        if isprime(i):
            for j in r:
                if i<j and isprime(j) and 2*j-i in r and isprime(2*j-i) and j<2*j-i:
                    print(i,j,2*j-i)
def fi():
    [f2(s) for s in MutiR(range(1,10),range(10),range(10),range(10)) if s[0]<=s[1]<=s[2]<=s[3] or s[1]==0 and s[1]<=s[2]<=s[3]]
fi()
