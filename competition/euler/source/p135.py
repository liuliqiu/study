from collections import defaultdict
def f(n):
    y=2
    Re=defaultdict(int)
    while y<n+4:
        for a in range(y//4+1,y-1):
            m=(4*a-y)*y
            if m>=n:
                break
            if 0<m<n:
                Re[m]+=1
        y+=1
    Re=[v for v in Re if Re[v]==10]
    return len(Re)
def f2(n):
    a=1
    Re=defaultdict(int)
    while 4*a-1<n:
        y=a+1
        if (3*a-1)*(a+1)>n:
            y=2*a+int((4*a*a-n)**0.5)
            while (4*a-y)*y>=n:
                y+=1
        while y<4*a:
            m=(4*a-y)*y
            if m>=n:
                y=4*a-y
            if 0<m<n:
                Re[m]+=1
            y+=1
        a+=1
    T=[v for v in Re if Re[v]==10]
    return len(T)
print(f2(10**6))
