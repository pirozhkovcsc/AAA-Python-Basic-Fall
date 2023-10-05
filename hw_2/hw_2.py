import csv
from typing import Dict, List, Union
from decimal import Decimal


def read_file(file_path: str) -> list:
    """
    Читает данные из csv-файла по заданному пути.
    """
    with open(file_path) as f:
        reader = csv.reader(f, delimiter=";")
        next(reader)
        data = list(reader)
    return data


def hierarchy(data: list) -> None:
    """
    Выводит в понятном виде иерархию команд,
    т.е. департамент и все команды, которые входят в него
    """
    # создадим словарь, куда положим Департамент и все команды
    command_hierarchy: Dict[str, set] = {}
    for row in data:
        if row[1] in command_hierarchy:
            command_hierarchy[row[1]].add(row[2])
        else:
            command_hierarchy[row[1]] = {
                row[2],
            }

    # найдем максимальную длину строки из Департаментов
    max_len = max(map(len, command_hierarchy))

    # выведем иерархию команд
    for department, commands in command_hierarchy.items():
        print(f"{department:<{max_len}}", end=" - ")
        print(*commands, sep=", ", end=";\n")


def summary_report(data: list) -> list:
    depart_stats: Dict[str, List[Union[int, Decimal]]] = {}
    # найдем для каждого департамента численность, мин, макс, общую выручку
    for row in data:
        dep = row[1]
        if dep in depart_stats:
            depart_stats[dep][0] += 1
            depart_stats[dep][1] = max(depart_stats[dep][1], Decimal(row[5]))
            depart_stats[dep][2] = min(depart_stats[dep][2], Decimal(row[5]))
            # используем Decimal, так как могут быть float числа
            depart_stats[dep][3] += Decimal(row[5])
        else:
            depart_stats[dep] = [
                1,
                Decimal(row[5]),
                Decimal(row[5]),
                Decimal(row[5]),
            ]

    # преобразуем в удобный вид
    report = [["Департамент", "Численность", "Вилка", "Среднее"]]

    for dep in depart_stats:
        report.append(
            [
                dep,
                str(depart_stats[dep][0]),
                f"{depart_stats[dep][2]} - {depart_stats[dep][1]}",
                str(round(depart_stats[dep][3] / depart_stats[dep][0], 2)),
            ]
        )

    return report


def print_report(report: list) -> None:
    """
    Печатает сводный отчет на экран.
    """
    max_length = max(len(str(elem)) for row in report for elem in row)
    for row in report:
        formatted_row = " | ".join(f"{elem:^{max_length}}" for elem in row)
        print(formatted_row)


def save_report(report: list, file_name="my_file") -> None:
    """
    Сохраняет отчет в виде csv-файла.
    """
    with open(f"{file_name}.csv", "w") as f:
        writer = csv.writer(f)
        for row in report:
            writer.writerow(row)


def menu(counter=0, stop=10):
    """
    Пользователь выбирает пункт меню,
    вводя соответствующее число.
    """
    assert counter < stop, "У вас больше нет попыток!"
    num = input(
        """
        Выберите пункт меню. Для этого введите:
        1) Если хотите увидеть иерархию команд;
        2) Если хотите сводный отчет по департаментам;
        3) Если хотите сохранить сводный отчет в виде csv-файла.
        \n
        """
    )
    if not (num.isdigit()):
        print(
            f"""
              Вы ввели не число!
              Аккуратней, осталось {stop - counter - 1} попыток!
              \n
             """
        )
        counter += 1
        menu(counter, stop)
    elif num not in set("123"):
        print(
            f"""
              Вы ввели число не из данного диапазона!
              Аккуратней, осталось {stop - counter - 1} попыток!
              \n
             """
        )
        counter += 1
        menu(counter, stop)
    else:
        data = read_file(pth)
        if num == "1":
            hierarchy(data)
        else:
            report = summary_report(data)
            if num == "2":
                print_report(report)
            else:
                save_report(report, file_name="Summary")


if __name__ == "__main__":
    pth = "./Corp_Summary.csv"
    menu(counter=0, stop=10)
