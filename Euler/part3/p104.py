##The Fibonacci sequence is defined by the recurrence relation:
##Fn = Fn1 + Fn2, where F1 = 1 and F2 = 1.
##It turns out that F541, which contains 113 digits, is the first Fibonacci number
##for which the last nine digits are 1-9 pandigital (contain all the digits 1 to 9
##, but not necessarily in order). And F2749, which contains 575 digits, is the
##first Fibonacci number for which the first nine digits are 1-9 pandigital.
##Given that Fk is the first Fibonacci number for which the first nine digits AND
##the last nine digits are 1-9 pandigital, find k.

def pandigital(n):
    return len(n)==len(set(n))==9 and '0' not in n
def p104():
    a,b,c=1,1,1
    e,f=1,1
    while True:
        a,b=(a+b)%(10**9),(a+2*b)%(10**9)
        e,f=e+f,e+2*f
        while e>10**15:
            e=e//10
            f=f//10
        if pandigital(str(a)) and pandigital(str(e)[0:9]):
            return 2*c+1
        if pandigital(str(b)) and pandigital(str(f)[0:9]):
            return 2*c+2
        c+=1
print(p104())
        
    

