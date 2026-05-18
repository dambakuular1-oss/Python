import time

# Заданная epoch-метка
dt = 1602314100.0

# Получаем struct_time для UTC
struct_time_utc = time.gmtime(dt)

# Получаем struct_time для локального времени
struct_time_local = time.localtime(dt)

# Извлекаем часы и минуты из обоих объектов
utc_hours = struct_time_utc.tm_hour
utc_minutes = struct_time_utc.tm_min

local_hours = struct_time_local.tm_hour
local_minutes = struct_time_local.tm_min

# Выводим результаты
print("Сравнение UTC и локального времени:")
print(f"UTC время: {utc_hours:02d}:{utc_minutes:02d}")
print(f"Локальное время: {local_hours:02d}:{local_minutes:02d}")

# Дополнительно выводим полные struct_time для наглядности
print("\nПолные объекты struct_time:")
print(f"UTC: {struct_time_utc}")
print(f"Локальное: {struct_time_local}")