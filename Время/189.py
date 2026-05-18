from datetime import datetime

# Получаем текущее время один раз
current_datetime = datetime.now()

# Задача №1: выводим время в формате часы:минуты:секунды
time_only = current_datetime.strftime("%H:%M:%S")
print("№1. Текущее время (часы:минуты:секунды):", time_only)

# Задача №2: выводим дату и время в формате год-месяц-день часы:минуты:секунды
full_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print("№2. Текущие дата и время (год-месяц-день часы:минуты:секунды):", full_datetime)
