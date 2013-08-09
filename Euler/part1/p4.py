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
def f4():
    def makePalindromic(x):
        return int(str(x)+''.join(reversed(str(x))))
    def isProductOfTwo(x):
        for i in range(ceil(x**0.5),1000):
            if x%i==0:
                return True
        return False
    return next(filter(isProductOfTwo,map(makePalindromic,range(999,99,-1))))

##print(f1())
##print(f2())
##print(f3())
##print(f4())
from timeit import Timer
def test():
    f4()
t=Timer("test()","from __main__ import test")
print(t.timeit(100))
##print(f1())

