##The points P (x1, y1) and Q (x2, y2) are plotted at integer co-ordinates and are
##joined to the origin, O(0,0), to form ΔOPQ.
##
##
##There are exactly fourteen triangles containing a right angle that can be formed
##when each co-ordinate lies between 0 and 2 inclusive; that is,
##0<=x1, y1, x2, y2<=2.
##
##
##Given that 0<=x1, y1, x2, y2<=50, how many right triangles can be formed?
from itertools import product
def isright(x1,y1,x2,y2):
    if (x1==x2 and y1==y2 )or (x1==y1==0) or (x2==y2==0):
##        print("A")
        return False
    elif y1*(x1-x2)==(y1-y2)*x1:
##        print("B")
        return False
    elif x2<x1 or (x2==x1 and y2<=y1):
##        print("C")
        return False
    x3,y3=x1-x2,y1-y2
    return x1*x2+y1*y2==0 or x1*x3+y1*y3==0 or x2*x3+y2*y3==0

def p91(n):
    l=0
    for (x1,y1) in product(range(n+1),repeat=2):
        for (x2,y2) in product(range(n+1),repeat=2):
            if isright(x1,y1,x2,y2):
                l=l+1
    return l
##                print(x1,y1,x2,y2)
print(p91(50))
##print(isright(0,1,1,0))
##print(isright(1,0,1,1))
##print(isright(0,2,1,0))
##print(isright(1,0,1,2))
##print(isright(0,1,2,0))

