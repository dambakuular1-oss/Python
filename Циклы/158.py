# Задание №1
tst1 = [1, 3, 5]
tst2 = [2, 4, 6]
for pair in zip(tst1, tst2):
    print(pair)

# Задание №2
tst1 = ['a', 'b', 'c']
tst2 = ['d', 'e', 'f']
res = []
for i, char in enumerate(tst1, start=1):
    res.append(char)
    res.append(str(i))
print(res)

# Задание №3
tst1 = [11, 12, 13, 14]
tst2 = [21, 22, 23, 24]
tst3 = [31, 32, 33, 34]
sum = [a + b + c for a, b, c in zip(tst1, tst2, tst3)]
print(sum)
