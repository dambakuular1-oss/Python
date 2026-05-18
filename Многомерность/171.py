result = []

for i in range(0, 3):
    row = []
    for j in range(1, 4):
        row.append(j)
    result.append(row)

print(result)


lst1 = []
lst2 = ['a', 'b', 'c']

for _ in [0, 1]:
    lst1.append(lst2.copy())

print(lst1)
