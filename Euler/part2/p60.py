##The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes
##and concatenating them in any order the result will always be prime. For example
##, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes,
##792, represents the lowest sum for a set of four primes with this property.

##Find the lowest sum for a set of five primes for which any two primes
##concatenate to produce another prime.
from Crazy import primes
from Crazy import isprime
filen=8
ps=primes(10**4)
def conisprime(n,m):
    return isprime(int(str(n)+str(m))) and isprime(int(str(m)+str(n)))
def fi():
    re={}
    for i in range(1,len(ps)):
        if len(str(ps[i]))<=4:
            for j in range(i):
                if len(str(ps[j]))<=filen-len(str(ps[i])) and conisprime(ps[i],ps[j]):
                    if ps[j] in re:
                        re[ps[j]].append(ps[i])
                    else:
                        re[ps[j]]=[ps[i]]
    for i in re:
        for j in range(len(re[i])):
            if len(re[i])>=4 and re[i][j] in re:
                for k in range(j+1,len(re[i])):
                    if re[i][k] in re[re[i][j]] and re[i][k] in re:
                        for l in range(k+1,len(re[i])):
                            if re[i][l] in re[re[i][j]] and re[i][l] in re[re[i][k]] and re[i][l] in re:
                                for m in range(l+1,len(re[i])):
                                    if re[i][m] in re[re[i][j]] and re[i][m] in re[re[i][k]] and re[i][m] in re[re[i][l]]:
                                        print(i,re[i][j],re[i][k],re[i][l],re[i][m])
def ts():
    t1=[3,7,109,673]
    t2=[23,311,677,827]
    for i in range(1,len(ps)):
        print(ps[i])
        if len(str(ps[i]))>4:
            return 
        if all(conisprime(ps[i],j) for j in t1):
            print(ps[i],t1)
        if all(conisprime(ps[i],j) for j in t2):
            print(ps[i],t2)
fi()
