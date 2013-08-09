##By counting carefully it can be seen that a rectangular grid measuring 3 by 2
##contains eighteen rectangles:
##Although there exists no rectangular grid that contains exactly two million
##rectangles, find the area of the grid with the nearest solution.

def f(n):
    return n*(n+1)//2
def p85(n):
    i=1
    diff=n
    temp=(1,1)
    while f(i)*f(i)<2*n:
        j=i
        while f(i)*f(j)<2*n:
          if abs(f(i)*f(j)-n)<diff:
              diff=abs(f(i)*f(j)-n)
              temp=(i,j,i*j)
          j=j+1
        i=i+1
    return temp
print(p85(2000000))
