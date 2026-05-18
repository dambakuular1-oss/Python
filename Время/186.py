from datetime import datetime

now = datetime.now()
weekday_number = now.weekday()
print(weekday_number)

current_weekday = now.weekday()
if current_weekday < 5:
    day_type = "рабочий день"
else:
    day_type = "выходной"
print(day_type,current_weekday)
