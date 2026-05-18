# №1.
lst = [2, 4, 6, 8]
result1 = min(lst)
print(result1)  # 2

# №2.
tlp = (-1, 2, -6, 3)
result2 = min(tlp)
print(result2)  # -6

# №3.
dct = {
    'a': 2,
    'b': 4,
    'c': 5,
    'd': 1
}
result3 = max(dct.values())
print(result3)  # 5

# №4.
num = 123456
digits = [int(digit) for digit in str(num)]

result4_max = max(digits)
result4_min = min(digits)

print(result4_max,result4_min)  # макс: 6, мин: 1
