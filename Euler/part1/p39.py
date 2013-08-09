##If p is the perimeter of a right angle triangle with integral length sides,
##{a,b,c}, there are exactly three solutions for p = 120.
##{20,48,52}, {24,45,51}, {30,40,50}
##For which value of p<=1000, is the number of solutions maximised?
def righangle(i,j,k):
    return (i*i+j*j)==k*k
def more(v):
    result={}
    for i in v:
        if i in result:
            result[i]=result[i]+1
        else:
            result[i]=1
    m=0
    k=0
    for i in result:
        if result[i]>k:
            k=result[i]
            m=i
    return m
def fi(n):
    return more([i+j+k for i in range(1,(n+1)//3) for j in range(i+1,(n-i+1)//2) for k in range(j+1,n-i-j+1) if righangle(i,j,k)])
print(fi(1000))
