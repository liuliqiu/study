##The sequence of triangle numbers is generated by adding the natural numbers.
##So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
##The first ten terms would be:
##1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
##Let us list the factors of the first seven triangle numbers:
## 1: 1
## 3: 1,3
## 6: 1,2,3,6
##10: 1,2,5,10
##15: 1,3,5,15
##21: 1,3,7,21
##28: 1,2,4,7,14,28
##We can see that 28 is the first triangle number to have over five divisors.
##What is the value of the first triangle number to have over five hundred
##divisors?

def numberofdivisors(s):
    if s<=1:
        return 1
    n=2
    i=2
    while i*i<=s:
        if i*i==s:
            return n+1
        if s%i==0:
            n=n+2
        i=i+1
    return n

def fi(x):
    i=1
    while True:
        if i%2==0:
            tmp = numberofdivisors(i / 2) * numberofdivisors(i + 1)
        else:
            tmp = numberofdivisors(i) * numberofdivisors((i + 1) / 2)
        if tmp > x:
            return (i * i + i) / 2
        i += 1
print(fi(500))