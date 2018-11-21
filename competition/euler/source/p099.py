##Comparing two numbers written in index form like 2**11 and 3**7 is not difficult
##, as any calculator would confirm that 211 = 2048  37 = 2187.
##
##However, confirming that 632382**518061  519432**525806 would be much more
##difficult, as both numbers contain over three million digits.
##
##Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file
##containing one thousand lines with a base/exponent pair on each line, determine
##which line number has the greatest numerical value.
##
##NOTE: The first two lines in the file represent the numbers in the example given
##above.
import math


def p99():
    re = 0
    a, b, i = 1, 0, 1
    for line in open(r"txt\base_exp.txt"):
        s = line.strip().split(",")
        n = int(s[0])
        e = int(s[1])
        if math.pow(a, b / e) < n:
            re = i
            a, b = n, e
        i = i + 1
    return re


print(p99())
