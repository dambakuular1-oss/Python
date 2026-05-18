st1 = {2, 4, 8, 10}
st2 = {1, 8, 3, 2}

st4 = st1 ^ st2  # или st1.symmetric_difference(st2)
print(st4)  # Выведет: {1, 3, 4, 10}
