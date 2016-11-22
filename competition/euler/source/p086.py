Cached=set()
def HCD(a,b):
    if a>b:
        return HCD(b,a)
    if a==0:
        return b
    return HCD(b%a,a)
def tries():
    for m in range(2,1000):
        for n in range(1,min(m,2000//m+1)):
            t1=m*m-n*n
            t2=2*m*n
            t3=HCD(t1,t2)
            a=min(t1,t2)
            b=max(t1,t2)
            if(b<10000):
                Cached.add((a//t3,b//t3))
def p86(N):
    def Value(M):
        x=[i for i in Cached if i[1]<2*M]
##        if M==100:
##            print(x)
##        print(x)
        re=0
        for i in x:
            a,b=i
            if M%a==0 and b<2*a:
                t=M//a
##                print((b*t)//2-(b-a)*t+1,a,b)
                re+=(b*t)//2-(b-a)*t+1
##                print(re)
            if M%b==0:
                t=M//b
##                print((a*t)//2,a,b)
                re+=(a*t)//2
        return re
##    print(Value(N))
##    print(L)
    re=0
    for i in range(2000):
        re+=Value(i)
        if re>N:
            return i
tries()
print(p86(1000000))
