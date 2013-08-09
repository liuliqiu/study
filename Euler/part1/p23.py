##A perfect number is a number for which the sum of its proper divisors is
##exactly equal to the number. For example, the sum of the proper divisors of
##28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
##A number n is called deficient if the sum of its proper divisors is less than
##n and it is called abundant if this sum exceeds n.
##As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
##number that can be written as the sum of two abundant numbers is 24. By
##mathematical analysis, it can be shown that all integers greater than 28123
##can be written as the sum of two abundant numbers. However, this upper limit
##cannot be reduced any further by analysis even though it is known that the
##greatest number that cannot be expressed as the sum of two abundant numbers
##is less than this limit.
##Find the sum of all the positive integers which cannot be written as the sum
##of two abundant numbers.

from Crazy import *
def d(n):
    a=divisors(n)
    a.remove(n)
    return lsum(a)
def fi():
    k=[]
    result=[]
    for i in range(28123):
        n=i+1
        if d(n)>n:
            k.append(n)
    s=0
    for i in range(28123):
        n=i+1
        for j in k:
            if j>=n:
                s=s+n
                break
            if n-j in k:
                break
        if n%300==0:
            print(n)
    return s

abundants = set(i for i in range(1,28124) if d(i) > i) 
def abundantsum(i):
    return any(i-a in abundants for a in abundants) 
print(sum(i for i in range(1,28124) if not abundantsum(i)))
