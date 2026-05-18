import random
random.seed(42)

# №1.
num1 = 10
num2 = 20
result1 = random.randint(num1, num2)
print(result1)

# №2.
num1 = 5
num2 = 30
result2 = random.randint(num1, num2)
print(result2)

# №3.
num1 = 1.345
num2 = 14.784
result3 = random.uniform(num1, num2)
print(result3)

# №4.
num1 = -2
num2 = 10
result4 = random.uniform(num1, num2)
print(result4)

# №5.
num1 = 5
num2 = 50
num3 = 4
result5 = random.randrange(num1, num2, num3)
print(result5)

# №6.
lst = [1, 2, 3, 4, 5]
result6 = random.choice(lst)
print(result6)

# №7.
lst = [1, 2, 3, 4, 5]
result7 = random.sample(lst, 3)
print(result7)

# №8.
lst = [1, 2, 3, 4, 5]
random.shuffle(lst)  # изменяет исходный список
print(lst)

# №9.
lst = [1, 1, 1, 2, 2, 3, 3, 4, 5]
unique_elements = list(set(lst))  # убираем дубликаты
result9 = random.sample(unique_elements, 3)
print(result9)

# №10.
num = 7
random.seed(num)  # инициализируем генератор с числом 7
# Генерируем случайное число после инициализации
after_seed_num = random.random()
print(num)

# №11.
tlp = (10, 6, 2, 4)
random_number = random.choice(tlp)
initialized_value = random_number  # инициализация переменной
print(tlp,initialized_value)
