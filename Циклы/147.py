# Задание №1: сумма квадратов элементов списка
tst1 = [1, 2, 3, 4, 5]
su = 0
for num in tst1:
    su += num ** 2
print(su)

# Задание №2: соединение элементов списка в строку
tst2 = ['a', 'b', 'c', 'd', 'e']
res = ''
for char in tst2:
    res += char
print(res)

# Задание №3: соединение элементов списка в число
tst3 = [1, 2, 3, 4, 5]
resu = ''
for digit in tst3:
    resu += str(digit)
resul = int(resu)
print(resul)
