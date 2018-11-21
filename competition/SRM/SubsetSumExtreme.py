"""
Problem Statement
Bob is playing a game. The game is played with a collection of blocks and a single custom-made die.

Each of the blocks has a positive integer written on it. You are given a block. Each element of block is the number written on one of the blocks.

Each of the faces of the die also has a positive integer written on it. You are given a face. Each element of face is the number written on one of the faces of the die. Whenever Bob rolls the die, one of its faces is selected uniformly at random, and Bob uses the number written on that face.

The game is played in turns. Each turn looks as follows:

    Bob rolls the die to select a random number R.
    Bob selects a subset of blocks such that the sum of their numbers is exactly R.
    Bob removes the selected blocks from the game.
    In step 2, if there is no such subset, the whole game ends. If there are multiple subsets with the required sum, Bob gets to choose which subset is removed. Note that Bob is not allowed to skip a turn: whenever there is at least one valid subset of blocks, he must choose and remove one such subset.

    Bob's score at the end of the game is the sum of the numbers on the remaining blocks. Bob plays the game optimally. More precisely, Bob plays the game in a way that minimizes his expected score at the end of the game. Compute and return the expected value of Bob's score at the end of the game.

    Definition
    Class: SubsetSumExtreme
    Method: getExpectation
    Parameters: vector <int>, vector <int>
    Returns: double
    Method signature: double getExpectation(vector <int> block, vector <int> face)
    (be sure your method is public)
    Limits
    Time limit (s): 2.000
    Memory limit (MB): 256
    Notes
    - Your answer will be accepted if it has absolute or relative error at most 1e-6.
    Constraints
    - block,face will have between 1 and 12 elements, inclusive.
    - Each element of block,face will be between 1 and 1,000, inclusive.
    Examples
    0)
    {1,2,3}
    {6,5}
    Returns: 0.5
    Bob has three blocks with the numbers 1, 2, and 3. Bob has a two-sided die with the numbers 6 and 5 on its faces. (I.e., Bob has a fair coin that has 6 on one side and 5 on the other side.) Let's look at the first turn of the game. In step 1 Bob will randomly choose either 6 or 5, each with probability 1/2. If he chose 6, he will then select all three blocks. If he chose 5, he will select the block with a 2 and the block with a 3. Finally, he will remove the selected blocks from the game. In either case, the game will end in the second turn. Hence, with probability 1/2 Bob's final score will be 1 and with probability 1/2 his final score will be 0. This means that the expected value of his score is (1/2)*1 + (1/2)*0 = 1/2.
    1)
    {1,2,1}
    {1,2}
    Returns: 0.5
    Note that Bob's choices matter. For example, assume that in this game he rolls a 2 in the first turn. Now he has two different options: either he removes the two blocks with 1s, or the single block with a 2. One of these two options is strictly better than the other.
    2)
    {10,11,12}
    {3,4,5,6}
    Returns: 33.0
    The numbers on Bob's blocks are too large. This game will end already in its first turn, and Bob's score is guaranteed to be 33.
    3)
    {1,1,1,1}
    {1}
    Returns: 0.0
    This game will end on turn 5. In each of the previous four turns Bob rolls a 1 and removes one of the four blocks from the game.
    4)
    {3,2,2,3}
    {2,3,2,3,2,3}
    Returns: 2.1875
    5)
    {968,423,592,419,321,253,62,42,12,32,2,4}
    {968,423,592,419,321,253,62,42,12,32,2,4}
    Returns: 1996.9320680897076
    6)
    {12,11,10,9,8,7,6,5,4,3,2,1}
    {12,12,12,12,12,6,6,6,3,3,2,1}
    Returns: 40.03765576104895
"""


class SubsetSumExtreme(object):
    def test(self):
        pass
