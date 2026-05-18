num1 = 12345
num2 = 12321

# преобразуем числа в строки
str_num1 = str(num1)
str_num2 = str(num2)

# создаём множества цифр
d_num1 = set(str_num1)  # {'1', '2', '3', '4', '5'}
d_num2 = set(str_num2)  # {'1', '2', '3'}

# проверяем, что все цифры num2 есть в num1
result = d_num2.issubset(d_num1)

# результаты
print(result)
