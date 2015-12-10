def f():
    g=lambda c:-1 if c=='-' else int(c)
    x=[[g(c) for c in line.strip().split(',')] for line in open('txt/network.txt')]
    G,i=set(),0
    n=len(x)
    U=set(range(n))
    All=0
    for a in U:
        for b in U:
            if x[a][b]>0:
                All+=x[a][b]
    result=0
    while len(G)<(n-1):
        G.add(i)
        Mini=-1
        temp=(0,0)
        for a in G:
            for b in U.difference(G):
                if x[a][b]>0:
                    if Mini<0:
                        Mini=x[a][b]
                        temp=(a,b)
                    elif x[a][b]<Mini:
                        Mini=x[a][b]
                        temp=(a,b)
        result+=Mini
##        print(temp)
        i=temp[1]
    return All//2-result
print(f())
