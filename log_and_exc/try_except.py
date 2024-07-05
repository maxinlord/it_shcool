def main():
    try:
        s = input("Введи число: ")
        int(s)
    except ValueError:
        print("Ошибка ввода")
    else:
        print("Все хорошо")
    finally:
        print("Выполняется всегда")


if __name__ == "__main__":
    main()
