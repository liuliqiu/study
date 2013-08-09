##The Fibonacci sequence is defined by the recurrence relation:
##Fn = Fn1 + Fn2, where F1 = 1 and F2 = 1.
##Hence the first 12 terms will be:
##F1 = 1
##F2 = 1
##F3 = 2
##F4 = 3
##F5 = 5
##F6 = 8
##F7 = 13
##F8 = 21
##F9 = 34
##F10 = 55
##F11 = 89
##F12 = 144
##The 12th term, F12, is the first term to contain three digits.
##What is the first term in the Fibonacci sequence to contain 1000 digits?

import math
def fi(n):
    sqrt5=math.sqrt(5)
    print(1+sqrt5/2)
    return (n-1+math.log(sqrt5,10))/math.log((1+sqrt5)/2,10)
print(fi(1000))

