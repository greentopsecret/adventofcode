import unittest
from unittest.mock import mock_open
from unittest.mock import patch


def get_cnt(path):
    cnt = 0

    with open(path, 'r') as f:
        prev_sum = None
        current_sum = 0
        bag = []
        while True:
            line = f.readline().strip()
            if not line.isnumeric():
                break

            number = int(line)

            bag.append(number)
            current_sum += number

            if len(bag) == 3:
                if prev_sum and prev_sum < current_sum:
                    cnt += 1
                prev_sum = current_sum
                current_sum -= bag.pop(0)

        f.close()

    return cnt


class Test12(unittest.TestCase):
    def test_get_cnt(self):
        d = """1
    2
    3
    5
    2
    7
    1
    3"""
        path = 'file/path/mock'
        with patch('builtins.open', mock_open(read_data=d)):
            r = get_cnt(path)

        self.assertEqual(3, r)


if __name__ == '__main__':
    print(get_cnt('data/day1b.txt'))
