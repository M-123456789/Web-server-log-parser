################### Генератор лог файла ##################

# импортируем библиотеку работы со случайными числами
import random

# импортируем библиотеку работы с регулярными выражениями
import re

from datetime import date

# Функция генерации случайной даты
# Возвращает строковое значение даты в формате YYYY-MM-DD
def generate_random_date():
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    current_year = int(date.today().year)
    random_year = random.randint(2000, current_year)

    if (random_year == current_year):
        random_month = random.randint(1, int(date.today().month))
    else:
        random_month = random.randint(1, 12)
    
    if random_month == 2 and random_year % 4 == 0:
        # если месяц февраль и год високосный, то дата может быть 1-29 февраля.    
        random_day_in_month = random.randint(1, 29)    
    else:
        random_day_in_month = random.randint(1, days_in_month[random_month-1])    

    random_date=str(random_year)+'-'
    
    if random_month < 10:
        random_date += '0'
    random_date += str(random_month)+'-'
    
    if random_day_in_month < 10:
        random_date += '0'
    random_date += str(random_day_in_month)

    return random_date

# Функция проверки даты на валидность
# Передаваемый параметр - строка с датой в формате YYYY-MM-DD
# Если дата валидна, функция возвращает True, иначе False
def validate_date(request_date):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    print ("Дата запроса: " + request_date, end ="")
    if len(request_date) == 10:
        match = re.search(r'\d\d\d\d\-\d\d\-\d\d', request_date)
        if match:
            request_year = int (request_date[:4])
            request_month = int (request_date[5:7])
            request_day = int (request_date[-2:])

            current_year = int(date.today().year)
            current_month = int(date.today().month)
            current_day = int(date.today().day)
     
            if ((request_year >= 2000 and request_year < current_year and
                (request_month >= 1 and request_month <= 12 and
                request_day >= 1 and request_day <= days_in_month[request_month-1]) or
                (request_year % 4 == 0 and request_month == 2 and request_day == 29)) 
                or 
                (request_year == current_year and
                ((request_month >= 1 and request_month < current_month and
                request_day >= 1 and request_day <= days_in_month[request_month-1]) or 
                (request_year % 4 == 0 and request_month == 2 and request_day == 29) or
                (request_month == current_month and 
                request_day >=1 and request_day <= current_day)))):
                print (" - валидна")
                return True
    print (" - невалидна")
    return False

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

# Функция проверки времени на валидность
# Передаваемый параметр - строка с временем в формате HH:MM:SS
# Если время валидно, функция возвращает True, иначе False
def validate_time(request_time):
    print ("Время запроса: " + request_time, end ="")
    if len(request_time) == 8:
        match = re.search(r'\d\d\:\d\d\:\d\d', request_time)
        if match:
            request_hour = int (request_time[:2])
            request_minute = int (request_time[3:5])
            request_second = int (request_time[-2:])

            if (request_hour >= 0 and request_hour <= 23 and
                request_minute >=0 and request_minute <= 59 and
                request_second >=0 and request_second <= 59):
                print (" - валидно")
                return True
    print (" - невалидно")
    return False

