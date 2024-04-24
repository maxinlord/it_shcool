"""Выполнил: Гордеев Максим Стальевич"""


def _parse_input(input_str: str) -> tuple[list[int], str]:
    # Разделяем строку и преобразуем в список чисел
    numbers = [int(num) for num in input_str.split() if num.isdigit()]

    # Проверяем количество чисел
    if len(numbers) != 2:
        raise ValueError("Необходимо ввести два числа")

    # Проверяем диапазон чисел
    for num in numbers:
        if not 1 <= num <= 10:
            raise ValueError("Числа должны быть в диапазоне от 1 до 10")

    # Извлекаем операцию
    operation = input_str.split()[1]
    if operation not in "+-*/":
        raise ValueError("Неизвестная операция")

    return numbers, operation


def main(input_str: str) -> str:
    # Разделяем строку на числа и операцию
    numbers, operation = _parse_input(input_str)

    # Выполняем операцию
    match operation:
        case "+":
            result = numbers[0] + numbers[1]
        case "-":
            result = numbers[0] - numbers[1]
        case "*":
            result = numbers[0] * numbers[1]
        case "/":
            result = numbers[0] // numbers[1]

    # Возвращаем строку с результатом
    return f"{input_str} = {result}"


if __name__ == "__main__":
    while True:
        # Запрашиваем у пользователя строку с выражением
        input_str = input("Введите выражение (число1 операция число2): ")
        result_str = main(input_str)
        print(result_str)
