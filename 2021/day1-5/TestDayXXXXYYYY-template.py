import unittest
from day5 import task1, task2

INPUT = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""


class TestDay5(unittest.TestCase):
    def test_task1(self):
        self.assertEqual(5, task1(INPUT))

    # def test_task2(self):
    #     self.assertEqual(5, task2(INPUT))
