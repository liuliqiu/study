#!/usr/bin/env python
#-*- coding:utf-8 -*-


def edit_distance(s1, s2):
    if len(s1) == 0:
        return len(s2)
    elif len(s2) == 0:
        return len(s1)

    d1, d2, d3 = edit_distance(s1[:-1], s2), edit_distance(s1, s2[:-1]), edit_distance(s1[:-1], s2[:-1])
    if s1[-1] == s2[-1]:
        return min(d1 + 1, d2 + 1, d3)
    else:
        return 1 + min(d1, d2, d3)


def main():
    print edit_distance("snowy", "sunny")
    print edit_distance("implicit", "complete")


if __name__ == "__main__":
    main()
