from logic_utils import parse_guess


def test_parse_guess_accepts_integer_input():
    ok, value, error = parse_guess("42")

    assert ok is True
    assert value == 42
    assert error is None


def test_parse_guess_accepts_decimal_input():
    ok, value, error = parse_guess("7.9")

    assert ok is True
    assert value == 7
    assert error is None


def test_parse_guess_rejects_empty_input():
    ok, value, error = parse_guess("")

    assert ok is False
    assert value is None
    assert error == "Enter a guess."


def test_parse_guess_accepts_whitespace_around_input():
    ok, value, error = parse_guess("  42  ")

    assert ok is True
    assert value == 42
    assert error is None


def test_parse_guess_accepts_negative_numbers():
    ok, value, error = parse_guess("-7")

    assert ok is True
    assert value == -7
    assert error is None


def test_parse_guess_accepts_decimal_input_and_truncates_to_int():
    ok, value, error = parse_guess("7.9")

    assert ok is True
    assert value == 7
    assert error is None


def test_parse_guess_rejects_boolean_input():
    ok, value, error = parse_guess(True)

    assert ok is False
    assert value is None
    assert error == "That is not a number."


def test_parse_guess_rejects_non_numeric_input():
    ok, value, error = parse_guess("abc")

    assert ok is False
    assert value is None
    assert error == "That is not a number."


def test_parse_guess_rejects_infinity_input():
    ok, value, error = parse_guess("inf")

    assert ok is False
    assert value is None
    assert error == "That is not a number."
