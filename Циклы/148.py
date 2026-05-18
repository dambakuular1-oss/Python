# Задание №1: вывести из множества только положительные числа
tst1 = {-2, 1, 3, -5, 4, -8}
for num in tst1:
    if num > 0:
        print(num)

# Задание №2: элементы списка больше 2 и меньше 5
tst2 = [7, 1, 2, 5, 3, 9]
result_list = []
for num in tst2:
    if 2 < num < 5:
        result_list.append(num)
print(result_list)

# Задание №3: сумма чётных элементов кортежа
tst3 = (1, 2, 3, 4, 5, 6, 7)
sum_even = 0
for num in tst3:
    if num % 2 == 0:
        sum_even += num
print(sum_even)

# Задание №4: нечётные цифры числа в новый список
tst4 = 1234567
odd_digits = []
for digit in str(tst4):
    digit_int = int(digit)
    if digit_int % 2 != 0:
        odd_digits.append(digit_int)
print(odd_digits)
