#!/usr/bin/env python
#-*- coding:utf-8 -*-

test_str = """7  53 183 439 863
497 383 563  79 973
287  63 343 169 583
627 343 773 959 943
767 473 103 699 303"""

matrix_str = """7  53 183 439 863 497 383 563  79 973 287  63 343 169 583
627 343 773 959 943 767 473 103 699 303 957 703 583 639 913
447 283 463  29  23 487 463 993 119 883 327 493 423 159 743
217 623   3 399 853 407 103 983  89 463 290 516 212 462 350
960 376 682 962 300 780 486 502 912 800 250 346 172 812 350
870 456 192 162 593 473 915  45 989 873 823 965 425 329 803
973 965 905 919 133 673 665 235 509 613 673 815 165 992 326
322 148 972 962 286 255 941 541 265 323 925 281 601  95 973
445 721  11 525 473  65 511 164 138 672  18 428 154 448 848
414 456 310 312 798 104 566 520 302 248 694 976 430 392 198
184 829 373 181 631 101 969 613 840 740 778 458 284 760 390
821 461 843 513  17 901 711 993 293 157 274  94 192 156 574
 34 124   4 878 450 476 712 914 838 669 875 299 823 329 699
 815 559 813 459 522 788 168 586 966 232 308 833 251 631 107
 813 883 451 509 615  77 281 613 459 205 380 274 302  35 805"""


def read_matrix(m_s):
    return [map(int, s.split()) for s in m_s.split("\n")]

from itertools import izip, combinations
import random



def f(m):
    t = tuple(range(len(m)))
    Mem = {}

    def f_helper(A, B):
        if len(A) == 0:
            return 0
        else:
            if (A, B) not in Mem:
                Mem[(A, B)] = max(m[A[0]][b] + f_helper(A[1:], B[:j] + B[j + 1:])
                        for j, b in enumerate(B))
            return Mem[(A, B)]
    return f_helper(t, t)


def get_sum(k, m):
    return sum(l[i] for i, l in izip(k, m))


def g(m):
    list_comb = list(combinations(range(len(m)), 2))
    max_k = random.sample(range(len(m)), len(m))
    max_s = get_sum(max_k, m)
    flag = True
    while flag:
        flag = False
        k = max_k[:]
        for i, j in list_comb:
            k[i], k[j] = k[j], k[i]
            s = get_sum(k, m)
            if s > max_s:
                max_s = s
                max_k = k[:]
                flag = True
            k[i], k[j] = k[j], k[i]

    return max_s


def f_random(m):
    return max(g(m) for i in range(1000))

def main():
    #test_m = read_matrix(test_str)
    #print f(test_m)
    m = read_matrix(matrix_str)
    print f(m)

if __name__ == "__main__":
    main()
