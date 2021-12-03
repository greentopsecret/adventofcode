import unittest
from unittest.mock import mock_open
from unittest.mock import patch
from day3a import Day3A as TaskA
from day3b import Day3B as TaskB


class TestDay3(unittest.TestCase):
    def test_a_get_result(self):
        d = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""
        file = 'file/path/mock'
        with patch('builtins.open', mock_open(read_data=d)):
            r = TaskA.get_result(file)

        self.assertEqual(198, r)

    def test_b_get_result(self):
        d = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
"""
        file = 'file/path/mock'
        with patch('builtins.open', mock_open(read_data=d)):
            r = TaskB.get_result(file)

        self.assertEqual(230, r)
