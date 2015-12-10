##If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
##
##Find the sum of all the multiples of 3 or 5 below 1000.

def f1(n):
    return sum(i for i in range(n) if i%3==0 or i%5==0)

def f(n):
    Sum=lambda x:(x*x+x)//2
    SumDivisibleBy=lambda k:Sum((n-1)//k)*k
    return SumDivisibleBy(3)+SumDivisibleBy(5)-SumDivisibleBy(15)

test_case = [(10, 23)]
x = 1000

