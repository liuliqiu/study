from itertools import permutations,product
lams=[lambda x,y:x+y,lambda x,y:x-y,lambda x,y:x*y,lambda x,y:x/y]
def maxnum(l):
    S=[s[2](s[1](s[0](i[0],i[1]),i[2]),i[3]) for i in permutations(l,4) for s in product(lams,repeat=3)]+[s[2](s[0](i[0],i[1]),s[1](i[2],i[3])) for i in permutations(l,4) for s in product(lams,repeat=3)]
    return min(set(range(1,400)).difference(set(filter(lambda x:x>0 and x-int(x)<10**-7,S))))-1
def p93():
    k=10
    for i in permutations(range(1,11),4):
        t=maxnum(i)
        if t>k:
            k=t
            print(i,k)
p93()
