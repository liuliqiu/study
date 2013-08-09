from Crazy import primes
def f1(n):
    ps=primes(3*10**5)
    for i,j in enumerate(ps,1):
        if i&1==1:
            if ((2*i)%j)*j>n:
                return i,j
print(f1(10**10))
