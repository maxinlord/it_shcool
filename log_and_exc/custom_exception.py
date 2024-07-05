class MyExceptionGeneral(Exception):
    """Общий класс ошибки"""


class MyException(MyExceptionGeneral):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    def __str__(self) -> str:
        return f"MyException: {super().__str__()}"


def raise_my_exception():
    # raise MyExceptionGeneral("Что-то пошло не так")
    raise MyException("Что-то пошло не так")


def main():
    try:
        raise_my_exception()
    except MyException as e:
        print(e)
    except MyExceptionGeneral as e:
        print(e)


if __name__ == "__main__":
    main()
