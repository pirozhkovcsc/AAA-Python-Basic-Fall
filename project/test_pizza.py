import pytest
from pizza import Margherita, Hawaiian


def test_pizza_equality():
    assert Margherita("L") == Margherita("L"), \
        "Должны быть равны"

    assert Margherita("L") != Margherita("XL"), \
        "Разные размеры! Не должны быть равны."

    assert Margherita() != Hawaiian(), \
        "Разные пиццы! Не должны быть равны."


def test_pizza_sizes():
    with pytest.raises(ValueError):
        Margherita("M")  # размер 'M' не поддерживается

    try:
        Margherita("L")  # размер 'L' поддерживается
        Margherita("XL")  # размер 'XL' поддерживается
    except ValueError:
        pytest.fail("Поймали ошибку, хотя не ожидали ее получить.")


def test_pizza_dict_method():
    pizza = Margherita()
    pizza_dict = pizza.dict()

    assert pizza_dict == {
        "Размер": "L",
        "Ингредиенты": ["tomato sauce", "mozzarella", "tomatoes"],
    }, "Неправильно отображается словарь!"
