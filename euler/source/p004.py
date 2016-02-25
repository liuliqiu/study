##A palindromic number reads the same both ways. The largest palindrome made from
##the product of two 2-digit numbers is 9009 = 91  99.
##Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindromic(n):
    return str(n)==''.join(reversed(str(n)))

def f1():
    result=0
    for i in range(999,99,-1):
        if i*999<=result:
            break
        for j in range(999,i-1,-1):
            if i*j<=result:
                break
            if isPalindromic(i*j) and i*j>result:
                result=i*j;
    return result
def f2():
    result=0
    for i in range(999,99,-1):
        if i*999<=result:
            break
        for j in range(999 if i%11==0 else 990,i-1,-1 if i%11==0 else -11):
            if i*j<=result:
                break
            if isPalindromic(i*j) and i*j>result:
                result=i*j;
    return result
def f3():
    i=(999,999)
    result=0
    while (sum(i)/2)**2>result:
        while i[1]<=i[0]:
            if isPalindromic(i[0]*i[1]) and i[0]*i[1]>result:
                result=i[0]*i[1]
            i=(i[0]-1,i[1]+1)
        i=(999,sum(i)-1000)
    return result
from math import ceil
from itertools import ifilter

def f(n):
    def makePalindromic(x):
        return int(str(x)+''.join(reversed(str(x))))
    def isProductOfTwo(x):
        for i in range(int(ceil(x**0.5)),10 ** n):
            if x%i==0:
                return True
        return False
    return next(ifilter(isProductOfTwo,map(makePalindromic,range(10 ** n - 1,10 **(n - 1) - 1,-1))))
test_case = []
x = 3