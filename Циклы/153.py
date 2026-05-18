# Задание №1
tst1 = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5
}
for value in tst1.values():
    print(value)

# Задание №2
tst2 = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5
}
sum = sum(tst2.values())
print(sum)

# Задание №3
tst3 = {
    '1': 'a',
    '2': 'b',
    '3': 'c',
    '4': 'd'
}
res = ''.join(tst3.values())
print(res)
