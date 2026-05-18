# №1
tst1 = 2
tst2 = 4
tst3 = 6

def sum3(a, b, c):
    return a + b + c

print(sum3(tst1, tst2, tst3))

# №2
def func(lst):
    sum = 0

    for el in lst:
        sum += el

    return sum

tst = [1, 3, 6]
print(func(tst))