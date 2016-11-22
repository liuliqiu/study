from math import log
def f(n):
    i=2
    while (i-1)/(int(log(i,2)))<=n:
        i=i+1
##        print(i-1,log(i,2),(i-1)/(int(log(i,2))))
    return i*(i-1)
print(f(12345))
    
