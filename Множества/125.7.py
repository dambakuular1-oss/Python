st1 = {'ab', 'b', 'ce', 'de', 'd'}
st2 = {'ef', 'd', 'ab', 'bc'}
st3 = {'a', 'g', 'b', 'c'}

# Находим общие элементы для st1 и st2
com = st1 & st2

# Объединяем полученное множество с st3
result = com | st3

print(com)
print(result)
