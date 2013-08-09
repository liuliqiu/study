from itertools import combinations
def P(s):
    if s==tuple():
        return 1
    else:
        return s[0]*P(s[1:])
def f(L):
    result=1
    ex=1
    for i in range(1,len(L)+1):
        K=combinations(L,i)
        S=0
        for x in K:
            S=S+P(x)
##        print(S)
        result=result+S*ex
        ex=ex*2
    print(result)
    return result
##f([2,2,1,1,1,1])
f([3,3,2,2,1,1,1,1,1,1,1,1])
