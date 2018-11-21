##If the numbers 1 to 5 are written out in words: one, two, three, four, five,
##then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
##If all the numbers from 1 to 1000 (one thousand) inclusive were written
##out in words, how many letters would be used?
##NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
##forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
##20 letters. The use of "and" when writing out numbers is in compliance
##with British usage.

s = "One two three four \
Five six seven eight \
Nine ten eleven twelve \
Thirteen fourteen fifteen sixteen \
Seventeen eighteen nineteen"
s2 = "twenty Thirty forty fifty sixty Seventy eighty ninety"


def lsum(l):
    s = 0
    for i in l:
        s = s + i
    return s


def fi(x):
    z = s.split(" ")
    m = [len(i) for i in z]
    z2 = s2.split(" ")
    m2 = [len(i) for i in z2]
    result = [0]
    re2 = [""]
    for i in range(1, x + 1):
        if i < len(m) + 1:
            result.append(m[i - 1])
            re2.append(z[i - 1])
        elif i < 100:
            result.append(m2[i // 10 - 2] + result[i % 10])
            re2.append(z2[i // 10 - 2] + "-" + re2[i % 10])
        elif i == 100:
            result.append(10)
            re2.append("one hundred")
        elif i < 1000:
            if i % 100 == 0:
                result.append(m[i // 100 - 1] + 7)
            else:
                result.append(m[i // 100 - 1] + 10 + result[i % 100])
        elif i == 1000:
            result.append(11)
        else:
            result.append(m[i // 1000 - 1] + 11 + result[i % 1000])
    print(re2)
    return lsum(result)


print(fi(1000))
