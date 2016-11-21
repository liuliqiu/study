#!/usr/bin/env python
# -*- coding:utf-8 -*-

#from __future__ import print_function
import dis


if_control_py = """
a = 1
if a > 10:
    print "a > 10"
elif a <= -2:
    print "a <= -2"
else:
    print "Unkown a"
"""

for_control_py = """
for i in [1, 2]:
    print i
"""
while_control_py = """
i = 0
while i < 10:
    i += 1
    if a > 5:
        continue
    if a == 20:
        break
    print a
"""
yield_py = """
def f(x):
    if x > 3:
        yield x

f(2)
"""

func_py = """
def f(x):
    return x + 1
f(3)
"""

def show_code(code):
    print("\ncode - ", code.co_name, ":\n")
    dis.disco(code)
    for const in code.co_consts:
        if type(const) is type(code):
            show_code(const)

def main():
    for py_code in [if_control_py, for_control_py, while_control_py, func_py, yield_py]:
        print("=" * 100)
        print(py_code)
        code = compile(py_code, "<stdin>", "exec")
        show_code(code)


if __name__ == "__main__":
    main()
