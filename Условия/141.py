month = 6

if not (1 <= month <= 12):
    print("Ошибка: номер месяца должен быть в интервале от 1 до 12")
else:
    if month in [12, 1, 2]:
        print('зима')
    elif month in [3, 4, 5]:
        print('весна')
    elif month in [6, 7, 8]:
        print('лето')
    else:  # месяцы 9, 10, 11
        print('осень')
    
num = 91  # Пример значения

if 10 <= num <= 99:
    tens = num // 10
    
    if tens <= 9:
        print('однозначное число')
    else:
        print('двузначное число')
else:
    print('Число не попадает в диапазон от 10 до 99')
 
