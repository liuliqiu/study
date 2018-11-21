##NOTE: This problem is a more challenging version of Problem 81.
##The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the
##left column and finishing in any cell in the right column, and only moving up,
##down, and right, is indicated in red and bold; the sum is equal to 994.
##
##
##131	673	234	103	18
##201	96	342	965	150
##630	803	746	422	111
##537	699	497	121	956
##805	732	524	37	331
##
##Find the minimal path sum, in matrix.txt (right click and 'Save Link/Target As...'),
##a 31K text file containing a 80 by 80 matrix, from the left column to the right
##column.


def getmatrix():
    ##    string='''131,673,234,103,18
    ##201,96,342,965,150
    ##630,803,746,422,111
    ##537,699,497,121,956
    ##805,732,524,37,331
    ##'''
    string = open(r"txt\matrix.txt").read()
    m = [[int(k) for k in s.split(",")] for s in string.strip().split("\n")]
    return m


def p82(matrix):
    l = len(matrix)
    ##    print(l)
    a = [[j for j in x] for x in matrix]
    for i in range(1, l):
        for j in range(l):
            a[j][i] = a[j][i - 1] + matrix[j][i]
        j = 0
        print(i)
        while j < l:
            ##            print(j,end=' ')
            if j > 0 and a[j][i] > a[j - 1][i] + matrix[j][i]:
                a[j][i] = a[j - 1][i] + matrix[j][i]
            if j < l - 1 and a[j][i] > a[j + 1][i] + matrix[j][i]:
                a[j][i] = a[j + 1][i] + matrix[j][i]
                if j > 0:
                    j = j - 1
                    continue
            j = j + 1
    return min(a[i][l - 1] for i in range(l))


print(p82(getmatrix()))
