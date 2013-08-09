##The radical of n, rad(n), is the product of distinct prime factors of n.
##For example, 504 = 2^3*3^2*7, so rad(504) = 2*3*7 = 42.
##
##If we calculate rad(n) for 1  n  10, then sort them on rad(n), and sorting on
##n if the radical values are equal, we get:
##
##Let E(k) be the kth element in the sorted n column; for example, E(4) = 8 and
##E(6) = 9.
##
##If rad(n) is sorted for 1<=n<=100000, find E(10000).
MAX=100000
def p124():
    L=[1 for i in range(MAX)]
    i=2
    while i<MAX:
        if L[i-1]==1:
            for j in range(i-1,MAX,i):
                L[j]=L[j]*i
        i=i+1
    K=list(enumerate(L))
    K.sort(key=lambda x :x[1])
    return K[10000-1]
print(p124())
