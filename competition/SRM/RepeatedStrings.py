"""
Problem Statement
The set of good strings is defined as follows:

    The string "()" is a good string.
    If S is a good string, each string of the form "(SS...S)" is a good string. That is, if you take any good string, concatenate an arbitrary number of its copies, and then surround the result in parentheses, you will produce another good string.
    Nothing else is a good string.
    A subsequence of a string X is any string that can be obtained from X by erasing zero or more of its characters.

    You are given a s. Each character of s is either '(' or ')'.

    Let G be the set of all distinct subsequences of s that are good strings. Note that G contains each good subsequence only once, even if it can be produced in multiple ways. For example, for s="(()())" the set G contains the strings "()", "(())", and "(()())".

    You are also given an k. If there are fewer than k strings in G, return the empty string. Otherwise, return the k-th lexicographically smallest string in G, counting from 1.

    Definition
    Class: RepeatedStrings
    Method: findKth
    Parameters: string, int
    Returns: string
    Method signature: string findKth(string s, int k)
    (be sure your method is public)
    Limits
    Time limit (s): 2.000
    Memory limit (MB): 256
    Constraints
    - s will have between 1 and 150 characters, inclusive.
    - Each character in s must be '(' or ')'.
    - k will be between 1 and 10^9, inclusive.
    Examples
    0)
    "()))((()())"
    3
    Returns: "(())"
    This string has the following distinct good subsequences in sorted order: "((()))", "(()())", "(())", "()". The third one in this list is "(())".
    1)
    "))))))))))))(((((((((("
    1
    Returns: ""
    This string has no good subsequences.
    2)
    "(())(()(()))"
    1
    Returns: "(((())))"
    3)
    "(())))()((())())"
    8
    Returns: "()"
    4)
    "(()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()())"
    64
    Returns: "(((((((((((((()()()())(()()()())))))))))))))"
    5)
    "("
    1000000000
    Returns: ""
"""
