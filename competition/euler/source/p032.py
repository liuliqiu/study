##We shall say that an n-digit number is pandigital if it makes use of all the
##digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1
##through 5 pandigital.
##The product 7254 is unusual, as the identity, 39  186 = 7254, containing
##multiplicand, multiplier, and product is 1 through 9 pandigital.
##Find the sum of all products whose multiplicand/multiplier/product identity
##can be written as a 1 through 9 pandigital.
##HINT: Some products can be obtained in more than one way so be sure to only
##include it once in your sum.


def pandigital(string, n=9):
    return len(string) == n and all([chr(i + 48) in string for i in range(1, n + 1)])


def pandig9(string):
    return len(string) == 9 and "0" not in string and len(set(string)) == 9


def fi():
    a = [
        i * j
        for i in range(1, 10)
        for j in range(1234, 5000)
        if pandig9(str(i) + str(j) + str(i * j))
    ]
    b = [
        i * j
        for i in range(12, 98 + 1)
        for j in range(123, 987 + 1)
        if i % 10 and i % 11 and pandig9(str(i) + str(j) + str(i * j))
    ]
    return sum(set(a + b))


print(fi())
