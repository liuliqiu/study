

class GridSort(object):
    def sort(self, n, m, grid):
        """
        >>> GridSort().sort(2, 2, (1, 2, 3, 4))
        'Possible'
        >>> GridSort().sort(2, 2, (3, 4, 1, 2))
        'Possible'
        >>> GridSort().sort(2, 2, (4, 3, 1, 2))
        'Impossible'
        >>> GridSort().sort(1, 10, (4,5,1,2,9,8,3,10,7,6))
        'Possible'
        >>> GridSort().sort(3, 5, (10,6,8,9,7, 5,1,3,4,2, 15,11,13,14,12))
        'Possible'
        >>> GridSort().sort(6, 2, (11,12, 2,1, 9,10, 7,8, 6,5, 3,4 ))
        'Impossible'
        """
        for i in range(n):
            if len(set((grid[i * m + j] - 1) / m for j in range(m))) != 1:
                return "Impossible"
        for j in range(m):
            if len(set((grid[i * m + j] - 1) % m for i in range(n))) != 1:
                return "Impossible"
        return "Possible"


