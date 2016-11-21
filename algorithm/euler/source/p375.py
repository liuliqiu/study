#!/usr/bin/env python
#-*- coding:utf-8 -*-

import operator

from itertools import imap

from eulertools import primes

class PrimeGeneratingIntergers(object):
    def __init__(self, n):
        self.ps = list(primes(n))
        self.ps_set = set(self.ps)
        self.n = n

    def is_prime(self,n):
        return n in self.ps_set

    def deep_iter(self):
        status = Status(self.ps)
        yield 1  # special for 1, 1 + 1 = 2 is prime
        while True:
            number = status.get_number()
            if number <= self.n:
                if not status.from_child():
                    if self.is_generating_number(status):
                        yield number
                    status.child()
                else:
                    if status.has_parent():
                        status.sibling()
                    else:
                        break
            else:
                if status.has_parent():
                    status.parent()
                else:
                    break

    def is_generating_number(self, status):
        return all(imap(self.is_prime, status.all_generate_integers()))

class Status(object):
    def __init__(self, ps):
        self.status = [0]
        self.lst = [[(1, 2)]]
        self.stack = [False]
        self.ps = ps
        self._from_child = False

    def all_generate_integers(self):
        return [a + b for a, b in self.lst[-1]]

    def next_lst(self, lst, p):
        return [(a , b * p) for a, b in lst] + [(a * p, b) for a, b in lst]

    def child(self):
        self.status.append(self.status[-1] + 1)
        self.lst.append(self.next_lst(self.lst[-1], self.ps[self.status[-1]]))
        self._from_child = False

    def sibling(self):
        self.status[-1] += 1
        self.lst[-1] = self.next_lst(self.lst[-2], self.ps[self.status[-1]])
        self._from_child = False

    def from_child(self):
        return self._from_child

    def parent(self):
        self.status.pop()
        self.lst.pop()
        self._from_child = True

    def has_parent(self):
        return len(self.lst) > 1

    def get_number(self):
        return reduce(operator.mul, (self.ps[s] for s in self.status))


def main():
    v = 10 ** 8 # 1739023853137
    test = 10 **6
    print sum(PrimeGeneratingIntergers(test).deep_iter())


if __name__ == "__main__":
    main()
