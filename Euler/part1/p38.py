##Take the number 192 and multiply it by each of 1, 2, and 3:
##192*1 = 192
##192*2 = 384
##192*3 = 576
##By concatenating each product we get the 1 to 9 pandigital, 192384576. We will
##call 192384576 the concatenated product of 192 and (1,2,3)
##The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5
##, giving the pandigital, 918273645, which is the concatenated product of 9 and
##(1,2,3,4,5).
##What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
##concatenated product of an integer with (1,2, ... , n) where n  1?
from functools import reduce
def ispandigital(s):
    return len(s)==9 and len(set(s))==9 and '0' not in s
def connumber(n,v):
    return reduce(lambda x,y:x+y,[str(n*i) for i in v])
def mr(n):
    return range(1,n+1)
def fi():
    ##return list(10//i for i in range(2,10))
    return max(connumber(n,mr(i))  for n in range(1,(10**(10//i))) if ispandigital(connumber(n,mr(i))))
print(fi())
    
    
