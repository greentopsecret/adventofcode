import pytest

from day5 import (task1, task2)

DATA_L = """0,9 -> 5,9
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

DATA_XS_1 = """0,0 -> 4,4
2,0 -> 0,2 
"""

DATA_XS_2 = """4,4 -> 0,0 
0,2 -> 2,0  
"""

DATA_S = """4,4 -> 0,0 
0,2 -> 2,0  
3,0 -> 0,0  
"""

DATA_M = """4,4 -> 0,0 
0,2 -> 2,0  
2,0 -> 0,0  
1,1 -> 0,2  
"""


def test_task1():
    assert 5 == task1(DATA_L)


@pytest.mark.parametrize('data, expected_result', (
        (DATA_XS_1, 1),
        (DATA_XS_2, 1),
        (DATA_S, 3),
        (DATA_M, 4),
        (DATA_L, 12),
))
def test_task2(data, expected_result):
    assert expected_result == task2(data)
