import pytest

from day6 import (task, task2, get_frequencies)

DATA = """3,4,3,1,2
"""


# 3,4,3,1,2
# 2,3,2,0,1                         0: 1, 1: 1, 2: 2, 3: 1
# 1,2,1,6,0,8                       8: 1, 6: 1, 0: 1, 1: 2, 2: 1
# 0,1,0,5,6,7,8                     8: 1, 6: 1, 0: 2, 1: 1, 5: 1
# 6,0,6,4,5,6,7,8,8                 8: 2, 6: 2, 0: 1, 4: 1, 5: 1
# 5,6,5,3,4,5,6,7,7,8


def test_get_frequencies():
    assert {3: 2, 4: 1, 1: 1, 2: 1} == get_frequencies((3, 4, 3, 1, 2))


# @TODO: parametrized
def test_task1():
    assert task(DATA, days=80) == 5934
    assert task(DATA, days=5) == 10

# @pytest.mark.parametrize('data, expected_result', (
#         (DATA_XS_1, 1),
#         (DATA_XS_2, 1),
#         (DATA_S, 3),
#         (DATA_M, 4),
#         (DATA_L, 12),
# ))
# def test_task2(data, expected_result):
#     assert expected_result == task(data, diagonal=True)
