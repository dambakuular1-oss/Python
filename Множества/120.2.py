st1 = {1, 2, 3, 4}
st2 = {1, 2, 4, 5}
st3 = {1, 2, 5, 7}

common = st1.intersection(st2).intersection(st3)
print(common)  # Выведет: {1, 2}
