##It is possible to write five as a sum in exactly six different ways:
##4 + 1
##3 + 2
##3 + 1 + 1
##2 + 2 + 1
##2 + 1 + 1 + 1
##1 + 1 + 1 + 1 + 1
##How many different ways can one hundred be written as a sum of at least two
##positive integers?

cached={}
def p76(num):
    def cachnum(n,k):
        return k*(num+1)+n
    def f(n,k):
        '''n表示成小于n个数的和的方法数,每个数都大于或等于k'''
        if n==0:
            return 1
        canum=cachnum(n,k)
        if canum not in cached:
            cached[canum]=sum(f(n-i,i) for i in range(k,n+1))
        return cached[canum]
    return f(num,1)-1
##print(p76(1)==0)
##print(p76(2)==1)
##print(p76(3)==2)
##print(p76(4)==4)
##print(p76(5)==6)
##print(p76(6)==10)
##print(p76(10)==41)
##print(p76(50)==204225)
print(p76(100))
