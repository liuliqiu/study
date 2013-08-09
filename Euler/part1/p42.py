##The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1);
##so the first ten triangle numbers are:
##1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
##By converting each letter in a word to a number corresponding to its
##alphabetical position and adding these values we form a word value. For example,
##the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is
##a triangle number then we shall call the word a triangle word.
##Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
##containing nearly two-thousand common English words, how many are triangle
##words?

def value(string):
    return sum(ord(c)-64 for c in string)
def readfile():
    f=open("words.txt")
    z=f.read()
    k=z.split(',')
    f.close()
    return list(j.strip("\"") for j in k)
def fi():
    v=[i*(i+1)//2 for i in range(1,100)]
    return len([i for i in readfile() if value(i) in v])
print(fi())
