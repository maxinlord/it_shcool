"""Написать программу для генерации случайных чисел в заданном диапазоне. 
Если пользователь ввел недопустимые границы диапазона (например, меньше нуля), 
программа должна вывести ошибку и попросить ввести диапазон заново. 
Информация об ошибках должна быть записана в лог."""

import logging
import random

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(message)s")
file_handler = logging.FileHandler("logging_task2.log", mode="w", encoding="utf-8")

file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

logger.info(f"Тестируем генерации случайных чисел в заданном диапазоне {__name__}...")

RANGE_RANDOM_MIN = 10
RANGE_RANDOM_MAX = 100


def generate_random_number(a: int, b: int):
    if a < RANGE_RANDOM_MIN or a > RANGE_RANDOM_MAX:
        logger.error(f"Недопустимый диапазон: {a=}")
        return None
    if b < RANGE_RANDOM_MIN or b > RANGE_RANDOM_MAX:
        logger.error(f"Недопустимый диапазон: {b=}")
        return None

    num = random.randint(a, b)
    logger.info(f"Случайное число: {num}")
    return num


def main():
    a = int(input("Введите a: "))
    b = int(input("Введите b: "))

    generate_random_number(a, b)


if __name__ == "__main__":
    main()
