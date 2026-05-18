import time

# Получаем текущее время в формате struct_time
current_time = time.localtime()

# Извлекаем день месяца из struct_time (поле tm_mday)
current_day = current_time.tm_mday

print(f"Текущий день месяца: {current_day}")

import time

dt = 1602314100.0


# Преобразуем epoch в struct_time для локального часового пояса
struct_time_local = time.localtime(dt)
print("Локальное время:", struct_time_local)

# Преобразуем epoch в struct_time для UTC
struct_time_utc = time.gmtime(dt)
print("UTC время:", struct_time_utc)