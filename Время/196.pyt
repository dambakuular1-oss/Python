from datetime import datetime

# Заданная дата
dt = '24/07/2015 16:1'

# Преобразуем строку в объект datetime (формат: день/месяц/год час:минута)
target_date = datetime.strptime(dt, '%d/%m/%Y %H:%M')

# Текущее время
current_time = datetime.now()

# Вычисляем разницу (целевая дата в прошлом, поэтому разница отрицательная)
time_difference = target_date - current_time
seconds_difference = int(time_difference.total_seconds())

print(f"Заданная дата: {target_date}")
print(f"Текущее время: {current_time}")
print(f"Секунд с текущего момента до заданной даты: {seconds_difference}")