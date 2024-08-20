
import threading
task = "Дано число в диапазоне от 1_000_000 до 20_000_000. Получите список целочисленных делителей этого числа."

def find_divisors(n, start, end, result):
    """Функция для поиска делителей числа n в диапазоне от start до end."""
    for i in range(start, end):
        if n % i == 0:
            result.append(i)

def get_divisors(n):
    max_divisor = n // 2
    num_threads = 8 
    step = max_divisor // num_threads + 1

    threads = []
    result = []

    # Запуск потоков
    for i in range(1, max_divisor + 1, step):
        start = i
        end = min(i + step, max_divisor + 1)
        thread = threading.Thread(target=find_divisors, args=(n, start, end, result))
        threads.append(thread)
        thread.start()

    # Ожидание завершения всех потоков
    for thread in threads:
        thread.join()

    result.append(n)  # само число также делитель

    return sorted(result)

if __name__ == "__main__":
    n = 220000001
    divisors = get_divisors(n)
    print(f"Делители числа {n}: {divisors}")
