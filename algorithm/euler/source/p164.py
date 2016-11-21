from itertools import *
def f():
    l=[i for i in product(range(10),repeat=2) if sum(i)<10]
    d={i:[j for j in l if sum(i)+j[0]<10 and i[1]+sum(j)<10] for i in l}
    k={i:len(d[i]) for i in d}
    for times in range(8):
        k={i:sum(k[j] for j in d[i]) for i in d}
    return sum(k[i] for i in k if i[0]!=0)
print(f())

    
