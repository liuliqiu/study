from collections import defaultdict,Counter
from math import ceil
def f(n):
    Re=defaultdict(int)
    for i in range(2,(n+1)//2+1):
        beg=1 if i*i<=n else ceil((i*i-n)**0.5)
        for j in range(i-2,beg-1,-2):
            Re[i*i-j*j]+=1
    c=Counter(Re.values())
    return sum(c[i] for i in c if 1<=i<=10)
print(f(1000000))
