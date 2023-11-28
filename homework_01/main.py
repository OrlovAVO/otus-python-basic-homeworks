"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return[number **2 for number in numbers]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def power_numbers(*args):
    """
    Функция, которая принимает N целых чисел и возвращает список квадратов этих чисел.

    >>> power_numbers(1, 2, 5, 7)
    [1, 4, 25, 49]
    """
    return [num ** 2 for num in args]


def is_prime(num):
    """
    Функция, которая проверяет, является ли переданное число простым.

    >>> is_prime(2)
    True
    >>> is_prime(4)
    False
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def filter_numbers(numbers, filter_type):
    """
    Функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента).

    >>> filter_numbers([1, 2, 3], ODD)
    [1, 3]
    >>> filter_numbers([2, 1, 3, 5, 4], EVEN)
    [2, 4]
    """
    if filter_type == ODD:
        return list(filter(lambda x: x % 2 != 0, numbers))
    elif filter_type == EVEN:
        return list(filter(lambda x: x % 2 == 0, numbers))
    elif filter_type == PRIME:
        return list(filter(is_prime, numbers))
    else:
        raise ValueError("Invalid filter type. Use ODD, EVEN, or PRIME.")


# Примеры использования
print(power_numbers(1, 2, 5, 7))
print(filter_numbers([1, 2, 3], ODD))
print(filter_numbers([2, 1, 3, 5, 4], EVEN))
