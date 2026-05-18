lst = [1, 2, 3, 4]

for el in lst:
    if el <= 0:
        print('---')
        break
else:
    print('+++')


n = 17

if n < 2:
    print('---')
elif n == 2:
    print('+++')
elif n % 2 == 0:
    print('---')
else:
    sqrt_n = int(n ** 0.5)
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            print('---')
            break
    else:
        print('+++')
