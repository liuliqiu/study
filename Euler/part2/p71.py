##Consider the fraction, n/d, where n and d are positive integers. If nd and
##HCF(n,d)=1, it is called a reduced proper fraction.
##If we list the set of reduced proper fractions for d  8 in ascending order of
##size, we get:
##1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7,
##3/4, 4/5, 5/6, 6/7, 7/8
##It can be seen that 2/5 is the fraction immediately to the left of 3/7.
##By listing the set of reduced proper fractions for d  1,000,000 in ascending
##order of size, find the numerator of the fraction immediately to the left of
##3/7.

def HCF(numer,denomin):
    if numer==0:
        return denomin
    else:
        return HCF(denomin%numer,numer)
def p71(n,numerator,denominator):
    tempnumer=0
    tempdenomin=1
    for denomin in range(n+1):
        numer=(denomin*numerator-1)//denominator
        if HCF(numer,denomin)==1 and numer*tempdenomin>denomin*tempnumer:
            tempdenomin=denomin
            tempnumer=numer
    return tempnumer
print(p71(1000000,3,7))
