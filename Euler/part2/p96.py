##Su Doku (Japanese meaning number place) is the name given to a popular puzzle
##concept. Its origin is unclear, but credit must be attributed to Leonhard Euler
##who invented a similar, and much more difficult, puzzle idea called Latin Square
##s. The objective of Su Doku puzzles, however, is to replace the blanks (or zeros
##) in a 9 by 9 grid in such that each row, column, and 3 by 3 box contains each
##of the digits 1 to 9. Below is an example of a typical starting puzzle grid and
##its solution grid.
##
##A well constructed Su Doku puzzle has a unique solution and can be solved by
##logic, although it may be necessary to employ "guess and test" methods in order
##to eliminate options (there is much contested opinion over this). The complexity
##of the search determines the difficulty of the puzzle; the example above is
##considered easy because it can be solved by straight forward direct deduction.
##
##The 6K text file, sudoku.txt (right click and 'Save Link/Target As...'), contain
##s fifty different Su Doku puzzles ranging in difficulty, but all with unique
##solutions (the first puzzle in the file is the example above).
##
##By solving all fifty puzzles find the sum of the 3-digit numbers found in the
##top left corner of each solution grid; for example, 483 is the 3-digit number
##found in the top left corner of the solution grid above.
test='''003020600
900305001
001806400
008102900
700000008
006708200
002609500
800203009
005010300'''
Num=set([str(i) for i in range(1,10)])
def tran(s):
    return [[c for c in line] for line in s.split('\n')]
def deepsearch(SoDoku):
##    print(SoDoku)
    search=True
    for i in range(9):
        for j in range(9):
            if search and SoDoku[i][j]=='0':
                search=False
                L=[]
                for a in range(9):
                    for b in range(9):
                        if a==i or b==j or (a//3==i//3 and b//3==j//3):
                            L.append(SoDoku[a][b])
##                print(L)
                X=Num.difference(L)
##                print(i,j,X)
                for k in X:
                    SoDoku[i][j]=k
                    Result=deepsearch(SoDoku)
                    if Result:
                        return Result
                SoDoku[i][j]='0'
    if search:
        return SoDoku
def p96():
    i=0
    s=""
    result=0
    for line in open('txt/sudoku.txt'):
        if i%10!=0:
            s=s+line
        else:
            s=""
        if i%10==9:
                print(s)
                SoDoku=deepsearch(tran(s))
##                print(SoDoku)
                nums=SoDoku[0][0]+SoDoku[0][1]+SoDoku[0][2]
##                print(nums)
                result=result+int(nums)
        i=i+1
    return result
print(p96())
