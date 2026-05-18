lst = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in lst:
    for element in row:
        print(element)


lst = [
    [2, 4, 6],
    [3, 5, 7],
    [9, 12, 15]
]

total_sum = 0
for row in lst:
    for element in row:
        total_sum += element

print(total_sum)  # Вывод: 63


lst = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]

result_string = ''
for row in lst:
    for element in row:
        result_string += element

print(result_string)  # Вывод: abcdefghi
