from typing import List, Dict, Union


class Pizza:
    """
    Базовый класс для всех видов пицц.

    Атрибуты:
        size (str): Размер пиццы (L или XL).
        ingredients (List[str]): Список ингредиентов.
        emoji (str): Эмоджи, представляющее пиццу.

    Методы:
        dict: Возвращает словарь с размером и списком ингредиентов для пиццы.
        __eq__: Сравнивает две пиццы по размеру и ингредиентам.
    """

    def __init__(self, size: str, ingredients: List[str], emoji: str):
        """
        Инициализирует пиццу с заданным размером, ингредиентами и эмоджи.

        Параметры:
            size (str): Размер пиццы (должен быть 'L' или 'XL').
            ingredients (List[str]): Список ингредиентов пиццы.
            emoji (str): Эмоджи, представляющее пиццу.

        Вызывает исключение ValueError, если размер пиццы недопустим.
        """
        if size.upper() not in ["L", "XL"]:
            raise ValueError(
                f"Недопустимый размер пиццы: {size}. Допустимые размеры: L, XL"
            )

        self.size = size.upper()
        self.ingredients = ingredients
        self.emoji = emoji

    def dict(self) -> Dict[str, Union[str, List[str]]]:
        """Возвращает словарь с размером и ингредиентами пиццы."""
        return {"Размер": self.size, "Ингредиенты": self.ingredients}

    def __eq__(self, other: object) -> bool:
        """
        Сравнивает эту пиццу с другой пиццей.

        Параметры:
            other (object): Объект, с которым сравнивается текущая пицца.

        Возвращает:
            bool: True, если пиццы равны по размеру и ингредиентам,
             иначе False.

        Вызывает TypeError, если other не является экземпляром класса Pizza.
        """
        if not isinstance(other, Pizza):
            raise TypeError("Такой пиццы у нас нет.")

        return self.size == other.size and \
            self.ingredients == other.ingredients


class Margherita(Pizza):
    """
    Класс для пиццы Маргарита.
    """

    def __init__(self, size: str = "L"):
        """
        Инициализирует пиццу Маргарита с заданным размером.

        Параметры:
            size (str): Размер пиццы (по умолчанию 'L').
        """
        super().__init__(size, ["tomato sauce", "mozzarella", "tomatoes"], "🍅")


class Pepperoni(Pizza):
    """
    Класс для пиццы Пепперони.
    """

    def __init__(self, size: str = "L"):
        """
        Инициализирует пиццу Пепперони с заданным размером.

        Параметры:
            size (str): Размер пиццы (по умолчанию 'L').
        """
        super().__init__(
            size,
            ["tomato sauce", "mozzarella", "pepperoni"],
            "🍕"
        )


class Hawaiian(Pizza):
    """
    Класс для гавайской пиццы.
    """

    def __init__(self, size: str = "L"):
        """
        Инициализирует гавайскую пиццу с заданным размером.

        Параметры:
            size (str): Размер пиццы (по умолчанию 'L').
        """
        super().__init__(
            size, ["tomato sauce", "mozzarella", "chicken", "pineapples"], "🍍"
        )
