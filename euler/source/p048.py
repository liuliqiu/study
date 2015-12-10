##The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
##
##Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

def f(n):
    result=1
    for i in range(1,n+1):
        result=(result*n)%(10**10)
        if result==0:
            return 0
    return result
def fi(n):
    return sum([f(i) for i in range(1,n+1)])%(10**10)
print(fi(1000))
