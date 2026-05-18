def is_leap_year(year):
 
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Задача №1
year1 = 2020
result1 = "високосный" if is_leap_year(year1) else "не високосный"
print(f"Год {year1} — {result1}")

# Задача №2
year2 = 1910
result2 = "високосный" if is_leap_year(year2) else "не високосный"
print(f"Год {year2} — {result2}")

# Задача №3 — текущий год
from datetime import datetime
current_year = datetime.now().year
result3 = "високосный" if is_leap_year(current_year) else "не високосный"
print(f"Текущий год ({current_year}) — {result3}")
