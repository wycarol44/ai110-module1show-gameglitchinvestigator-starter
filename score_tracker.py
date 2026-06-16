import csv
import os
from datetime import datetime
from typing import List, Tuple


SCORES_FILE = "high_scores.csv"


def _ensure_scores_file():
    """Create the scores CSV file if it doesn't exist."""
    if not os.path.exists(SCORES_FILE):
        with open(SCORES_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["score", "difficulty", "timestamp"])


def load_high_scores(difficulty: str = None, limit: int = 5) -> List[Tuple[int, str, str]]:
    """
    Load high scores from file.
    
    Args:
        difficulty: Filter by difficulty (Easy/Normal/Hard), or None for all.
        limit: Number of top scores to return.
    
    Returns:
        List of (score, difficulty, timestamp) tuples, sorted by score descending.
    """
    _ensure_scores_file()
    scores = []
    
    try:
        with open(SCORES_FILE, "r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if difficulty is None or row["difficulty"] == difficulty:
                    scores.append((int(row["score"]), row["difficulty"], row["timestamp"]))
    except (FileNotFoundError, ValueError):
        return []
    
    # Sort by score descending
    scores.sort(key=lambda x: x[0], reverse=True)
    return scores[:limit]


def save_score(score: int, difficulty: str) -> bool:
    """
    Save a score to the high scores file.
    
    Args:
        score: The score to save.
        difficulty: The difficulty level (Easy/Normal/Hard).
    
    Returns:
        True if successfully saved, False otherwise.
    """
    _ensure_scores_file()
    
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(SCORES_FILE, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([score, difficulty, timestamp])
        return True
    except Exception:
        return False


def is_high_score(score: int, difficulty: str, limit: int = 5) -> bool:
    """
    Check if a score qualifies as a high score.
    
    Args:
        score: The score to check.
        difficulty: The difficulty level.
        limit: Number of top scores to compare against.
    
    Returns:
        True if the score is in the top N scores for the difficulty, False otherwise.
    """
    top_scores = load_high_scores(difficulty=difficulty, limit=limit)
    
    # If fewer than limit scores exist, it's a high score
    if len(top_scores) < limit:
        return True
    
    # Otherwise, check if score is higher than the lowest top score
    return score > top_scores[-1][0]
