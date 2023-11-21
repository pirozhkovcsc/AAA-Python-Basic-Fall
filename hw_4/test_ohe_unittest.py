import unittest
from one_hot_encoder import fit_transform


class TestFitTransform(unittest.TestCase):
    """Проводит тесты для функции fit_transform"""

    def test_basic_words(self):
        words = ["AA", "BB", "AA", "BB", "CC", "CC", "CC", "DD"]
        actual = fit_transform(*words)
        excepted = [
            ("AA", [0, 0, 0, 1]),
            ("BB", [0, 0, 1, 0]),
            ("AA", [0, 0, 0, 1]),
            ("BB", [0, 0, 1, 0]),
            ("CC", [0, 1, 0, 0]),
            ("CC", [0, 1, 0, 0]),
            ("CC", [0, 1, 0, 0]),
            ("DD", [1, 0, 0, 0]),
        ]

        self.assertEqual(actual, excepted)

    def test_basic_one_word(self):
        actual = fit_transform(*["ABCDE"])
        excepted = [
            ("ABCDE", [1]),
        ]

        self.assertEqual(actual, excepted)

    def test_no_args_exception(self):
        with self.assertRaises(TypeError):
            fit_transform()

    def test_incorrect_binary_representation(self):
        words = ["HELLO", "WORLD", "!"]
        actual = fit_transform(*words)
        self.assertNotIn(("HELLO", [1, 0, 0]), actual)
        self.assertNotIn(("WORLD", [1, 0, 0]), actual)
        self.assertNotIn(("!", [0, 1, 0]), actual)

    def test_absent_category(self):
        words = ["PYTHON", "2023"]
        actual = fit_transform(*words)
        self.assertNotIn(("SQL", [0, 0, 1]), actual)
        self.assertNotIn(("2024", [1, 0, 0]), actual)
