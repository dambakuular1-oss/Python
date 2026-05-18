lst = [
    [
        ['a', 'b'],
        ['c', 'd'],
    ],
    [
        ['e', 'f'],
        ['g', 'h'],
    ]
]

# Получаем нужные символы по индексам и объединяем в строку
result = lst[0][0][0] + lst[0][1][0] + lst[1][0][0] + lst[1][1][0]
print(result)  # Вывод: acfg


lst = [
    [
        [1, 2],
        [3, 4],
    ],
    [
        [5, 6],
        [7, 8],
    ],
]

total = 0
for sublist1 in lst:  # проходим по внешним спискам
    for sublist2 in sublist1:  # проходим по средним спискам
        for num in sublist2:  # проходим по внутренним спискам с числами
            total += num
print(total)