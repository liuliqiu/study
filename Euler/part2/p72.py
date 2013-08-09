##Consider the fraction, n/d, where n and d are positive integers. If nd and
##HCF(n,d)=1, it is called a reduced proper fraction.
##
##If we list the set of reduced proper fractions for d  8 in ascending order of
##size, we get:
##
##1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7,
##3/4, 4/5, 5/6, 6/7, 7/8
##
##It can be seen that there are 21 elements in this set.
##
##How many elements would be contained in the set of reduced proper fractions
##for d 1,000,000?
def PrimeFactors(n):
    if n<2:
        return []
    i,s,re=3,n,[]
    if s&1==0:
        re.append(2)
    while s&1==0:
        s=s>>1
    while i*i<=s:
        if s%i==0:
            re.append(i)
        while s%i==0:
            s=s//i
        i=i+2
    if s>1 and s not in re:
        re.append(s)
    return re
def Euler(n):
    result=n
    for i in PrimeFactors(n):
        result=result//i*(i-1)
    return result
def TestPrimeFactors():
    Test={2:[2],3:[3],4:[2],5:[5],6:[2,3],7:[7],8:[2],9:[3],
          10:[2,5],11:[11],12:[2,3]}
    for i in Test:
##        print(PrimeFactors(i))
        print(PrimeFactors(i)==Test[i])
def TestEuler():
    Test={2:1,3:2,4:2,5:4,6:2,7:6,8:4,9:6,10:4,11:10,12:4}
    for i in Test:
        print(Euler(i)==Test[i])
##TestPrimeFactors()
##TestEuler()
def p72(n):
    return sum(Euler(i) for i in range(2,n+1))
##print(p72(8)==21)
print(p72(10**6))

