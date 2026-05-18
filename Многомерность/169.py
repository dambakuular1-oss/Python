lst = [
    [
        ['q', 'w', 'e'],
        ['r', 't', 'y'],
        ['u', 'i', 'o'],
    ],
    [
        ['p', 'a', 's'],
        ['d', 'f', 'g'],
        ['h', 'j', 'k'],
    ],
    [
        ['l', 'z', 'x'],
        ['c', 'v', 'b'],
        ['n', 'm', 'q'],
    ],
]

for level1 in lst:
    for level2 in level1:
        for element in level2:
            print(element)


lst = [
    [
        [1, 3],
        [5, 7],
    ],
    [
        [2, 4],
        [6, 8],
    ],
]

sum = 0
for level1 in lst:
    for level2 in level1:
        for number in level2:
            sum += number

print(sum)
