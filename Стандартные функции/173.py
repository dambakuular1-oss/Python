import math

# №1.
num = 16.456
result1 = round(num)
print(result1)  # 16

# №2.
num = 21.167
result2 = round(num, 2)
print(result2)  # 21.17

# №3.
num = 3.348
result3 = math.ceil(num)
print(result3)  # 4

# №4.
num = 18.565
result4 = math.floor(num)
print(result4)  # 18

# №5.
num = 17
sqrt_num = math.sqrt(num)
result5 = round(sqrt_num, 2)
print(result5)  # 4.12

# №6.
num = 17
cubic_root = num ** (1/3)
result6 = math.ceil(cubic_root)
print(result6)  # 3

# №7.
lst = [3.45, 1.54, 5.76]
result7 = [round(x) for x in lst]
print(result7)  # [3, 2, 6]

# №8.
lst1 = [1.514, 4.897, 2.657]
lst2 = [math.floor(x) for x in lst1]
print(lst1,lst2)  # lst2 = [1, 4, 2]
