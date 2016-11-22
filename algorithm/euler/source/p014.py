##The following iterative sequence is defined for the set of positive integers:
##n→n/2 (n is even)
##n→3n + 1 (n is odd)
##Using the rule above and starting with 13, we generate the following sequence:
##13→40→20→10→5→16→8→4→2→1
##It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
##Which starting number, under one million, produces the longest chain?
##NOTE: Once the chain starts the terms are allowed to go above one million.

def f(x):
    if x%2==0:
        return x//2
    else:
        return 3*x+1
def fi(x):
    v={1:0}
    z=0
    result=0
    for i in range(1,x):
        if i in v:
            continue
        r=[i]
        while r[-1] not in v:
            r.append(f(r[-1]))
        if v[r[-1]]+len(r)>z:
            z=v[r[-1]]+len(r)
            result=i
        for j in range(len(r)):
            if(r[j]<x):
                v[r[j]]=v[r[-1]]+len(r)-j
    return result
print(fi(1000000))
        
