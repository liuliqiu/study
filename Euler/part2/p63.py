##The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit
##number, 134217728=8^9, is a ninth power.
##How many n-digit positive integers exist which are also an nth power?

def fi():
    num=0
    for i in range(1,50):
        if 9**i>10**(i-1):
            for j in range(1,10):
                if j**i>=10**(i-1):
                    num=num+1
                    print(j**i,i)
        else:
            return num
print(fi())
