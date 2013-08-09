def f1():
    h1,k1=1,1
    h2,k2=2,3
    while True:
        h1,h2=h2,2*h2+h1
        k1,k2=k2,2*k2+k1
        if 2*h2*h2-1==k2*k2 and h2%2==1 and k2%2==1:
            if (k2-1)//2>10**12:
                return (h2+1)//2
print(f1())
