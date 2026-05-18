# №1 — нет docstring, нет аннотаций типов
def func(num1: float, num2: float) -> float:
    """Принимает два числа и возвращает их произведение."""
    return num1 * num2


# №2 — нет docstring, нет аннотаций, логика приветствия — 'bye' вместо 'hello'
def user(name: str) -> str:
    """Принимает имя пользователя и возвращает приветствие."""
    return 'hello, ' + name


# №3 — нет docstring, нет аннотаций, неинформативные названия func и num
def number_to_string(num: int | float) -> str:
    """Принимает число и возвращает его строковое представление."""
    return str(num)


# №4 — нет docstring, нет аннотаций, переменная sum перекрывает встроенную,
#       второй if/else с continue избыточен — отрицательные числа и так пропускаются
def get_positive_sum(lst: list) -> float:
    """Принимает список чисел и возвращает сумму положительных элементов."""
    total = 0

    for el in lst:
        if el > 0:
            total += el

    return total