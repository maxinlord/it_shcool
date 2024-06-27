"""Написать программу для нахождения среднего арифметического списка чисел. 
Если при вводе списка чисел была допущена ошибка (например, был передан не список, а строка), 
программа должна корректно обработать эту ошибку и выдать соответствующее сообщение.      
Информация об ошибках должна быть записана в лог."""

import logging
import random

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(message)s")
file_handler = logging.FileHandler("logging_task3.log", mode="w", encoding="utf-8")

file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

logger.info(f"Тестируем нахождения среднего арифметического списка чисел {__name__}...")


def average_num_of_list(lst: list):
    try:
        average_value = sum(lst) / len(lst)
        return average_value
    except TypeError:
        logger.error("Ошибка: Неверный тип данных в списке.")
    except ZeroDivisionError:
        logger.error("Ошибка: Попытка деления на ноль.")


def main():

    average_num_of_list([1, 2, 4, 5, 6])
    average_num_of_list([1, 2, 4, 5, "6"])
    average_num_of_list([])
    average_num_of_list(123)


if __name__ == "__main__":
    main()
