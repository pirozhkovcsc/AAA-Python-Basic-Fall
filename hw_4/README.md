# Домашняя работа &laquo;Тестирование&raquo;

## Описание

Этот проект включает в себя различные тесты для функций, написанные с использованием различных тестовых фреймворков, таких как `doctest`, `unittest` и `pytest`.

## Установка необходимых пакетов

Для запуска тестов необходимо установить следующие пакеты:
```bash
pip install pytest
pip install -U pytest-cov
```

## Задача 1.
### Тестирование функции encode с помощью doctest.
```bash
python -m doctest -o NORMALIZE_WHITESPACE -v morse.py 
```

## Задача 2.
### Параметрический тест функции decode с помощью pytest.
```bash
pytest -v test_morse.py
```

## Задача 3.
### Тестирование функции fit_transform с помощью unittest.
```bash
python -m unittest -v test_ohe_unittest.py
```

## Задача 4.
### Тестирование функции (аналогично Задаче 3) с использованием pytest.
```bash
pytest -v test_ohe_pytest.py
```

## Задача 5.
### Тестирование функции what_is_year_now.
```bash
coverage run test_what_is_year_now.py
coverage report
```