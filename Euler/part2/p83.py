##NOTE: This problem is a significantly more challenging version of Problem 81.
##
##In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom
##right, by moving left, right, up, and down, is indicated in bold red and is equal to 2297.
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
##right by moving left, right, up, and down.
##

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
def p83(matrix):
    l=len(matrix)
    a=[[j for j in x]for x in matrix]
    status=[[0 for j in x] for x in matrix]
    begin=(0,0)
    moves=[(1,0),(0,1),(-1,0),(0,-1)]
    movelist=[begin]
    while True:
##        print(begin)
        status[begin[0]][begin[1]]=1
        for move in moves:
            if 0<=begin[0]+move[0]<l and 0<=begin[1]+move[1]<l:
                x,y=begin[0]+move[0],begin[1]+move[1]
                if status[x][y]==0:
                    a[x][y]=a[begin[0]][begin[1]]+matrix[x][y]
                    if x==y==l-1:
                        return a[x][y]
                    status[x][y]=1
                    movelist.append((x,y))
        movelist.remove(begin)
        pos=movelist[0]
        value=a[pos[0]][pos[1]]
        for p in movelist:
            if a[p[0]][p[1]]<value:
                value,pos=a[p[0]][p[1]],p
        begin=pos
    return a
print(p83(getmatrix()))
