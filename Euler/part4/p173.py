
def f(n):
    return sum(int(((m*m+n)**0.5-m)/2) for m in range(1,n//4))

