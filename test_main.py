"""A module for testing main summator function."""

from typing import Tuple

import pytest

from main import summator

test_data = [((3, 5), 8), ((2, 4), 6), ((-10, 10), 0)]


@pytest.mark.parametrize('numbers, expected', test_data)
def test_summator(numbers: Tuple, expected: int) -> None:
    """Test summator function with test_data.

    Args:
        numbers: numbers to be passed to summator.
        expected: an actual expected summator result.

    Asserts:
        True if summator returns expected answers.
    """
    assert summator(*numbers) == expected
