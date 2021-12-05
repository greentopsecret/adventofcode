from day5 import task1, task2

DATA_M = """0,9 -> 5,9
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

DATA_S_1 = """0,0 -> 4,4
2,0 -> 0,2 
"""


# x.x.
# .x..
# x.x.
# ...x

DATA_S_2 = """4,4 -> 0,0 
0,2 -> 2,0  
"""


# x.x.
# .x..
# x.x.
# ...x

DATA_S_3 = """4,4 -> 0,0 
0,2 -> 2,0  
3,0 -> 0,0  
"""


# x.x.
# .x..
# x.x.
# ...x

DATA_S_4 = """4,4 -> 0,0 
0,2 -> 2,0  
2,0 -> 0,0  
1,1 -> 0,2  
"""


# XxX.
# .X..
# X.x.
# ...x

def test_task1():
    assert 5 == task1(DATA_M)


# @pytest.mark.parametrize('data, expected_result', (
#         (DATA_SMALL, 1)
#         (DATA, 12)
# ))
# def test_task2(data, expected_result):
def test_task2():
    assert 1 == task2(DATA_S_1)
    assert 1 == task2(DATA_S_2)
    assert 3 == task2(DATA_S_3)
    assert 4 == task2(DATA_S_4)
    assert 12 == task2(DATA_M)
