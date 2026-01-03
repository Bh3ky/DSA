import pytest
from plus_one import plus_one

@pytest.mark.parametrize(
    "input_digits, expected_output",
    [
        ([1, 2, 3], [1, 2, 4]),
        ([1, 2, 9], [1, 3, 0]),
        ([9, 9, 9], [1, 0, 0, 0]),
        ([0], [1]),
        ([4, 3, 2, 1], [4, 3, 2, 2]),
    ]
)
def test_plus_one(input_digits, expected_output):
    assert plus_one(input_digits) == expected_output