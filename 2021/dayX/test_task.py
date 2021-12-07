import pytest

from task import (task1, task2)

DATA = """
"""


@pytest.mark.parametrize('data, expected_result', (
        (DATA, -1),
))
def test_task(data, expected_result):
    assert task1(data) == expected_result
