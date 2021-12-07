import pytest

from task import (task1, task2, triangular_number, calculate_fuel)

DATA = """16,1,2,0,4,2,7,1,2,14
"""


@pytest.mark.parametrize('data, expected_result', (
        (DATA, 37),
))
def test_task1(data, expected_result):
    assert task1(data) == expected_result


@pytest.mark.parametrize('data, expected_result', (
        (DATA, 168),
))
def test_task2(data, expected_result):
    assert task2(data) == expected_result


@pytest.mark.parametrize('n, expected_result', (
        (1, 1),
        (2, 3),
        (5, 15),
))
def test_triangular_number(n: int, expected_result: int):
    assert triangular_number(n) == expected_result


@pytest.mark.parametrize('n1, n2, expected_result', (
        (6, 6, 0),
        (1, 6, 15),
))
def test_calculate_fuel(n1: int, n2: int, expected_result: int):
    assert calculate_fuel(n1, n2) == expected_result
