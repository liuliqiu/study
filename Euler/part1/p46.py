##It was proposed by Christian Goldbach that every odd composite number can be
##written as the sum of a prime and twice a square.
##9 = 7 + 2*1^2
##15 = 7 + 2*2^2
##21 = 3 + 2*3^2
##25 = 7 + 2*3^2
##27 = 19 + 2*2^2
##33 = 31 + 2*1^2
##It turns out that the conjecture was false.
##What is the smallest odd composite that cannot be written as the sum of a
##prime and twice a square?

def findprimes(n):
    v=[2]
    for i in range(3,n,2):
        for j in v:
            if j*j>i:
                v.append(i)
                break
            if i%j==0:
                break
    return v
def fi(n):
    r=findprimes(n)
    for i in range(9,n,2):
        if i not in r:
            for j in range(1,n):
                if 2*j*j>i:
                    return i
                    break
                if (i-2*j*j) in r:
                    break
print(fi(10000))
