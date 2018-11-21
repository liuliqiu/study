##You are given the following information, but you may prefer to do some research
##for yourself.
##1 Jan 1900 was a Monday.
##Thirty days has September,
##April, June and November.
##All the rest have thirty-one,
##Saving February alone,
##Which has twenty-eight, rain or shine.
##And on leap years, twenty-nine.
##A leap year occurs on any year evenly divisible by 4, but not on a century
##unless it is divisible by 400.
##How many Sundays fell on the first of the month during the twentieth century
##(1 Jan 1901 to 31 Dec 2000)?


def leapYear(y):
    if y % 4 != 0:
        return False
    elif y % 100 != 0:
        return True
    elif y % 400 == 0:
        return True
    else:
        return False


def fi():
    re = [1]
    dayofmonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    year = 1900
    month = 2
    while year < 2001:
        day = dayofmonth[month - 2]
        if month - 1 == 2 and leapYear(year):
            day = day + 1
        re.append((re[-1] + day) % 7)
        if month == 12:
            month = 1
            year = year + 1
        else:
            month = month + 1
    print(re)
    n = 0
    for i in range(len(re)):
        if i >= 12 and re[i] == 0:
            n = n + 1
    return n


print(fi())
