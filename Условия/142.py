num = 2

if num == 1:
    season = "зима"
elif num == 2:
    season = "весна"
elif num == 3:
    season = "лето"
elif num == 4:
    season = "осень"
else:
    season = "некорректный номер поры года"

print(season)

num1 = 6  # Пример значения

if num1 in [12, 1, 2]:
    season1 = "зима"
elif num1 in [3, 4, 5]:
    season1 = "весна"
elif num1 in [6, 7, 8]:
    season1 = "лето"
elif num1 in [9, 10, 11]:
    season1 = "осень"
else:
    season1 = "некорректный номер месяца"

print(season1)
