import click
from functools import wraps
from random import randint
from pizza import Margherita, Pepperoni, Hawaiian

# Создаем словарь для быстрого доступа к классам пицц
pizza_classes = {
    "margherita": Margherita,
    "pepperoni": Pepperoni,
    "hawaiian": Hawaiian
}


def log(arg=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            time = randint(1, 5)  # случайное время от 1 до 5 секунд
            if callable(arg):
                # Если arg - callable (функция без скобок),
                # то это означает, что передан декоратор
                # без аргументов

                print(f"{func.__name__} - {time}с")
                return func(*args, **kwargs)
            else:
                # Иначе, arg считается шаблоном для вывода
                print(arg.format(time))
                return func(*args, **kwargs)

        return wrapper

    if callable(arg):
        return decorator(arg)

    return decorator


@log("👨‍🍳 Приготовили за {}с!")
def bake(pizza) -> None:
    """Готовит пиццу."""
    pass


@log("🚗 Доставили за {}с!")
def delivery(pizza) -> None:
    """Доставляет пиццу."""
    pass


@log("🤗 Забрали за {}с!")
def pickup(pizza) -> None:
    """Самовывоз"""
    pass


@click.group()
def cli():
    pass


@cli.command()
@click.option(
    "--delivery_flag",
    default=False,
    is_flag=True,
    help="Доставить пиццу."
)
@click.argument(
    "pizza_type",
    nargs=1
)
def order(pizza_type: str, delivery_flag: bool):
    """Готовит и доставляет пиццу."""
    pizza_class = pizza_classes.get(pizza_type.lower())
    if not pizza_class:
        raise click.ClickException(f"Пицца типа '{pizza_type}' не найдена.")

    pizza = pizza_class()

    bake(pizza)

    if delivery_flag:
        delivery(pizza)
    else:
        pickup(pizza)


@cli.command()
def menu():
    """Выводит меню доступных пицц."""
    for name, cls in pizza_classes.items():
        pizza = cls()
        print(
            f"{name.capitalize()}{pizza.emoji}: {', '.join(pizza.ingredients)}"
        )


if __name__ == "__main__":
    cli()
