##The number 145 is well known for the property that the sum of the factorial of
##its digits is equal to 145:
##
##1! + 4! + 5! = 1 + 24 + 120 = 145
##
##Perhaps less well known is 169, in that it produces the longest chain of numbers
##that link back to 169; it turns out that there are only three such loops that
##exist:
##
##169  363601  1454  169
##871  45361  871
##872  45362  872
##
##It is not difficult to prove that EVERY starting number will eventually get
##stuck in a loop. For example,
##
##69  363600  1454  169  363601 ( 1454)
##78  45360  871  45361 ( 871)
##540  145 ( 145)
##
##Starting with 69 produces a chain of five non-repeating terms, but the longest
##non-repeating chain with a starting number below one million is sixty terms.
##
##How many chains, with a starting number below one million, contain exactly sixty
##non-repeating terms?

F=[1]
for i in range(1,10):
    F.append(F[-1]*i)
def f(n):
    if n==0:
        return 1
    result=0
    while n>0:
        result,n=result+F[n%10],n//10
    return result
def p74():
    re={}
    re[145]=1
    re[169]=re[363601]=re[1454]=3
    re[871]=re[872]=re[45361]=re[45362]=2
    re[40585]=1
    re[1]=re[2]=1
    for i in range(10**6):
        if i in re:
            continue
        Va,j=f(i),i
        L=[]
        while j not in re:
            L.append(j)
            Va,j=f(Va),Va
        k=re[j]
        if i%1000==0:
            print(i)
        for j,b in enumerate(L):
            re[b]=k+len(L)-j
    return len([i for i in re if i<10**6 and re[i]==60])
print(p74())
