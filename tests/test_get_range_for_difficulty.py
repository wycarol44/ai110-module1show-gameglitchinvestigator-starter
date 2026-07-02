import pytest

from logic_utils import get_range_for_difficulty


@pytest.mark.parametrize(
    ("difficulty", "expected"),
    [
        ("Easy", (1, 20)),
        ("Normal", (1, 50)),
        ("Hard", (1, 100)),
        ("Impossible", (1, 100)),
        ("", (1, 100)),
    ],
)
def test_get_range_for_difficulty_returns_expected_ranges(difficulty, expected):
    assert get_range_for_difficulty(difficulty) == expected
