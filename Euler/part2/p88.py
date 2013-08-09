import math
def products(n):
    if n>0 and n&(n-1)==0:
        return int(math.log(n,2))*[2]
    prods=[]
    while n&1==0:
        n=n>>1
        prods.append(2)
    i=3
    while i*i<=n:
        while n%i==0:
            n=n//i
            prods.append(i)
        i+=2
    if n!=1:
        prods.append(n)
    return prods
def prod(n,m):
    for i in range(m,int(n**0.5)+1):
        if n%i==0:
            yield [i,n//i]
            for l in prod(n//i,i):
                yield l+[i]
    
def p88(n):
    i=4
    kset={i for i in range(2,n+1)}
    result=set()
    while len(kset)>0:
        for l in prod(i,2):
            if i-sum(l)+len(l) in kset:
                result.add(i)
                kset.remove(i-sum(l)+len(l))
        i+=1
##    print(result)
    return sum(result)
print(p88(12000))
##for l in prod(9,2):
##    print(l)
