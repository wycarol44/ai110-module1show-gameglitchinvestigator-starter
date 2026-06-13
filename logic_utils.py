def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 50
    if difficulty == "Hard":
        return 1, 100
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    import math

    if raw is None:
        return False, None, "Enter a guess."

    if isinstance(raw, bool):
        return False, None, "That is not a number."

    if isinstance(raw, str):
        text = raw.strip()
        if text == "":
            return False, None, "Enter a guess."
        candidate = text
    else:
        candidate = str(raw)

    try:
        value = float(candidate)
    except (TypeError, ValueError):
        return False, None, "That is not a number."

    if not math.isfinite(value):
        return False, None, "That is not a number."

    return True, int(value), None


def check_guess(guess, secret):
    if guess == secret:
        return "Win", "🎉 Correct!"

    try:
        if guess > secret:
            return "Too High", "📈 Go LOWER!"
        else:
            return "Too Low", "📉 Go HIGHER!"
    except TypeError:
        g = str(guess)
        if g == secret:
            return "Win", "🎉 Correct!"
        if g > secret:
            return "Too High", "📈 Go LOWER!"
        return "Too Low", "📉 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        points = max(points, 10)
        return current_score + points

    if outcome in ["Too High", "Too Low"]:
        return max(0, current_score - 5)

    return current_score
