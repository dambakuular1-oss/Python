# №1
first_name = 'Дамба'
last_name = 'Куулар'
course = 2

def print_student(first_name, last_name, course):
    """Выводит информацию о студенте."""
    print(f"{last_name.upper()} {first_name.capitalize()}, курс: {course}")

print_student(first_name, last_name, course)


# №2
def rectangle_area(width: float, height: float) -> float:
    """Принимает ширину и высоту, возвращает площадь прямоугольника."""
    print(width * height)

rectangle_area(4, 5)


# №3
def string_to_tuple(text: str) -> tuple:
    """Принимает строку и возвращает кортеж её символов."""
    return tuple(text)

print(string_to_tuple("привет"))


# №4
def compare(a: float, b: float):
    """Сравнивает два числа и выводит результат."""
    if a > b:
        print(f"{a} больше, чем {b}")
    elif a < b:
        print(f"{b} больше, чем {a}")
    else:
        print(f"{a} и {b} равны")

compare(5, 3)
compare(2, 7)
compare(4, 4)


# №5
def to_string_if_number(value) -> str | None:
    """Если значение является числом, преобразует его в строку."""
    if isinstance(value, (int, float)):
        return str(value)

print(to_string_if_number(42))
print(to_string_if_number("текст"))


# №6
def even_numbers(limit: int) -> list:
    """Возвращает список чётных чисел от 1 до заданного числа."""
    return [n for n in range(1, limit + 1) if n % 2 == 0]

print(even_numbers(10))


# №7
users = {'Иван': 25, 'Мария': 30, 'Алексей': 22}

def print_users(users: dict):
    """Выводит пары ключ-значение словаря в виде кортежей."""
    for pair in users.items():
        print(pair)

print_users(users)


# №8
def day_of_week(num: int) -> str:
    """Принимает номер дня (1-7) и возвращает название дня недели."""
    days = {
        1: 'Понедельник',
        2: 'Вторник',
        3: 'Среда',
        4: 'Четверг',
        5: 'Пятница',
        6: 'Суббота',
        7: 'Воскресенье'
    }
    return days.get(num, 'Неверный номер дня')

print(day_of_week(1))
print(day_of_week(5))
print(day_of_week(8))