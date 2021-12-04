import numpy as np
from numpy import ndarray

"""
--- Day 4: Giant Squid ---
You're already almost 1.5km (almost a mile) below the surface of the ocean, already so deep that you can't see any sunlight. What you can see, however, is a giant squid that has attached itself to the outside of your submarine.

Maybe it wants to play bingo?

Bingo is played on a set of boards each consisting of a 5x5 grid of numbers. Numbers are chosen at random, and the chosen number is marked on all boards on which it appears. (Numbers may not appear on all boards.) If all numbers in any row or any column of a board are marked, that board wins. (Diagonals don't count.)

The submarine has a bingo subsystem to help passengers (currently, you and the giant squid) pass the time. It automatically generates a random order in which to draw numbers and a random set of boards (your puzzle input). For example:

7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
After the first five numbers are drawn (7, 4, 9, 5, and 11), there are no winners, but the boards are marked as follows (shown here adjacent to each other to save space):

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
After the next six numbers are drawn (17, 23, 2, 0, 14, and 21), there are still no winners:

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
Finally, 24 is drawn:

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
At this point, the third board wins because it has at least one complete row or column of marked numbers (in this case, the entire top row is marked: 14 21 17 24 4).

The score of the winning board can now be calculated. Start by finding the sum of all unmarked numbers on that board; in this case, the sum is 188. Then, multiply that sum by the number that was just called when the board won, 24, to get the final score, 188 * 24 = 4512.

To guarantee victory against the giant squid, figure out which board will win first. What will your final score be if you choose that board?

--- Part Two ---
On the other hand, it might be wise to try a different strategy: let the giant squid win.

You aren't sure how many bingo boards a giant squid could play at once, so rather than waste time counting its arms, the safe thing to do is to figure out which board will win last and choose that one. That way, no matter which boards it picks, it will win for sure.

In the above example, the second board is the last to win, which happens after 13 is eventually called and its middle column is completely marked. If you were to keep playing until this point, the second board would have a sum of unmarked numbers equal to 148 for a final score of 148 * 13 = 1924.

Figure out which board will win last. Once it wins, what would its final score be?
"""


class Board:
    bingo: bool
    matrix: np.array

    def __init__(self, matrix: np.array):
        self.bingo = False
        self.matrix = matrix

    def mark_number(self, number: int) -> None:
        w = np.where(self.matrix == number)
        if len(w[0]):
            i = w[0][0]
            j = w[1][0]
            self.matrix[i][j] = 0
            if self.matrix[i].sum() == 0 or self.matrix[:, j].sum() == 0:
                self.bingo = True

    def bingo(self) -> bool:
        return self.bingo

    def score(self, number: int) -> int:
        return self.matrix.sum() * number


class Day4:
    @staticmethod
    def task1(file):
        with open(file, 'r') as f:
            numbers, boards = Day4.convert_to_numbers_and_boards(f.read())

            for j in range(0, len(numbers)):
                number = numbers[j]
                for i in range(0, len(boards)):
                    board = boards[i]
                    board.mark_number(number)
                    if board.bingo:
                        return board.score(number)

    @staticmethod
    def task2(file):
        with open(file, 'r') as f:

            boards: np.array[Board]
            numbers, boards = Day4.convert_to_numbers_and_boards(f.read())

            for j in range(0, len(numbers)):
                number = numbers[j]
                del_indexes = []
                for i in range(0, len(boards)):
                    board = boards[i]
                    board.mark_number(number)
                    if board.bingo:
                        del_indexes.append(i)

                if len(del_indexes) == len(boards):
                    last_board = del_indexes[-1:][0]
                    return boards[last_board].score(number)
                elif del_indexes:
                    if len(boards) > 1:
                        boards = np.delete(boards, del_indexes)
                    else:
                        return board.score(number)

    @staticmethod
    def _build_matrix(raw) -> np.array:
        rows = []
        r = raw.split('\n')
        for j in range(0, len(r)):
            rows.append(list(map(lambda x: int(x), r[j].split())))

        return np.array(rows)

    @staticmethod
    def convert_to_numbers_and_boards(data) -> tuple:
        tmp = data.split('\n\n')

        numbers = [int(x) for x in tmp[:1][0].split(',')]
        raw_boards = tmp[1:]

        boards = []
        for i in range(0, len(raw_boards)):
            matrix = Day4._build_matrix(raw_boards[i])
            boards.append(Board(matrix))

        return numbers, np.array(boards)


if __name__ == '__main__':
    print('Result for the part 1: %s' % Day4.task1('data/day4.txt'))
    print('Result for the part 2: %s' % Day4.task2('data/day4.txt'))