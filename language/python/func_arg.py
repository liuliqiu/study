#!/usr/bin/env python
# -*- coding:utf-8 -*-

from utils import get_funcs, get_code
import dis

def f():
    a = 1
    def g(x):
        if x > 1:
            g(x - 1)
        else:
            print a
    g(2)

def main():
    f()
    code_file = get_code(__file__)
    funcs_file = get_funcs(code_file)
    code_f = funcs_file["f"]
    funcs_f = get_funcs(code_f)
    code_g = funcs_f["g"]
    dis.dis(code_file)
    print "f:"
    dis.dis(code_f)
    print "g:"
    dis.dis(code_g)
    print code_file.co_names
    print code_f.co_varnames
    print code_f.co_names

if __name__ == "__main__":
    main()
