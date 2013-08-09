from Crazy import primes
from fractions import Fraction
X=500
P=primes(500)
croaks="PPPPNNPPPNPPNPN"
##croaks="NN"
def p329():
    Prob=[]
    L={"N":[],"P":[]}
    for i in range(1,X+1):
        if i in P:
            L["N"].append(Fraction(1,3))
            L["P"].append(Fraction(2,3))
        else:
            L["N"].append(Fraction(2,3))
            L["P"].append(Fraction(1,3))
##    print(L)
    Re=L[croaks[-1]]
    for c in reversed(croaks[:-1]):
##        print(croaks[:-1],croaks[-1])
        T=L[c]
        Temp=[]
        for i in range(0,X):
            x=T[i]
            if i==0:
                x=x*Re[1]
            elif i==X-1:
                x=x*Re[i-1]
            else:
                x=x*Fraction(1,2)*(Re[i-1]+Re[i+1])
            Temp.append(x)
        Re=Temp
    return sum(Re)*Fraction(1,X)
print(p329())
