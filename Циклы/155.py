# Задание №1
tst1 = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5
}
print("Задание №1 — индексы и ключи в виде кортежа:")
for index, key in enumerate(tst1.keys()):
    print(index, key)

# Задание №2
tst2 = {
    '1': 11,
    '2': 12,
    '3': 13,
    '4': 14
}
print("\nЗадание №2 — индексы и ключи:")
for index, key in enumerate(tst2.keys()):
    print(index, key)

# Задание №3
tst3 = {
    'x': 10,
    'y': 20,
    'z': 30
}
print("\nЗадание №3 — ключи и индексы:")
for key, index in zip(tst3.keys(), range(len(tst3))):
    print(f"Ключ: '{key}', индекс: {index}")
