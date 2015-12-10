def issquare(n):
    return (int(n**0.5)**2)==n
def isA(n):
    return issquare(n*n*2-7)
k=[2,4,8]
a,b=0,2
for i in range(20):
    A1=k[-1]*3-b
    if isA(A1):
        k.append(A1)
    else:
        break
    A2=k[-1]*2+a+b
    if isA(A2):
        k.append(A2)
    else:
        break
    a,b=a+b,b*5+4*a
print([i//2-1 for i in k])
print(sum(i//2-1 for i in k))
