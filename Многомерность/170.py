lst = [
    {
        'a': 1,
        'b': 2,
        'c': 3
    },
    {
        'a': 4,
        'b': 5,
        'c': 6
    },
    {
        'a': 7,
        'b': 8,
        'c': 9,
    },
]

total_sum = 0
for dictionary in lst:
    for value in dictionary.values():
        total_sum += value

print(total_sum)


lst = [
    {
        'a': 1,
        'b': 2,
        'c': 3
    },
    {
        'a': 4,
        'b': 5,
        'c': 6
    },
    {
        'a': 7,
        'b': 8,
        'c': 9,
    },
]

for dictionary in lst:
    for key, value in dictionary.items():
        print(key,value)
