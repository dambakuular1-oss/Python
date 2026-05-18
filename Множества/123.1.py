st1 = {1, 3, 6, 8}
st2 = {5, 8, 4, 2}
st3 = {4, 7, 3, 1}

# Шаг 1: объединение st1 и st3
union_st1_st3 = st1  st3

# Шаг 2: пересечение объединения с st3
intersection_result = union_st1_st3 & st3

# Вывод результатов
print(st1)
print(st3)
print(union_st1_st3)
print(intersection_result)
