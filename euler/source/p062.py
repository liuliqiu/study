##The cube, 41063625 (345^3), can be permuted to produce two other cubes: 56623104
##(384^3) and 66430125 (405^3). In fact, 41063625 is the smallest cube which has
##exactly three permutations of its digits which are also cube.
##Find the smallest cube for which exactly five permutations of its digits are
##cube.

def fi():
    digits=10
    n1={}
    n2={}
    for i in range(10000):
        n=i**3
        if n>digits:
            n1={}
            n2={}
            digits=digits*10
        strn=str(sorted(str(n)))
        if strn in n1:
            if n1[strn]>=4:
                return (n2[strn])**3
            else:
                n1[strn]=n1[strn]+1
        else:
            n2[strn]=i
            n1[strn]=1
print(fi())
