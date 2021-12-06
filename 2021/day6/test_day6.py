import pytest

from day6 import (task, get_frequencies)

DATA = """3,4,3,1,2
"""


def test_get_frequencies():
    assert {3: 2, 4: 1, 1: 1, 2: 1} == get_frequencies((3, 4, 3, 1, 2))


@pytest.mark.parametrize('data, days, expected_result', (
        (DATA, 80, 5934),
        (DATA, 5, 10),
))
def test_task(data, days, expected_result):
    assert task(data, days=days) == expected_result
