st1 = {4, 2, 6, 10}
st2 = {1, 6, 3, 2}
st3 = {5, 8}
st4 = {6, 3, 1}

# Шаг 1: разница st1 и st2
dif = st1 - st2


# Шаг 2: объединение st3 и st4
uni = st3 | st4

# Шаг 3: пересечение результатов шагов 1 и 2
com = dif & uni

# Вывод результатов
print(st1)
print(st2)
print(dif)
print(st3)
print(st4)
print(uni)
print(com)
