
def f():
    n=5000
    result=-600000000000
    g=lambda r:sum((900-3*i)*(r**(i-1)) for i in range(1,n+1))
    r=0
    re=0
    for i in range(14):
        ba=10**(-i)
        j=0
        while g(re)>result:
            re=re+ba
        re-=ba
    print(re)
f()
