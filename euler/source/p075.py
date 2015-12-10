##It turns out that 12 cm is the smallest length of wire that can be bent to form
##an integer sided right angle triangle in exactly one way, but there are many
##more examples.
##
##12 cm: (3,4,5)
##24 cm: (6,8,10)
##30 cm: (5,12,13)
##36 cm: (9,12,15)
##40 cm: (8,15,17)
##48 cm: (12,16,20)
##
##In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer
##sided right angle triangle, and other lengths allow more than one solution to
##be found; for example, using 120 cm it is possible to form exactly three different
##integer sided right angle triangles.
##
##120 cm: (30,40,50), (20,48,52), (24,45,51)
##
##Given that L is the length of the wire, for how many values of L  1,500,000 can
##exactly one integer sided right angle triangle be formed?
##
##Note: This problem has been changed recently, please check that you are using
##the right parameters.
def HCF(i,j):
    if j==0:
        return i
    else:
        return HCF(j,i%j)
def p75():
    result=[]
    for i in range(2,866):
        for j in range(1,i):
            if i*(i+j)<750000 and HCF(i,j)==1 and (i&1==0 or j&1==0):
                if i*i-j*j>2*i*j:
                    result.append((2*i*j,i*i-j*j,i*i+j*j))
                else:
                    result.append((i*i-j*j,2*i*j,i*i+j*j))
    x=[0 for i in range(1500000+1)]
    for i in result:
        k=sum(i)
        for j in range(k,1500000+1,k):
            if j==120:
                print(k,i)
            x[j]=x[j]+1
    print(x[120])
    return len([i for i in x if i==1])
print(p75())
##print(HCF(2,1))
##print(HCF(20,8))
                    
