from logic_utils import update_score


def test_update_score_adds_win_points_and_caps_at_minimum():
    assert update_score(0, "Win", 1) == 80
    assert update_score(0, "Win", 9) == 10


def test_update_score_penalizes_too_high_or_too_low():
    assert update_score(10, "Too High", 1) == 5
    assert update_score(3, "Too Low", 2) == 0


def test_update_score_leaves_unknown_outcome_unchanged():
    assert update_score(25, "Invalid", 3) == 25
