##Three distinct points are plotted at random on a Cartesian plane, for which
##-1000  x, y  1000, such that a triangle is formed.
##
##Consider the following two triangles:
##
##A(-340,495), B(-153,-910), C(835,-947)
##
##X(-175,41), Y(-421,-714), Z(574,-645)
##
##It can be verified that triangle ABC contains the origin, whereas triangle XYZ
##does not.
##
##Using triangles.txt (right click and 'Save Link/Target As...'), a 27K text file
##containing the co-ordinates of one thousand "random" triangles, find the number
##of triangles for which the interior contains the origin.
##
##NOTE: The first two examples in the file represent the triangles in the example
##given above.

def f(a,b,c):
    if a[0]!=b[0]:
        X=(a[1]-b[1])/(a[0]-b[0])
        Y=a[1]-a[0]*X
        Z=X*c[0]-c[1]+Y
        return Y*Z>0
    else:
        return (a[0]-0)*(a[0]-c[0])>0
def g(l):
    a,b,c=(l[0],l[1]),(l[2],l[3]),(l[4],l[5])
    return f(a,b,c) and f(b,c,a) and f(c,a,b)
def p102():
    test1=[-340,495,-153,-910,835,-957]
    test2=[-175,41,-421,-714,574,-645]
    f=open('txt/triangles.txt')
    return len([line for line in f if g([int(i) for i in line.split(',')])])
print(p102())
