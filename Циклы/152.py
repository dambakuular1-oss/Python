# Задание №1
tst1 = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5
}
for key in tst1.keys():
    print(key)

# Задание №2
tst2 = {
    2: 'a',
    4: 'b',
    6: 'c',
    8: 'd'
}
for key in tst2.keys():
    if key != 8:
        print(key)

# Задание №3
tst = {
    '1': 'a',
    '2': 'b',
    '3': 'c',
    '4': 'd'
}
res = ''

for key in tst.keys():
    if key != '1':
        res += key

result = tuple(res)
print(result)