
def m1():
    L=[1,2]
    h1,h2=1,1
    k1,k2=1,2
    i=1
    result=0
    while 4*k2*k2<10**9 or 2*((3*h2-k2)**2)<10**9:
        if abs(3*h2*h2-k2*k2)==1:
            if 4*k2*k2<10**9:
                result+=4*k2*k2
##                print(k2*k2-h2*h2,h2*h2+k2*k2)
            if 2*h2>k2:
                m=(h2*h2+(2*h2-k2)**2)
                n=2*(2*h2-k2)*h2
                result+=2*(m+n)
##                print(".",n,m)
        h1,h2=h2,(L[i%2]*h2+h1)
        k1,k2=k2,(L[i%2]*k2+k1)
        i+=1
    return result
print(m1())
