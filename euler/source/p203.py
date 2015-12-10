from Crazy import primes
def factorial(n):
    re=1
    yield re
    for i in range(1,n+1):
        re*=i
        yield re
        
def f(n):
    L=list(factorial(n))
    S=set()
    ps=primes(n)
    def C(m,k):
        return L[m]//(L[k]*L[m-k])
    def notsquarefree(x):
        return all(x%(i*i)!=0 for i in ps)
    for i in range(n):
        for j in range(i//2+1):
            t=C(i,j)
            print(i,j,t)
            if notsquarefree(t):
                S.add(t)
##    print(S)
    return sum(S)
print(f(51))
