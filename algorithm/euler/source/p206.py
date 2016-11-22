##Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
##where each “_” is a single digit.

def isresult(n):
    s=str(n*n)
    return len(s)==19 and all(s[i*2]==str(i+1) for i in range(9))
def p206():
    for i in range(10000000,14142135+1):
        if i%10000==0:
            print(i)
        if isresult(i*100+30):
            return i*100+30
        elif isresult(i*100+70):
            return i*100+70
print(p206())
