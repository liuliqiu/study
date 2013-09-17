#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
    最长非降子序列
    Longest increasing subsequence

"""

def lis(A):
    B = [1] * len(A)
    for i, v in enumerate(A):
        for j, w in enumerate(A[:i]):
            if v > w and B[j] + 1 > B[i]:
                B[i] = B[j] + 1
    print B
    return max(B)


def main():
    A = [3, 2, 4, 8, 5, 9, 6, 1, 7]
    print lis(A)

if __name__ == "__main__":
    main()
