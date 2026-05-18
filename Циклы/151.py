# Задание №1
tst = [8, 6, -4, 2, -1]

for index, value in enumerate(tst):
    if value < 0:
        break
    print(index, value)


# Задание №2
tst = ['a', 'b', 'c', 'd', 'e']

for index, start in enumerate(tst, start=1):
    print(index, start)

# Задание №3
tst = [1, 2, 3, 4, 5]
result = []

for position, number in enumerate(tst):
    if position % 2 == 0:
         result.append(number ** 2)  # возводим в квадрат
    else:  # нечётная позиция
        result.append(number ** 3)  # возводим в куб
print(result)