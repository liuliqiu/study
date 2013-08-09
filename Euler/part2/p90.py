from itertools import combinations,combinations_with_replacement
def Contains(x,y,a,b):
    return (x in a and y in b ) or (x in b and y in a)
def isallow(a,b):
    if not Contains(0,1,a,b): return False
    if not Contains(0,4,a,b): return False
    if not (Contains(0,9,a,b) or Contains(0,6,a,b)): return False
    if not (Contains(1,6,a,b) or Contains(1,9,a,b)): return False
    if not Contains(2,5,a,b): return False
    if not (Contains(3,6,a,b) or Contains(3,9,a,b)): return False
    if not (Contains(4,9,a,b) or Contains(4,6,a,b)): return False
    if not (Contains(6,4,a,b) or Contains(9,4,a,b)): return False
    if not Contains(8,1,a,b): return False
    return True
def p90():
    return len([i for i in combinations_with_replacement(combinations(range(10),6),2) if isallow(i[0],i[1])])
print(p90())
##print(isa([],[],'0'+str(1*1)))
