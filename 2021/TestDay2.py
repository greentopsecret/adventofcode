import unittest
from unittest.mock import mock_open
from unittest.mock import patch
from day2a import Day2A
from day2b import Day2B


class TestDay2(unittest.TestCase):
    def test_day2a_get_result(self):
        d = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""
        file = 'file/path/mock'
        with patch('builtins.open', mock_open(read_data=d)):
            r = Day2A.get_result(file)

        self.assertEqual(150, r)

    def test_day2b_get_result(self):
        d = """forward 5
down 5
forward 8
up 3
down 8
forward 2
"""
        file = 'file/path/mock'
        with patch('builtins.open', mock_open(read_data=d)):
            r = Day2B.get_result(file)

        self.assertEqual(900, r)
