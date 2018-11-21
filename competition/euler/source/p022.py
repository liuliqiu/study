##Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
##containing over five-thousand first names, begin by sorting it into
##alphabetical order. Then working out the alphabetical value for each name,
##multiply this value by its alphabetical position in the list to obtain a name
##score.
##For example, when the list is sorted into alphabetical order, COLIN, which
##is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN
##would obtain a score of 938*53 = 49714.
##What is the total of all the name scores in the file?


def score(string):
    up = string.upper()
    z = {}
    for i in range(1, 27):
        z[chr(i + 64)] = i
    result = 0
    for i in up:
        if i in z:
            result = result + z[i]
    return result


def fi():
    f = open("names.txt")
    s = f.readline()
    z = s.split(",")
    z.sort()
    result = 0
    j = 1
    for i in z:
        sco = score(i)
        result = result + j * sco
        j = j + 1
    return result


print(fi())
