##There are exactly ten ways of selecting three from five, 12345:
##123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
##In combinatorics, we use the notation, 5C3 = 10.
##In general,
##nCr =	n!/r!(nr)!
##,where r  n, n! = n(n1)...321, and 0! = 1.
##It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.
##How many, not necessarily distinct, values of  nCr, for 1<=n<=100, are greater
##than one-million?
v=[1]
for i in range(1,101):
    v.append(v[-1]*i)
def C(n,r):
    return v[n]/(v[r]*v[n-r])
def fi():
    re=0
    for i in range(2,101):
        for j in range(0,i//2+1):
            if C(i,j)>1000000:
                re=re+i-2*j+1
                break
    return re
print(fi())
