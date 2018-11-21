##Let r be the remainder when (a-1)^n + (a+1)^n is divided by a^2.
##
##For example, if a = 7 and n = 3, then r = 42: 6^3 + 8^3 = 728  42 ≡ mod 49.
##And as n varies, so too will r, but for a = 7 it turns out that rmax = 42.
##
##For 3<=a<=1000, find ∑rmax.


def p120():
    """ """

    def rmax(n):
        if n % 2 == 1:
            return n * (n - 1)
        return max((4 * i * n + 2 * n) % (n * n) for i in range(2 * n + 1))

    for i in range(3, 10 + 1):
        print(i, rmax(i))
    return sum(rmax(i) for i in range(3, 1000 + 1))


print(p120())
