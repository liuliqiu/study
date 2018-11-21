##We can easily verify that none of the entries in the first seven rows of Pascal's
##triangle are divisible by 7:
##
## 	 	 	 	 	 	 1
## 	 	 	 	 	 1	 	 1
## 	 	 	 	 1	 	 2	 	 1
## 	 	 	 1	 	 3	 	 3	 	 1
## 	 	 1	 	 4	 	 6	 	 4	 	 1
## 	 1	 	 5	 	10	 	10	 	 5	 	 1
##1	 	 6	 	15	 	20	 	15	 	 6	 	 1
##However, if we check the first one hundred rows, we will find that only 2361 of
##the 5050 entries are not divisible by 7.
##
##Find the number of entries which are not divisible by 7 in the first one billion
##(10^9) rows of Pascal's triangle.
import math

BASE = 7


def s(n):
    return n * (n - 1) / 2


def tri(i):
    return s(BASE ** i)


def divisubleNum(n):
    k = int(math.log(n - 1, BASE))
    if k == 0:
        return 0
    tris = [tri(i) for i in range(1, k + 1)]
    tris2 = [0]
    for t in tris:
        tris2.append(s(BASE) * t + s(BASE + 1) * tris2[-1])
    height, left = divmod(n, BASE ** k)
    result = s(height) * tris[k - 1] + s(height + 1) * tris2[k - 1]
    return (
        result
        + height * (s(BASE ** k) - s(BASE ** k - left))
        + (height + 1) * divisubleNum(left)
    )


def p148(n):
    print(s(n + 1) - divisubleNum(n))


p148(10 ** 9)
