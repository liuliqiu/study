#!/usr/bin/env python
#-*- coding:utf-8 -*-



def matrix_max_line(matrix):
    """
    >>> matrix_max_line(data())
    52852124
    >>> matrix_max_line([-2, 5, 3, 2, 9, -6, 5, 1, 3, 2, 7, 3, -1, 8, -4, 8])
    16
    """
    l = len(matrix)
    n = int(l ** 0.5)
    assert n * n == l
    result = 0
    for ls in h(n, lambda i, j: matrix[i + n * j]):
        result = max(result, max_sum(ls))
    return result

def h(n, f):
    for i in range(n):
        yield list(f(i, j) for j in range(n))
        yield list(f(j, i) for j in range(n))
    for i in range(2 * n - 1):
        yield list(f(i - j, j) for j in range(n) if 0<=j < n and 0<=i-j<n)
        yield list(f(i - j, n - 1 - j) for j in range(n) if 0<= n - 1 -j < n and 0<=i-j<n)

def data():
    ls = []
    for i in range(2000 * 2000):
        if i <= 54:
            x = (100003 - 200003 * (i + 1) + 300007 * (( i + 1 ) ** 3)) % 1000000 - 500000
        else:
            x = (ls[i - 24] + ls[i - 55] ) % 1000000 - 500000
        ls.append(x)
    return ls

def max_sum(ls):
    t, s = [0], 0
    for v in ls:
        s += v
        t.append(s)
    return _max_sub(t)

def _max_sub(s):
    if len(s) == 1:
        return s[0]
    elif len(s) == 2:
        return max(s[0], s[1] - s[0])
    max_v, max_i = s[0], 0
    min_v, min_i = s[0], 0
    for i, v in enumerate(s[1:]):
        if v > max_v:
            max_v, max_i = v, i + 1
        elif v < min_v:
            min_v, min_i = v, i + 1
    
    if max_i > min_i:
        return max_v - min_v
    elif max_i < min_i - 2:
        return max(max_v - min(s[:max_i + 1]), _max_sub(s[max_i + 1:min_i]), max(s[min_i:]) - min_v)
    else:
        return max(max_v - min(s[:max_i + 1]), max(s[min_i:]) - min_v)
