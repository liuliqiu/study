##Working from left-to-right if no digit is exceeded by the digit to its left it
##is called an increasing number; for example, 134468.
##
##Similarly if no digit is exceeded by the digit to its right it is called a
##decreasing number; for example, 66420.
##
##We shall call a positive integer that is neither increasing nor decreasing a
##"bouncy" number; for example, 155349.
##
##Clearly there cannot be any bouncy numbers below one-hundred, but just over
##half of the numbers below one-thousand (525) are bouncy. In fact, the least
##number for which the proportion of bouncy numbers first reaches 50% is 538.
##
##Surprisingly, bouncy numbers become more and more common and by the time we
##reach 21780 the proportion of bouncy numbers is equal to 90%.
##
##Find the least number for which the proportion of bouncy numbers is exactly 99%.

def bouncy(n):
    s=str(n)
    l=len(s)
    if l<3:
        return False
    else:
        return not(all(s[i]<=s[i+1] for i in range(l-1)) or all(s[i]>=s[i+1] for i in range(l-1)))
X=99
def p112():
    b,nb=0,1
    i=2
    while b/nb<X:
        if bouncy(i):
            b=b+1
        else:
            nb=nb+1
##        print(i,b,nb)
        i=i+1
    return i-1
print(p112())
