st = [2, 4, 6, 8]

for el in st:
    if el % 2 != 0:  # если элемент нечётный
        print('---')
        break
else:
    print('+++')


tst = 'abcdef'

if 'd' in tst:
    print('+++')  # символ 'd' есть в строке
else:
    print('---')  # символа 'd' нет в строке
