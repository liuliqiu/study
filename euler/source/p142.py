from collections import defaultdict
def f():
    Cached=defaultdict(list)
    for i in range(1,10**4):
        for j in range(1,i):
            t1=(((2*i-1)**2+(2*j-1)**2)//2,((2*i-1)**2-(2*j-1)**2)//2)
            t2=(((2*i)**2+(2*j)**2)//2,((2*i)**2-(2*j)**2)//2)
##            print(t1)
##            print(t2)
            if t1[0] in Cached and t1[1] in Cached and len(set(Cached[t1[0]]).intersection(set(Cached[t1[1]])))>0:
                return sum(t1)+min(set(Cached[t1[0]]).intersection(set(Cached[t1[1]])))
            if t2[0] in Cached and t2[1] in Cached and len(set(Cached[t2[0]]).intersection(set(Cached[t2[1]])))>0:
                return sum(t2)+min(set(Cached[t2[0]]).intersection(set(Cached[t2[1]])))
            Cached[t1[0]].append(t1[1])
            Cached[t2[0]].append(t2[1])
##    print(Cached)
print(f())
