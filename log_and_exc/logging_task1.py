"""Написать программу на Python для решения квадратного уравнения ax^2 + bx + c = 0. 
Если дискриминант отрицателен, программа должна выдать ошибку и предложить пользователю попробовать еще раз с 
другими коэффициентами. При выполнении скрипта в лог должна записываться информация о успехе или неудаче операции."""


import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(message)s")
file_handler = logging.FileHandler(
    "logging_task1.log", mode="w", encoding="utf-8"
)

file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

logger.info(f"Тестируем решение квадратного уравнения {__name__}...")


def quadratic_equation(a: int, b: int, c: int):
    discriminant = b**2 - 4 * a * c
    if discriminant < 0:
        logger.error(
            f"Дискриминант ({discriminant}) отрицательный для чисел {a=}, {b=}, {c=}"
        )
        return
    x1 = (-b + (discriminant**0.5)) / (2 * a)
    x2 = (-b - (discriminant**0.5)) / (2 * a)

    logger.info(f"Уравнение: {a}x^2 + {b}x + {c} = 0")
    logger.info(f"Дискриминант: {discriminant}")
    logger.info(f"Корни: {x1=}, {x2=}")

    return x1, x2


def main():
    a = int(input("Введите a: "))
    b = int(input("Введите b: "))
    c = int(input("Введите c: "))

    quadratic_equation(a, b, c)

if __name__ == "__main__":
    main()