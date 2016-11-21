#!/usr/bin/env python
#-*- coding:utf-8 -*-

from eulertools import primes, is_prime_fast as is_prime

class Node(object):
    def __init__(self, parent, value, digits_sum = None, strong_harshad = False):
        self.value = value
        if digits_sum is None:
            self.digits_sum = value
        else:
            self.digits_sum = digits_sum
        self.children = []
        self.parent = parent
        self.strong_harshad = strong_harshad
        if parent is not None:
            parent.children.append(self)

    @staticmethod
    def new(parent, d):
        value = parent.value * 10 + d
        digits_sum = parent.digits_sum + d
        is_harshad = digits_sum != 0 and value % digits_sum == 0
        if is_harshad:
            strong_harshad = is_prime(value / digits_sum)
            return Node(parent, value, digits_sum, strong_harshad)


class Count(object):
    def __init__(self, n):
        self.x = 0
        self.n = n

    def count(self, v):
        for i in range(1, 10, 2):
            k = v * 10 + i
            if is_prime(v * 10 + i):
                self.x += k

    def deep_first_search(self, node):
        for i in range(10):
            child = Node.new(node, i)
            if child is not None and child.value < self.n / 10:
                if child.strong_harshad:
                    self.count(child.value)
                self.deep_first_search(child)


def HarshadNumbers(n):
    root = Node(None, 0)
    c = Count(n)
    c.deep_first_search(root)
    return c.x


def main():
    n = 10 ** 4
    assert HarshadNumbers(n) == 90619
    print HarshadNumbers(10 ** 14) # 696067597313468

if __name__ == "__main__":
    main()
