"""
Problem Statement
Charlie has a grid of n rows by m columns. The rows are numbered 0 through n-1 from top to bottom. The columns are numbered 0 through m-1 from left to right.

Each cell of the grid contains a positive integer. The integers in Charlie's grid are a permutation of the numbers 1 through n*m. (I.e., each of these numbers occurs in the grid exactly once.)

Given a grid, its value list is a sequence constructed by listing all values in the grid in row major order. That is, we first list the values in row 0 from left to right, then the values in row 1 from left to right, and so on.

You are given the s n and m: the dimensions of Charlie's grid. You are also given a grid: the value list for Charlie's grid. (Formally, grid[i*m+j] is the value stored in row i, column j of the grid.)

In Charlie's eyes, the most beautiful of all grids is the sorted grid: the grid whose value list is the ordered ordered sequence {1,2,3,...,n*m}.

Given a grid, its similarity string is a string of zeroes and ones that describes the similarity between that particular grid and the sorted grid. More precisely:

    The similarity string is a string of length n*m.
    For each i, character i of the similarity string is '1' if both grids have the same i-th element in their value lists, and it is '0' if those values differ. (All indices in the previous sentence are 0-based.)
    For example, suppose n=2 and m=3. The sorted grid has the value list {1,2,3,4,5,6}, and its similarity string is "111111". Another possible grid with these dimensions has the value list {1,5,2,4,3,6}. The similarity string for this grid is "100101".

    Charlie can modify his grid in two ways: He may swap any two rows, and he may swap any two columns. He wants to use these operations to obtain a grid with the lexicographically largest possible similarity string. Find and return that string.

    Definition
    Class: GridSortMax
    Method: findMax
    Parameters: int, int, vector <int>
    Returns: string
    Method signature: string findMax(int n, int m, vector <int> grid)
    (be sure your method is public)
    Limits
    Time limit (s): 2.000
    Memory limit (MB): 256
    Constraints
    - n,m will be between 1 and 50, inclusive.
    - grid will be a permutation of [1,...,n*m]
    Examples
    0)
    2
    2
    { 1,2, 3,4 }
    Returns: "1111"
    Charlie's grid is the sorted grid. Its similarity string is therefore "1111". Charlie should make no changes to the grid, as this is already the lexicographically largest of all possible strings.
    1)
    2
    2
    { 2,1, 3,4 }
    Returns: "1100"
    The similarity string for Charlie's current grid is "0011", as the values 3 and 4 are in the same places as in the sorted grid. Charlie should swap the two columns. That swap will produce a grid with the similarity string "1100": now the values 1 and 2 are in their correct places but the values 3 and 4 aren't.
    2)
    2
    2
    { 4,2, 3,1 }
    Returns: "1001"
    3)
    1
    10
    {10,6,2,3,5,7,1,9,4,8}
    Returns: "1111111111"
    4)
    3
    5
    { 5,2,10,7,9, 3,4,14,11,1, 15,12,6,8,13 }
    Returns: "101100100100000"
    5)
    6
    2
    { 3,9, 5,1, 10,6, 2,7, 8,11, 12,4 }
    Returns: "100000101010"
"""

class GridSortMax(object):
    def findMax(self, n, m, s):
        rev = {}
        for i, v in enumerate(s):
            rev[v] = i
        unsolved_columns = set(range(m))

        for row_index in range(n):
            min_unsolved_in_row = row_index * n + min(unsolved_columns) + 1
            solved_row_index = rev[min_unsolved_in_row] / m

            if solved_row_index != row_index:
                for j in range(m):
                    index_1, index_2 = row_index * m + j, solved_row_index * m + j
                    s[index_1], s[index_2] = s[index_2], s[index_1]
                    rev[s[index_1]] = index_1
                    rev[s[index_2]] = index_2

            temp_set = set()
            print(s)
            for j in unsolved_columns:
                value = s[row_index * m + j]
                if (value - 1) / m == row_index:
                    new_j = (value - 1) % m
                    if new_j != j:
                        print(j, new_j)
                        for i in range(n):
                            index_1, index_2 = i * m + j, i * m + new_j
                            s[index_1], s[index_2] = s[index_2], s[index_1]
                            rev[s[index_1]] = index_1
                            rev[s[index_2]] = index_2
                    print(s)
                temp_set.add(j)
            print(temp_set, unsolved_columns)
            for j in temp_set:
                unsolved_columns.remove(j)

            print(s)
            if len(unsolved_columns) <= 1:
                unsolved_rows = set(range(row_index + 1, n))
                for i in range(row_index + 1, n):
                    for j in range(m):
                        value = i * m + j + 1
                        new_i = rev[value] / m
                        if(rev[value] % m == j and new_i in unsolved_rows):
                            if new_i != i:
                                for _j in range(m):
                                    index_1, index_2 = i * m + _j, new_i * m + _j
                                    s[index_1], s[index_2] = s[index_2], s[index_1]
                                    rev[s[index_1]] = index_1
                                    rev[s[index_2]] = index_2
                            unsolved_rows.remove(i)
                            break
                    print(s)
                break

        print(s)
        return "".join("1" if (i==v) else "0" for i, v in enumerate(s, 1))


if __name__ == "__main__":
    obj = GridSortMax()
    print(obj.findMax(2, 2, [1, 2, 3, 4]))
    print(obj.findMax(2, 2, [2, 1, 3, 4]))
    assert obj.findMax(3, 5, [ 5,2,10,7,9, 3,4,14,11,1, 15,12,6,8,13]) == "101100100100000"
    assert obj.findMax(6, 2, [3,9, 5,1, 10,6, 2,7, 8,11, 12,4]) == "100000101010"
    print(obj.findMax(1, 10, [10,6,2,3,5,7,1,9,4,8]))

