from datetime import datetime

# Задача №1
print("Задача №1")
dt1_1 = '13/10/2018 22:15:45'
dt2_1 = '15/11/2018 09:47:16'

# Преобразуем строки в объекты datetime с форматом день/месяц/год час:минута:секунда
date1_1 = datetime.strptime(dt1_1, '%d/%m/%Y %H:%M:%S')
date2_1 = datetime.strptime(dt2_1, '%d/%m/%Y %H:%M:%S')


difference_1 = date2_1 - date1_1

print(f"Разница: {difference_1}")
print()

# Задача №2
print("Задача №2")
dt1_2 = '01-12-2025 16:07:05'  # исправлено: секунды 05 вместо 5
dt2_2 = '31-12-2025 10:32:45'  # исправлено: разделитель - вместо :

# Преобразуем строки в объекты datetime с форматом день-месяц-год час:минута:секунда
date1_2 = datetime.strptime(dt1_2, '%d-%m-%Y %H:%M:%S')
date2_2 = datetime.strptime(dt2_2, '%d-%m-%Y %H:%M:%S')

difference_2 = date2_2 - date1_2

print(f"Разница: {difference_2}")
