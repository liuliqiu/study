def f(a,b,c):
    def g(n):
        if n>b:
            return n-c
        else:
            return g(a+g(a+g(a+g(a+n))))
    for i in range(0,2000,10):
        print(i,g(i))
def S(a,b,c):
    re=(b*b+b)//2
    t=(b+1)//a
    re+=2*t*(t+1)*a*a
    re-=(3*t*(t+1)*a*c)//2
    re-=(t*c*a)
    re+=((b+1)%a)*((t+1)*(4*a-3*c)-c)
    return re
print(S(21**7,7**21,12**7))
