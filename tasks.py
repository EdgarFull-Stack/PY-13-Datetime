# 1 Task
import datetime
dt_res = datetime.datetime.today()
print(dt_res.year)
print(dt_res.month)
print(dt_res.day)
print(dt_res.hour)
print(dt_res.minute)
print(dt_res.second)
print(f'Dabar yra {dt_res.hour}:{dt_res.minute}, {dt_res.day}-{dt_res.month}-{dt_res.year}')
print('--------------------------------------------')
# 2 Task
print(datetime.datetime(1995, 7, 14, 15 ,30))
datetime_obj = datetime.datetime(1995, 7, 14)
print(datetime_obj.date())
print('--------------------------------------------')
# 3 Task
time_from_2000 = datetime.datetime.today() - datetime.datetime(2000, 1, 1)
print(f'Praejo {time_from_2000.days} dienu nuo 2000-01-01')
print('--------------------------------------------')