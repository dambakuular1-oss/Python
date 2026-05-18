# Задание №1: список строк
tst = ['1', '2', '3', '4', '5']
for element in tst:
    print(element)

# Задание №2: кортеж чисел
tst = (1, 2, 3, 4, 5)
for element in tst:
    print(element)

# Задание №3: множество символов
tst = {'a', 'b', 'c', 'd', 'e'}
for element in tst:
    print(element)

# Задание №4: строка
tst = 'abcde'
for char in tst:
    print(char)

# Задание №5: число (вывод каждой цифры)
tst = 12345
for digit in str(tst):
    print(digit)

# Задание №6: список чисел + 2 к каждому элементу
tst = [1, 2, 3, 4, 5]
result = [x + 2 for x in tst]
print(result)
