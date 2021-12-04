import unittest
from unittest.mock import mock_open
from unittest.mock import patch
from dayXXXXyyyy_template import DayXXXXYYYY as TaskYYYY
from day3b import Day3B as TaskB


class TestDay4(unittest.TestCase):
    def test_a_get_result(self):
        d = """"""
        file = 'file/path/mock'
        with patch('builtins.open', mock_open(read_data=d)):
            r = TaskYYYY.task1(file)

        self.assertEqual('ZZZZ', r)

    # def test_b_get_result(self):
    #     d = """"""
    #     file = 'file/path/mock'
    #     with patch('builtins.open', mock_open(read_data=d)):
    #         r = TaskYYYY.get_result(file)
    #
    #     self.assertEqual('ZZZZ', r)
