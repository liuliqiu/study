##The rules for writing Roman numerals allow for many ways of writing each number
##(see FAQ: Roman Numerals). However, there is always a "best" way of writing a
##particular number.
##
##For example, the following represent all of the legitimate ways of writing the
##number sixteen:
##
##IIIIIIIIIIIIIIII
##VIIIIIIIIIII
##VVIIIIII
##XIIIIII
##VVVI
##XVI
##
##The last example being considered the most efficient, as it uses the least
##number of numerals.
##
##The 11K text file, roman.txt (right click and 'Save Link/Target As...'), contain
##s one thousand numbers written in valid, but not necessarily minimal, Roman
##numerals; that is, they are arranged in descending units and obey the
##subtractive pair rule (see FAQ for the definitive rules for this problem).
##
##Find the number of characters saved by writing each of these in their minimal
##form.
##
##Note: You can assume that all the Roman numerals in the file contain no more
##than four consecutive identical units.


def p89():
    Tr = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    Mi = [0, 1, 2, 3, 2, 1, 2, 3, 4, 2]

    def num(c):
        return Tr[c]

    def va(s):
        result = 0
        for i in range(len(s)):
            if i == (len(s) - 1) or num(s[i]) >= num(s[i + 1]):
                result = result + num(s[i])
            else:
                result = result - num(s[i])
        return result

    def cOfMin(n):
        ##        print(n)
        re = 0
        i = 0
        while n != 0:
            if i < 3:
                re = re + Mi[n % 10]
            else:
                re = re + n % 10
            n = n // 10
            i = i + 1
        return re

    test = ["MMMMDCLXXII", "CCXCVIII"]
    ##    for i in test:
    ##        print(cOfMin(va(i)))
    m = sum(cOfMin(va(line.strip("\n"))) for line in open("txt/roman.txt"))
    n = sum(len(line.strip("\n")) for line in open("txt/roman.txt"))
    return n - m


##def t2():
##    re=0
##    for line in open('txt/roman.txt'):
##        s=line.strip('\n')
##        s=s.replace("DCCCC", "CM")
##        s=s.replace("LXXXX", "XC")
##        s=s.replace("VIIII" , "IX")
##        s=s.replace("IIII" , "IV")
##        s=s.replace("XXXX", "XL")
##        s=s.replace("CCCC" , "CD")
##        re=re+len(s)
print(p89())
