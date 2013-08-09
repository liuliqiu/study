##All square roots are periodic when written as continued fractions and can be written in the form:
##
##sqrt(N) = a0 +	1/(a1 +	1/(a2 +	1/(a3 + ...)))
##For example, let us consider 23:
##
##sqrt(23) = 4 + sqrt(23) — 4 = 4 + 1/(1/(sqrt(23)—4)) = 4 + 1/(1 +(sqrt(23) – 3)/7)
##If we continue we would get the following expansion:
##
##23 = 4 +1/(1+1/(3 +1/(1 +(1/(8 + ...)))))
##It can be seen that the sequence is repeating. For conciseness, we use the
##notation 23 = [4;(1,3,1,8)], to indicate that the block (1,3,1,8) repeats
##indefinitely.
##
##The first ten continued fraction representations of (irrational) square roots
##are:
##
##2=[1;(2)], period=1
##3=[1;(1,2)], period=2
##5=[2;(4)], period=1
##6=[2;(2,4)], period=2
##7=[2;(1,1,1,4)], period=4
##8=[2;(1,4)], period=2
##10=[3;(6)], period=1
##11=[3;(3,6)], period=2
##12= [3;(2,6)], period=2
##13=[3;(1,1,1,1,6)], period=5
##
##Exactly four continued fractions, for N  13, have an odd period.
##
##How many continued fractions for N  10000 have an odd period?
from Crazy import divisor
def a(n):
    m=n**0.5
    x=[1]
    y=[1]
    z=[int(m)]
    ss=[int(m)]
    i=0
    while True:
        t1=(x[i]**2)*n-z[i]**2
        s=divisor(t1,y[i])
        t1=t1//s
        t2=int((y[i]*x[i])//s)
        t3=int((y[i]*z[i])//s)
        s2=int((t2*m+t3)//t1)
        ss.append(s2)
        for j in range(len(x)):
            if t1==y[j] and t2==x[j] and s2*t1-t3==z[j]:
                return ((len(x)-j)&1==1)
        y.append(t1)
        z.append(s2*t1-t3)
        x.append(t2)
        i=i+1
def fi(n):
    return len([i for i in range(2,n) if int(i**0.5)!=i**0.5 and a(i)])
print(fi(10001))
