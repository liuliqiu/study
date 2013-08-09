##A permutation is an ordered arrangement of objects. For example, 3124 is one
##possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
##are listed numerically or alphabetically, we call it lexicographic order.
##The lexicographic permutations of 0, 1 and 2 are:
##012   021   102   120   201   210
##What is the millionth lexicographic permutation of the digits
##0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
from Crazy import *
def fi(x):
    v=[Factorial(i) for i in range(10)]
    n=[i for i in range(10)]
    p=0
    i=9
    print(v)
    while i>0:
        fn=v[i]
        j=(x-1)//fn
        print(i,j,n[j])
        p=p*10+n[j]
        n.remove(n[j])
        x=(x-1)%fn+1
        i=i-1
    p=p*10+n[0]
    return p
print(fi(1000000))
