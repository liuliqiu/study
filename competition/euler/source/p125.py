##The palindromic number 595 is interesting because it can be written as the sum
##of consecutive squares: 6^2 + 7^2 + 8^2 + 9^2 + 10^2 + 11^2 + 12^2.
##
##There are exactly eleven palindromes below one-thousand that can be written as
##consecutive square sums, and the sum of these palindromes is 4164. Note that 1
##= 0^2 + 1^2 has not been included as this problem is concerned with the squares
##of positive integers.
##
##Find the sum of all the numbers less than 108 that are both palindromic and can
##be written as the sum of consecutive squares.
def ispandigital(n):
    s = str(n)
    l = len(s)
    return all(s[i] == s[l - 1 - i] for i in range(l // 2))


def p125():
    L = [1]
    result = set()
    p = 0
    for i in range(1, 10 ** 4 + 1):
        if i % 100 == 0:
            print(i)
        t = (i + 1) // 2
        Sq = (
            2 * L[t - 1] + t * t * (i + 2)
            if i % 2 == 1
            else 2 * L[t - 1] + (t + 1) * (t + 1) * (i + 1)
        )
        if Sq < 10 ** 8 and ispandigital(Sq):
            result.add(Sq)
        for j in range(p, len(L) - 1):
            if Sq - L[j] < 10 ** 8:
                if ispandigital(Sq - L[j]):
                    result.add(Sq - L[j])
                    print(L[j], Sq, i, j, Sq - L[j])
            else:
                p = p + 1
        L.append(Sq)
    print(result)
    return sum(result)


print(p125())
