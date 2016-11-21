#-*- coding:utf-8 -*-
##By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
##that the 6th prime is 13.
##What is the 10001st prime number?

def f(n):
    result=[2]
    i=3
    while len(result)<n:
        for j in result:
            if i%j==0:
                break
            elif j*j>i:
                result.append(i)

                break
        i=i+2
    return result[-1]

def sieve(n):
    '''使用[0,1,2,...,((n-1)//2)-1]来表示[3,5,7,...,((n-1)//2)*2+1]'''
    if n<2:
        raise StopIteration
    yield 2
    if n>2:
        k=[True for i in range((n-1)//2)]
        for i in range((n-1)//2):
            val=2*i+3
            if val*val>n:
                for j in range(i,(n-1)//2):
                    if k[j]:
                        yield 2*j+3
                break
            if k[i]:
                yield val
                for j in range(i+val,(n-1)//2,val):
                    k[j]=False
from math import log
def f2(n):
    ps=list(sieve(int(n*log(n)*1.2)))
    return ps[n-1]
def f3(n):
    if n==1:
        return 2
    else:
        Step=10000
        ps=list(sieve(2*Step+2))[1:]
        ##求第一个分段3- 2*Step+3的素数，然后去掉2。
        if n-2<len(ps):
            return ps[n-2]
        else:
            begin=3
            k=[True for i in range(Step)]
            while n-2>=len(ps):
                begin+=2*Step
                ##使用[0,1,2,...,Step-1]来表示[begin,begin+2,...begin+2*Step-2]
                end=2*Step+begin-2
                for i in range(Step):
                    k[i]=True
                for i in ps:
                    if i*i>end:
                        for j in range(Step):
                            if k[j]:
                                ps.append(2*j+begin)
                        break
                    NumModeI=((begin-1)//i)*i+i
                    ##求出比 大于或等于begin的最小的能被i整除的整数
                    if NumModeI%2==0:
                        NumModeI+=i
                    for j in range((NumModeI-begin)//2,Step,i):
                        k[j]=False
            return ps[n-2]
def f4(n):
    if n==1:
        return 2
    else:
        Step=1000
        ps=[list(sieve(2*Step+2))[1:]]
        if n-2<len(ps[0]):
            return ps[0][n-2]
        else:
            begin=3
            k=[True for i in range(Step)]
            R=len(ps[0])
            while n-2>=R:
                begin+=2*Step
                Val_Max=2*Step+begin-2
                for i in range(Step):
                    k[i]=True
                for i in (i for p in ps for i in p):
                    if i*i>Val_Max:
                        ps.append([2*j+begin for j in range(Step) if k[j]])
                        break
                    Temp=((begin-1)//i)*i+i
                    if Temp%2==0:
                        Temp+=i
                    for j in range((Temp-begin)//2,Step,i):
                        k[j]=False
                R+=len(ps[-1])
            return ps[-1][n-R-2]

from libs.prime import primes
from libs.eulertools import skip

def f5(n):
    return next(skip(primes(int(n*log(n)*1.2)), n - 1))

test_case = [(300001, 4256249)]
x = 10001
