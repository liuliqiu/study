##Starting in the top left corner of a 22 grid, there are 6 routes
##(without backtracking) to the bottom right corner.
##How many routes are there through a 2020 grid?


def fi(x):
    v = [1]
    i = 2
    while i <= 2 * x:
        v.append(v[-1] * i)
        i = i + 1
    return v[2 * x - 1] // (v[x - 1] * v[x - 1])


print(fi(20))
