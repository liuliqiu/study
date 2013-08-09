##The number, 1406357289, is a 0 to 9 pandigital number because it is made up of
##each of the digits 0 to 9 in some order, but it also has a rather interesting
##sub-string divisibility property.
##Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note
##the following:
##d2d3d4=406 is divisible by 2
##d3d4d5=063 is divisible by 3
##d4d5d6=635 is divisible by 5
##d5d6d7=357 is divisible by 7
##d6d7d8=572 is divisible by 11
##d7d8d9=728 is divisible by 13
##d8d9d10=289 is divisible by 17
##Find the sum of all 0 to 9 pandigital numbers with this property.
def norptnum(n):
    return (len(str(n))==len(set(str(n))))
def fi():
    v17=[i for i in range(17,989,17)]
    v13=[i for i in range(13,989,13)]
    v11=[i for i in range(506,605,11)]
    v7=[i for i in range(14,989,7) if (i//10)%5==0]
    s4=[j*10+i%10 for i in v17 for j in v13 if i//10==j%100 and norptnum(j*10+i%10)]
    s5=[j*100+i%100 for i in s4 for j in v11 if j%100==i//100 and norptnum(j*100+i%100)]
    s6=[j*1000+i%1000 for i in s5 for j in v7 if j%100==i//1000 and norptnum(j*1000+i%1000)]
    s7=[j*1000000+i for i in s6 for j in range(10) if norptnum(j*1000000+i) and j%2==0]
    s8=[j*10000000+i for i in s7 for j in range(10) if norptnum(j*10000000+i) and (j+i//100000)%3==0]
    s10=[j*100000000+i for i in s8 for j in range(1,99) if norptnum(j*100000000+i) and len(str(j*100000000+i))==10]
    return sum(s10)
print(fi())
