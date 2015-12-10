def f(n):
    L=[1]
    M=[1]
    i=1
    j=k=1
    re=1
    r=2
    while M[-1]<n**3:
        i+=1
        if i>L[j-1]:
            j+=1
        if r**3<=M[-1]+j*i and r<n:
            if r%10000==0:
                print(r)
            re+=(L[-1]+1+(r**3-M[-1]-1)//i)
            r+=1
        L.append(L[-1]+j)
        M.append(M[-1]+j*i)
##    print(L)
##    print(M)
    return re
def main():
    print(f(10**6))
main()
