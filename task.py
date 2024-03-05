################### Генератор лог файла ##################

import random

# Функция генерации случайной даты
# Возвращает строковое значение даты в формате YYYY-MM-DD
def generate_random_date():
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    random_year = random.randint(2000, 2024)
    random_month = random.randint(1, 12)
    
    if random_month == 1 and random_year % 4 == 0:
        random_day_in_month = random.randint(1, 29)    
    else:
        random_day_in_month = random.randint(1, days_in_month[random_month-1])    

    date=str(random_year)+'-'
    
    if random_month < 10:
        date=date+'0'
    date=date+str(random_month)+'-'
    
    if random_day_in_month < 10:
        date=date+'0'
    date=date+str(random_day_in_month)

    return date


# Функция генерации случайного времени
# Возвращает строковое значение времени в формате HH:MM:SS
def generate_random_time():
    random_hour = random.randint(0, 23)
    random_minute = random.randint(0, 59)
    random_second = random.randint(0, 59)
    
    time=''

    if random_hour < 10:
        time='0'
    time=time+str(random_hour)+':'

    if random_minute < 10:
        time=time+'0'
    time=time+str(random_minute)+':'

    if random_second < 10:
        time=time+'0'
    time=time+str(random_second)
    
    return time


# Функция генерации случайного типа запроса
# Возвращает строковое значение типа запроса из перечня возможных типов: GET, POST, PUT, DELETE
def generate_request_type():
    web_request_type = ['GET','POST','PUT','DELETE']
    return web_request_type[random.randint(0, 3)]


# Функция генерации случайного IP адреса запроса
# Возвращает строковое значение в диапазоне 1.1.1.1-254.254.254.254
def generate_ip_address():
    random_hour = random.randint(0, 23)
    random_minute = random.randint(0, 59)
    random_second = random.randint(0, 59)
    
    ip_address = str(random.randint(1, 254)) + "." + str(random.randint(1, 254)) + "." + \
                 str(random.randint(1, 254)) + "." + str(random.randint(1, 254))

    return ip_address


#################### Вход в программу ###############

with open('log.txt','w') as file1:

    # Создаём лог файл из 100 записей
    for i in range (100):

        # Создаём запись запроса со случайными датой, временем, IP-адресом и типом запроса и записываем её в файл
        request_date = generate_random_date()
        request_time = generate_random_time()
        request_type = generate_request_type()
        request_ip_address = generate_ip_address()

        request_record = request_date + " " + request_time + " " + \
            request_ip_address + " " + request_type + "\n"
        
        print(request_record, end="")
        
        file1.writelines(request_record)
