import time

epoch_time = time.time()  # получаем текущий epoch
readable_date = time.ctime(epoch_time)
print(readable_date)