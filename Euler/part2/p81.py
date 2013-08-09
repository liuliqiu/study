##In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom
##right, by only moving to the right and down, is indicated in bold red and is
##equal to 2427.
##
##
##131	673	234	103	18
##201	96	342	965	150
##630	803	746	422	111
##537	699	497	121	956
##805	732	524	37	331
##
##Find the minimal path sum, in matrix.txt (right click and 'Save Link/Target As...'),
##a 31K text file containing a 80 by 80 matrix, from the top left to the bottom
##right by only moving right and down.

def getmatrix():
##    string='''131,673,234,103,18
##201,96,342,965,150
##630,803,746,422,111
##537,699,497,121,956
##805,732,524,37,331
##'''
    string=open(r'txt\matrix.txt').read()
    m=[[int(k) for k in s.split(',')] for s in string.strip().split('\n')]
    return m
def p81(matrix):
    l=len(matrix)
    s=[]
    for i in range(0,l):
        s.append([])
        for j in range(0,l):
            s[i].append(0)
    for k in range(0,2*l-1):
        for j in range(0,k+1):
            if j<l and k-j<l:
                i=k-j
                a=0
                if j>0:
                    a=s[j-1][i]
                if i>0 and (s[j][i-1]<a or a==0):
                    a=s[j][i-1]
                s[j][i]=a
                s[j][i]=s[j][i]+matrix[j][i]
##    for i in range(0,l):
##        for j in range(0,l):
##            print(s[j][i],end=' ')
##        print()
    return s[l-1][l-1]
print(p81(getmatrix()))
##print(getmatrix())
