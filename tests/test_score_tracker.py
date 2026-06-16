import pytest
import os
import csv
from score_tracker import load_high_scores, save_score, is_high_score, SCORES_FILE


@pytest.fixture(autouse=True)
def cleanup_scores_file():
    """Clean up the scores file before and after each test."""
    if os.path.exists(SCORES_FILE):
        os.remove(SCORES_FILE)
    yield
    if os.path.exists(SCORES_FILE):
        os.remove(SCORES_FILE)


def test_save_score_creates_file():
    """Test that save_score creates the scores file if it doesn't exist."""
    assert not os.path.exists(SCORES_FILE)
    result = save_score(100, "Easy")
    assert result is True
    assert os.path.exists(SCORES_FILE)


def test_save_score_multiple():
    """Test saving multiple scores."""
    assert save_score(100, "Easy") is True
    assert save_score(150, "Normal") is True
    assert save_score(200, "Hard") is True
    
    with open(SCORES_FILE, "r") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    assert len(rows) == 3


def test_load_high_scores_empty():
    """Test loading scores when no scores exist."""
    scores = load_high_scores()
    assert scores == []


def test_load_high_scores_sorted_by_score():
    """Test that scores are sorted by score descending."""
    save_score(100, "Easy")
    save_score(150, "Easy")
    save_score(200, "Easy")
    
    scores = load_high_scores(difficulty="Easy")
    assert len(scores) == 3
    assert scores[0][0] == 200
    assert scores[1][0] == 150
    assert scores[2][0] == 100


def test_load_high_scores_by_difficulty():
    """Test filtering scores by difficulty."""
    save_score(100, "Easy")
    save_score(150, "Normal")
    save_score(200, "Hard")
    
    easy_scores = load_high_scores(difficulty="Easy")
    normal_scores = load_high_scores(difficulty="Normal")
    hard_scores = load_high_scores(difficulty="Hard")
    
    assert len(easy_scores) == 1
    assert easy_scores[0][0] == 100
    assert len(normal_scores) == 1
    assert normal_scores[0][0] == 150
    assert len(hard_scores) == 1
    assert hard_scores[0][0] == 200


def test_load_high_scores_limit():
    """Test that limit parameter works correctly."""
    for i in range(10):
        save_score(100 + i * 10, "Easy")
    
    scores = load_high_scores(difficulty="Easy", limit=5)
    assert len(scores) == 5
    assert scores[0][0] == 190  # Highest score


def test_is_high_score_when_empty():
    """Test is_high_score when no scores exist yet."""
    assert is_high_score(100, "Easy") is True
    assert is_high_score(50, "Normal") is True


def test_is_high_score_when_below_limit():
    """Test is_high_score when fewer scores than limit exist."""
    save_score(100, "Easy")
    save_score(150, "Easy")
    
    assert is_high_score(200, "Easy") is True  # Higher than all
    assert is_high_score(75, "Easy") is True  # Still below limit


def test_is_high_score_when_at_limit():
    """Test is_high_score when limit is reached."""
    for i in range(5):
        save_score(100 + i * 10, "Easy")
    
    assert is_high_score(200, "Easy") is True  # Higher than lowest
    assert is_high_score(100, "Easy") is False  # Equal to lowest existing
    assert is_high_score(50, "Easy") is False  # Lower than all


def test_is_high_score_different_difficulties():
    """Test that is_high_score filters by difficulty."""
    save_score(100, "Easy")
    save_score(500, "Normal")
    
    assert is_high_score(99, "Easy") is True  # Below Easy high score
    assert is_high_score(50, "Normal") is True  # No Normal scores yet (below 500)
