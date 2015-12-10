##The prime factors of 13195 are 5, 7, 13 and 29.
##What is the largest prime factor of the number 600851475143 ?
def factors(n):
    factor=2
    while factor**2<=n:
        while n%factor==0:
            n=n//factor
            yield factor
        factor+=(2 if factor!=2 else 1)
    if n!=1:
        yield n


def f(n):
    return max(factors(n))


def TestFactors():
    tests=[8,9,12,3223,234435,345,345,3,34,234,24]
    for t in tests:
        print(t,list(factors(t)))

test_case = [(13195, 29)]
x = 600851475143

