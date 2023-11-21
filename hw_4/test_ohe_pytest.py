import pytest
from one_hot_encoder import fit_transform


def test_basic_words():
    words = ["A", "B", "A", "B", "C", "C", "C", "D"]
    actual = fit_transform(*words)
    expected = [
        ("A", [0, 0, 0, 1]),
        ("B", [0, 0, 1, 0]),
        ("A", [0, 0, 0, 1]),
        ("B", [0, 0, 1, 0]),
        ("C", [0, 1, 0, 0]),
        ("C", [0, 1, 0, 0]),
        ("C", [0, 1, 0, 0]),
        ("D", [1, 0, 0, 0]),
    ]

    assert actual == expected


def test_basic_one_word():
    actual = fit_transform(*["ABCDE"])
    expected = [
        ("ABCDE", [1]),
    ]

    assert actual == expected


def test_no_args_exception():
    with pytest.raises(TypeError):
        fit_transform()


def test_incorrect_binary_representation():
    words = ["HI", "MAN", "!"]
    actual = fit_transform(*words)

    assert ("HI", [1, 0, 0]) not in actual
    assert ("MAN", [1, 0, 0]) not in actual
    assert ("!", [0, 1, 0]) not in actual


def test_absent_category():
    words = ["METRICS", "2024"]
    actual = fit_transform(*words)

    assert ("AB", [0, 0, 1]) not in actual
    assert ("2025", [1, 0, 0]) not in actual
