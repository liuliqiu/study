"""
Problem Statement
This problem has a non-standard time limit: 5 seconds.
A number x in a list of integers is called lonely if no other number y in the list satisfies |x-y| <= k. That is, each other number differs from a lonely number by more than k. For example, if k=10, the only lonely number in the list {1,30,47,1,20,17} is 47.

A list of integers is called happy if there are no lonely numbers in the list.

A sublist of a list is a contiguous subsequence of the list. For example, {3,4,5} is a sublist of {1,2,3,4,5,6}, but {2,4,6} is not a sublist of {1,2,3,4,5,6}.

You are given a list of integers (in a format that is specified below) and an m. Find and return the smallest k such that the given list has a happy sublist of length at least m.

The list of integers is provided in the following way: You are given an len, a init, and s a, b, c, and d. Use the following pseudocode to generate the list:

    input: len, init, a, b, c, d.

    arr = array of length len
    for i = 0,...,len(init)-1:
       arr[i] = init[i]
       for i = len(init),...,len-1:
          arr[i] = (arr[i-1] * a + b * i + c) % d
          Be careful of overflow, and also note that these indices are 0-based.

          Definition
          Class: FindingFriends
          Method: shortestDistance
          Parameters: int, vector <int>, int, int, int, int, int
          Returns: int
          Method signature: int shortestDistance(int len, vector <int> init, int a, int b, int c, int d, int m)
          (be sure your method is public)
          Limits
          Time limit (s): 5.000
          Memory limit (MB): 256
          Notes
          - The judge solution does not depend on any properties of the random number generator.
          Constraints
          - len will be between 2 and 100,000 inclusive.
          - init will have between 1 and min(len, 2,500) elements, inclusive.
          - Each element of init will be between 0 and 10^9, inclusive.
          - d will be between 1 and 10^9, inclusive.
          - a,b,c will be between 0 and d-1, inclusive.
          - m will be between 2 and len, inclusive.
          Examples
          0)
          6
          {8,1,10,2,9,7}
          12
          34
          56
          78
          2
          Returns: 1
          The generated array is {8,1,10,2,9,7} There is no happy sublist if k=0. The sublist {1,10,2,9} is one of the happy sublists if k=1. This sublist is long enough, so k=1 is our answer.
          1)
          7
          {1}
          1
          0
          0
          12345678
          5
          Returns: 0
          The generated array is {1,1,1,1,1,1,1}.
          2)
          12
          {0}
          1
          0
          1
          6
          3
          Returns: 0
          The generated array is {0,1,2,3,4,5,0,1,2,3,4,5}.
          3)
          10
          {3,4,5}
          23
          34
          35
          46
          4
          Returns: 4
          The generated array is {3,4,5,22,33,44,9,20,31,42}.
          4)
          2
          {0,1000000000}
          0
          0
          0
          1
          2
          Returns: 1000000000
          5)
          5
          {1,2,1000,3,4}
          9
          8
          7
          10
          3
          Returns: 996
          6)
          100000
          {967948965}
          758179342
          788391896
          28648718
          999999937
          3
          Returns: 59543
          Be careful of overflow when generating the array.
"""


class FindingFriends(object):
    def shortestDistance(self, length, init, a, b, c, d, m):
        result = [0] * length
        for x in self.get_data(length, init, a, b, c, d):
            print(x)

    def get_data(self, length, init, a, b, c, d):
        last = init[-1]
        for i in range(length):
            if i < len(init):
                yield init[i]
            else:
                last = (last * a + b * i + c) % d
                yield last

if __name__ == "__main__":
    obj = FindingFriends()
    print(obj.shortestDistance(6, [8,1,10,2,9,7], 12, 34, 56, 78, 2))
