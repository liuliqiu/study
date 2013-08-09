##The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
##Find the sum of all numbers, less than one million, which are palindromic
##in base 10 and base 2.
##(Please note that the palindromic number, in either base, may not include
## leading zeros.)
import math
import Crazy
def ispalindromic(n,p=10):
    try:
        x=math.floor(math.log(n,p)+1)
    except:
        print(n,p)
    return all([((n//(p**i))%p==(n//(p**(x-i-1)))%p) for i in range(x//2+1)])
def fi():
    return sum([i for i in range(1,1000000,2) if ispalindromic(i) and ispalindromic(i,2)])
def fi2():
    a1=sum([i for i in range(1,10,2) if ispalindromic(i,2)])
    a2=sum([i*11 for i in range(1,10,2) if ispalindromic(i*11,2)])
    a3=sum([i*101+j*10 for i in range(1,10,2) for j in range(10) if ispalindromic(i*101+j*10,2)])
    a4=sum([i*1001+j*110 for i in range(1,10,2) for j in range(10) if ispalindromic(i*1001+j*110,2)])
    a5=sum([i*10001+j*1010+k*100 for i in range(1,10,2) for j in range(10) for k in range(10) if ispalindromic(i*10001+j*1010+k*100,2)])
    a6=sum([i*100001+j*10010+k*1100 for i in range(1,10,2) for j in range(10) for k in range(10) if ispalindromic(i*100001+j*10010+k*1100,2)])
    return a1+a2+a3+a4+a5+a6
print(fi2())
