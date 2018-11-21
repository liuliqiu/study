class TestTaking(object):
    def findMax(self, questions, guessed, actual):
        """
        >>> TestTaking().findMax(3, 2, 1)
        2
        >>> TestTaking().findMax(5, 5, 0)
        0
        >>> TestTaking().findMax(10, 8, 8)
        10
        >>> TestTaking().findMax(7, 0, 2)
        5
        """
        return min(guessed, actual) + questions - max(guessed, actual)
