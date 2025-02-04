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
# 4 Task
user_input = input('Enter the date in this format YYYY-MM-DD: ')
date_object = datetime.datetime.strptime(user_input, "%Y-%m-%d")
print('Converted date', date_object)
# 5 Task
ivestis = "2022-12-31, 23:59:59"

my_datetime = datetime.datetime.strptime(ivestis, "%Y-%m-%d, %H:%M:%S")

menesiai = {
    "January": "sausio", "February": "vasario", "March": "kovo", "April": "balandžio",
    "May": "gegužės", "June": "birželio", "July": "liepos", "August": "rugpjūčio",
    "September": "rugsėjo", "October": "spalio", "November": "lapkričio", "December": "gruodžio"
}

menuo_en = my_datetime.strftime("%B")
menuo_lt = menesiai[menuo_en]

formatted_date_1 = my_datetime.strftime("%d/%m/%Y, %H:%M:%S")
formatted_date_2 = my_datetime.strftime(f"%Y metų {menuo_lt} %d diena")

print(formatted_date_1)
print(formatted_date_2)
print('--------------------------------------------')
# 6 Task
data1 = datetime.datetime(2023,1,1)
data2 = datetime.datetime(2024,1,1)
skirtumas = data2-data1
print(f'Skirtumas yra: {skirtumas.days}')
print('--------------------------------------------')
# 7 Task
current_date = datetime.datetime.today()
res = current_date + datetime.timedelta(days=90)
print(f'Data po 90 dienu bus: {res.strftime('%Y-%m-%d')}')
print('--------------------------------------------')
# 8 Task
current_date = datetime.datetime.today()
previous_date = datetime.datetime(2000, 1, 1)
res = current_date - previous_date
print(f'Days: {res}')
print(f'Hours: {res.seconds // 3600}')
seconds = res.total_seconds()
print(f'Seconds: {seconds}')

