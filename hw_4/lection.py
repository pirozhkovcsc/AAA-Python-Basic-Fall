import unittest


# Класс для примера, его будем нагружать тестами
class Pokemon:
    def __init__(self, name: str, poketype: str):
        self.name = name
        self.poketype = poketype

    def __str__(self):
        """
        Модифицированная функция str

        >>> str(Pokemon(name='Bulbasaur', poketype='grass'))
        'Bulbasaur/grass'

        >>> str(Pokemon(name='Pikachu', poketype='electric\\r\\npower'))
        'Pikachu/electric\\r\\npower'

        >>> str(Pokemon(name='Squirtle', poketype='water' * 30))
        'Squirtle/waterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwater'
        """

        return f"{self.name}/{self.poketype}"


# Пишем тесты для базовой проверки с помощью assert
def test_str():
    """Проводит тесты для метода __str__ вторым способом"""

    res = Pokemon(name="Bulbasaur", poketype="grass")

    assert (
        str(res) == "Bulbasaur/grass"
    ), f"expected: Bulbasaur/grass, got: {res}"

    res = Pokemon(name="Pikachu", poketype="electric\r\npower")

    assert (
        str(res) == "Pikachu/electric\r\npower"
    ), f'expected: "Pikachu/electric\r\npower", got: {res}'

    res = Pokemon(name="Squirtle", poketype="water" * 30)

    assert (
        str(res) == f'Squirtle/{"water" * 30}'
    ), f"expected: Squirtle/...many times word water (30), got: {res}"


# Пишем тесты для unittest
class TestPokemonStr(unittest.TestCase):
    """
    Проводит тесты для метода __str__ третьим способом
    с помощью unittest
    """

    def test_base_words(self):
        actual = str(Pokemon(name="Bulbasaur", poketype="grass"))
        excepted = "Bulbasaur/grass"
        self.assertEqual(actual, excepted)

    def test_special_symbols(self):
        actual = str(Pokemon(name="Pikachu", poketype="electric\r\npower"))
        excepted = "Pikachu/electric\r\npower"
        self.assertEqual(actual, excepted)

    def test_long_word(self):
        actual = str(Pokemon(name="Squirtle", poketype="water" * 30))
        excepted = f'Squirtle/{"water" * 30}'
        self.assertEqual(actual, excepted)


# Пишем тесты для pytest
def test_base_words_pytest():
    res = Pokemon(name="Bulbasaur", poketype="grass")
    assert (
        str(res) == "Bulbasaur/grass"
    ), f"expected: Bulbasaur/grass, got: {res}"


def test_special_pytest():
    res = str(Pokemon(name="Pikachu", poketype="electric\r\npower"))
    assert (
        str(res) == "Pikachu/electric\r\npower"
    ), f'expected: "Pikachu/electric\r\npower", got: {res}'


def test_long_word_pytest():
    res = str(Pokemon(name="Squirtle", poketype="water" * 30))
    assert (
        str(res) == f'Squirtle/{"water" * 30}'
    ), f"expected: Squirtle/...many times word water (30), got: {res}"


if __name__ == "__main__":
    test_str()
