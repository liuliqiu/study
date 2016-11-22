cached={}
def cachnum(R,C):
    return  str(C)+'-'+str(R)
def M(C,R):
    cach=cachnum(R,C)
    if C>R:
        return R+1
    elif cach in cached:
            return cached[cach]
    else:
        X=M(C,R-1)
        t=X-C+1
        p,q=t//(C-2),t%(C-2)
        if q==0:
            cached[cach]=C+p*C
        else:
            cached[cach]=C+p*C+q+2
        return cached[cach]
def p327():
    return sum(M(C,30) for C in range(3,40+1))
print(p327())
