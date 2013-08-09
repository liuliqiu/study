##Starting with 1 and spiralling anticlockwise in the following way, a square
##spiral with side length 7 is formed.
##37 36 35 34 33 32 31
##38 17 16 15 14 13 30
##39 18  5  4  3 12 29
##40 19  6  1  2 11 28
##41 20  7  8  9 10 27
##42 21 22 23 24 25 26
##43 44 45 46 47 48 49
##It is interesting to note that the odd squares lie along the bottom right
##diagonal, but what is more interesting is that 8 out of the 13 numbers lying
##along both diagonals are prime; that is, a ratio of 8/13  62%.
##If one complete new layer is wrapped around the spiral above, a square spiral
##with side length 9 will be formed. If this process is continued, what is the
##side length of the square spiral for which the ratio of primes along both
##diagonals first falls below 10%?
from Crazy import isprime
def fi():
    a,b=0,1
    first=1
    mo=0
    for i in range(100000):
        mo=mo+2
        for j in range(3):
            first=first+mo
            if isprime(first):
                a=a+1
        first=first+mo
        b=b+4
        if i%1000==0:
            print(a,b)
        if b/a>10:
            return 2*i+3
print(fi())
