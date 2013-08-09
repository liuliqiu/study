##We shall say that an n-digit number is pandigital if it makes use of all the
##digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
##also prime.
##What is the largest n-digit pandigital prime that exists?
def isprime(n):
    if n==2:
        return True
    if n&1==0:
        return False
    for j in range(3,n,2):
        if j*j>n:
            return True
        if n%j==0:
            return False
def d(n):
    return list(range(1,n+1))
def pandnum(s):
    def f(n,r):
        if len(r)==1:
            yield n+r[0]
        else:
            for i in range(len(r)):
                for j in f((n+r[i])*10,r[:i]+r[i+1:]):
                    yield j
    for i in f(0,s):
        yield i
def fi():
    return max(i for j in range(2,9) for i in pandnum(d(j)) if j%3 and isprime(i))
print(fi())
