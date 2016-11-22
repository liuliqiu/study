#!/usr/bin/env python
# -*- coding:utf-8 -*-

from types import CodeType

def get_code(file_name):
    return compile(open(file_name).read(), file_name, "exec")

def get_funcs(code):
    return {co.co_name:co for co in code.co_consts if isinstance(co, CodeType)}