# Функция генерации случайного типа запроса
# Возвращает строковое значение типа запроса из перечня возможных типов: GET, POST, PUT, DELETE, HEAD, OPTIONS, PATCH
def generate_request_type():
    web_request_type = ['GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'OPTIONS', 'PATCH']
    return web_request_type[random.randint(0, len(web_request_type)-1)]


# Функция проверки типа запроса на валидность
# Передаваемый параметр - строка с типом запроса
# Если тип запроса валиден, функция возвращает True, иначе False
def validate_request_type(request_type):
    print ("Тип запроса: " + request_type, end ="")
    web_request_type = ['GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'OPTIONS', 'PATCH']
    if request_type in web_request_type:
        print (" - валиден")
        return True
    print (" - невалиден")
    return False


# импортируем библиотеку работы с IP-адресами
import ipaddress

# Функция проверки корректности IP адреса
def ip_address_validator(ip):
    try:
        ip_obj = ipaddress.ip_address(ip)
        print(f"{ip} is a valid IP address")
        return True
    except ValueError:
        print(f"ERROR: {ip} is not a valid IP address!")
        return False

# Функция генерации случайного IP адреса запроса
# Возвращает строковое значение в диапазоне 1.1.1.1-254.254.254.254
def generate_ip_address():
    valid_ip = 0
    while valid_ip == 0:
        ip_address = str(random.randint(1, 254)) + "." + str(random.randint(0, 254)) + "." + \
                     str(random.randint(0, 254)) + "." + str(random.randint(1, 254))
        valid_ip=ip_address_validator(ip_address)
    return ip_address

# Функция генерации случайного кода ответа веб-сервера на запрос
# Возвращает первые три символа строкового значения кода ответа веб-сервера из диапазона преднастроенных значений
def generate_request_answer_code():
    web_request_answer_code = ['100 Continue', '101 Switching Protocols', '102 Processing', '103 Early Hints',\
                        '200 OK', '201 Created', '203 Non-Authoritative Information',\
                        '204 No Content', '205 Reset Content', '206 Partial Content',\
                        '207 Multi-Status', '208 Already Reported', '226 IM Used',\
                        '300 Multiple Choices','301 Moved Permanently','302 Found',\
                        '303 See Other', '304 Not Modified', '305 Use Proxy', '306 unused',\
                        '307 Temporary Redirect', '308 Permanent Redirect',\
                        '400 Bad Request', '401 Unauthorized', '402 Payment Required',\
                        '403 Forbidden', '404 Not Found', '405 Method Not Allowed',\
                        '406 Not Acceptable', '407 Proxy Authentication Required',\
                        '408 Request Timeout', '409 Conflict', '410 Gone', '411 Length Required',
                        '412 Precondition Failed', '413 Payload Too Large', '414 URI Too Long',\
                        '415 Unsupported Media Type', '416 Range Not Satisfiable', '417 Expectation Failed',\
                        '418 I\'m a teapot','421 Misdirected Request', '422 Unprocessable Content',\
                        '423 Locked', '424 Failed Dependency', '425 Too Early',\
                        '426 Upgrade Required', '428 Precondition Required', '429 Too Many Requests',\
                        '431 Request Header Fields Too Large', '451 Unavailable For Legal Reasons',\
                        '500 Internal Server Error', '501 Not Implemented', '502 Bad Gateway',\
                        '503 Service Unavailable', '504 Gateway Timeout', '505 HTTP Version Not Supported',\
                        '506 Variant Also Negotiates', '507 Insufficient Storage', '508 Loop Detected',\
                        '510 Not Extended', '511 Network Authentication Required']
    return web_request_answer_code[random.randint(0, len(web_request_answer_code)-1)][:3]


# Функция генерации случайного енд-пойнта
# Возвращает строковое значение из диапазона преднастроенных значений
def generate_request_endpoint():
    web_request_endpoint = ['/', '/adminka', '/forum', '/catalog', '/authorization_endpoint']
    return web_request_endpoint[random.randint(0, len(web_request_endpoint)-1)]

#################### Вход в программу ###############

#Открываем лог файл для записи
with open('log.txt','w') as log_file:

    # Создаём лог файл из 100 записей
    for i in range (100):

        # Создаём запись запроса со случайными датой, временем, IP-адресом,
        # типом запроса, кодом ответа веб-сервера, ендпойнтом и длиной запроса
        # и записываем её в файл
        request_date = generate_random_date()
        request_time = generate_random_time()
        request_ip_address = generate_ip_address()
        request_type = generate_request_type()
        request_server_answer_code = generate_request_answer_code()
        request_endpoint = generate_request_endpoint()
        request_content_length = str(random.randint(20, 65535))

        request_record = request_date + " " + request_time + " " + \
            request_ip_address + "," + request_type + "," + \
            request_server_answer_code + "," + request_endpoint + "," + \
            request_content_length + "\n"
        
        print(request_record, end="")
        
        log_file.writelines(request_record)

print("Сгенерировали файл журнала веб-сервера. Нажмите ENTER для его чтения и обработки.")
input()

from heapq import nlargest

# читаем сгенерированный лог файл
with open('log.txt','r') as log_file:

    total_records_in_file = 0
    total_valid_requests = 0
    requests_types_counts = {'GET':0, 'POST':0, 'PUT':0, 'DELETE':0, 'HEAD':0, 'OPTIONS':0, 'PATCH':0}

    for string_from_file in log_file:
        print(string_from_file, end="")
        
        total_records_in_file += 1

        if len(string_from_file) < len('2024-01-01 01:23:59 1.1.1.1,GET,404,/,20'):
            print("Строка [" + string_from_file + "] не соответствует минимальной длине - строка не может быть обработана")
        else:
            # Для учёта запроса дата, время, IP-адрес, тип запроса, код ответа веб-сервера, ендпойнт и длина запроса должны быть валидны
            # Для этого используем счётчик валидных полей
            request_check = 0

            #Проверяем корректность даты
            request_date = string_from_file[:10] 
            #print (request_date)
            if validate_date(request_date):
                request_check += 1

            #Проверяем корректность времени
            request_time = string_from_file[11:11+8] 
            #print (request_time)
            if validate_time(request_time):
                request_check += 1

            #Проверяем корректность IP-адреса
            #match = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', string_from_file[20:])
            request_payload = string_from_file[20:].split(',')
            print ("Полезная информация в запросе для дальнейшего анализа: ", end="")
            print (request_payload)
            #print ("Подстрока для проверки IP-адреса " + request_payload[0])
            if ip_address_validator (request_payload[0]):
                #print ("IP-адрес валидный: " + request_payload[0])
                request_check += 1
            
            #Проверяем корректность типа запроса
            if validate_request_type(request_payload[1]):
                request_check += 1

            print ("Проверок на валидность запроса пройдено успешно: " + str(request_check) + " из 4")
            #Если все проверки прошли успешно, учитываем запрос в дальнейшем
            if request_check == 4:
                total_valid_requests += 1
                
                requests_types_counts[request_payload[1]] += 1 
    
    print ("Всего строк в файле: " + str(total_records_in_file))
    print ("Количество валидных запросов: " + str(total_valid_requests))
    print ("Типы запросов и их количество: ", end="")
    print (requests_types_counts)

    sorted_dict = sorted(requests_types_counts.items(), key=lambda x:x[1], reverse=True)[:5]
    converted_dict = dict(sorted_dict)

    print ("Топ 5 запросов по количеству: ")
    print (converted_dict)