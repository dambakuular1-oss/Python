# №1. Проверка, является ли число чётным
number = 8
if number % 2 == 0:
    print("Число чётное")
else:
    print("Число нечётное")

# №2. Замена символа 'a' на '!' в строке
text = "banana"
if 'a' in text:
    text = text.replace('a', '!')
print(text)

# №3. Проверка наличия символа '@' в email
email = input("Введите вашу электронную почту: ")
while '@' not in email:
    print("Ошибка: email должен содержать символ '@'")
    email = input("Пожалуйста, введите правильный email: ")
print(f"Email принят: {email}")

# №4. Проверка длины имени пользователя
name = "Alex"
if len(name) < 3:
    print("Имя слишком короткое")
elif 3 <= len(name) <= 20:
    print("Имя корректно")
else:
    print("Необходимо сократить имя")

# №5. Проверка пароля на пустоту и длину
password = "my_secret_123"
if not password:
    print("Пароль не может быть пустым")
elif 6 <= len(password) <= 14:
    print("Пароль корректен")
else:
    print("Длина пароля должна быть от 6 до 14 символов")

# №6. Переписывание кода с тернарным оператором
tst = 'abcdef'
print('string is too long' if len(tst) > 20 else 'string is too short')
