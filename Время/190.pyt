from datetime import datetime
import locale

# Пытаемся установить русскую локаль для отображения дня недели на русском языке
try:
    locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')
except:
    try:
        locale.setlocale(locale.LC_TIME, 'Russian_Russia.1251')
    except:
        pass  # Если локали не найдены, используем настройки по умолчанию

# Получаем текущее время и форматируем его
current_time = datetime.now().strftime("%H:%M:%S %Y/%m/%d:%A")
print(current_time)