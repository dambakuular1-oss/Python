# №1: Перебор словаря и создание списка [0, 'a', 1, 'b', 2, 'c']
tst = {
    '1': 'a',
    '2': 'b',
    '3': 'c',
    '4': 'd'
}

result = []
for i, key in enumerate(tst.keys()):
    if i < 3:  # берём только первые 3 элемента
        result.append(i)
        result.append(tst[key])
print("№1:", result)

# №2: Заполнение строки чётными числами от 1 до 20
s = ""
for num in range(2, 21, 2):
    s += str(num) + " "
s = s.strip()
print("№2:", s)

# №3: Вывод в столбик нечётных чисел от 100 до 1
print("№3:")
for num in range(99, 0, -2):
    print(num)

# №4: Заполнение списка 10-ю иксами
lst = []
for _ in range(10):
    lst.append('x')
print("№4:", lst)

# №5: Заполнение множества первыми 10-ю буквами английского алфавита
alphabet_set = set()
for i in range(10):
    letter = chr(ord('a') + i)
    alphabet_set.add(letter)
print("№5:", alphabet_set)

# №6: Вывод чисел из кортежа, которые больше 5 и меньше 10
numbers = (3, 7, 12, 8, 5, 9, 15)
print("№6:")
for num in numbers:
    if 5 < num < 10:
        print(num)

# №7: Проверка наличия буквы 'c' в строке
string = "example string with c"
has_c = False
for char in string:
    if char == 'c':
        has_c = True
        break
print("№7: Буква 'c' есть в строке:", has_c)

# №8: Нахождение среднего арифметического элементов списка
numbers = [10, 20, 30, 40, 50]
total = 0
count = 0
for num in numbers:
    total += num
    count += 1
average = total / count if count > 0 else 0
print("№8: Среднее арифметическое:", average)

# №9: Перебор элементов списка до первого положительного числа
numbers = [-5, -3, -1, 2, 4, 6]
print("№9:")
for num in numbers:
    if num > 0:
        print("Первое положительное число:", num)
        break

# №10: Вывод всех элементов словаря в виде кортежа ключ-значение
users = {
    "user1": {"name": "Alice", "surname": "Smith", "age": 25},
    "user2": {"name": "Bob", "surname": "Johnson", "age": 30},
    "user3": {"name": "Charlie", "surname": "Brown", "age": 35},
    "user4": {"name": "Diana", "surname": "Prince", "age": 28},
    "user5": {"name": "Eve", "surname": "Wilson", "age": 22}
}
print("№10:")
for key, value in users.items():
    print((key, value))

# №11: Вывод имён пользователей с большой буквы
print("№11:")
for user in users.values():
    name = user["name"]
    print(name)
