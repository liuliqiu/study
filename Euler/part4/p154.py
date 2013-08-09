#!/usr/bin/env python
#-*- coding:utf-8 -*-

from math import factorial, log

def g(end, base):
    return Triangle(end, base).value()

class Triangle:
    def __init__(self, n, base):
        self.n = n
        self.base = base
        a = int(log(n, base))
        left = n - base ** a
        x = base ** (a - 1) + left
        self.params = (a, left, x, base ** a)

    def get(self, line, index):
        print index, line, self.n
        assert 0 <= index<= line < self.n
        if self.n <= self.base:
            return 0
        else:
            a, left, x, base_n = self.params
            if line < left: #顶部小三角
                return Triangle(left, self.base).get(line, index)
            elif line >= base_n and index <= line - base_n:#左侧小三角
                return Triangle(left, self.base).get(line - base_n, index)
            elif line >= base_n and index >= base_n:#右侧小三角
                return Triangle(left, self.base).get(line - base_n, index - base_n)

    def value(self):
        return [[self.get(line, index) for index in range(line + 1)] for line in range(self.n)]

def join(a, b, c, n, left, base):
    result = []
    for line in a:
        result.append(line.copy())
    for line in b[len(a)]:
        result.append(line.copy())
    return result


def compare(a, b):
    if len(a) != len(b):
        return False
    for x, y in zip(a, b):
        if len(x) != len(y):
            return False
        for i, j in zip(x, y):
            if i != j:
                return False
    return True


def _f(n, base = 5):
    count = 0
    while n % base == 0:
        n /= base
        count += 1
    return count

def main():
    base = 5
    for i in range(1, 7):
        result = []
        for line in range(i):
            line_lst = []
            for n in range(1, line + 2):
                value = _f(factorial(i - 1) / (factorial(line) * factorial(i - 1 - line)) * factorial(line) / (factorial(n - 1) * factorial(line + 1 - n)), base)
                line_lst.append(value)
            result.append(line_lst)
        assert compare(result, g(i, base)), "Error: {0}".format(i)

if __name__ == "__main__":
    main()
