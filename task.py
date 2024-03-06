################### Генератор лог файла ##################

# импортируем библиотеку работы со случайными числами
import random

# Функция генерации случайной даты
# Возвращает строковое значение даты в формате YYYY-MM-DD
def generate_random_date():
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    random_year = random.randint(2000, 2024)
    random_month = random.randint(0, len(days_in_month)-1)
    

    if random_month == 1 and random_year % 4 == 0:
        # если месяц февраль и год високосный, то дата может быть 1-29 февраля.    
        random_day_in_month = random.randint(1, 29)    
    else:
        random_day_in_month = random.randint(1, days_in_month[random_month])    

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
# Возвращает строковое значение типа запроса из перечня возможных типов: GET, POST, PUT, DELETE, HEAD, OPTIONS, PATCH
def generate_request_type():
    web_request_type = ['GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'OPTIONS', 'PATCH']
    return web_request_type[random.randint(0, len(web_request_type)-1)]


# Функция генерации случайного IP адреса запроса
# Возвращает строковое значение в диапазоне 1.1.1.1-254.254.254.254
def generate_ip_address():
    ip_address = str(random.randint(1, 254)) + "." + str(random.randint(0, 254)) + "." + \
                 str(random.randint(0, 254)) + "." + str(random.randint(1, 900))
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

# импортируем библиотеку работы с регулярными выражениями
import re

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

# читаем сгенерированный лог файл
with open('log.txt','r') as log_file:

    for string_from_file in log_file:
        print(string_from_file, end="")
        if len(string_from_file) < len('2024-01-01 01:23:59 1.1.1.1,GET,404,/,20'):
            print("Строка [" + string_from_file + "] не соответствует минимальной длине - строка не может быть обработана")
        else:
            #Проверяем корректность даты
            request_date = string_from_file[:10] 
            print (request_date)
            match = re.search(r'\d\d\d\d\-\d\d\-\d\d', request_date)
            if match:
                print ("Дата запроса: " + match[0])
            else:
                print ("Дата запроса не соответствует шаблону")

            #Проверяем корректность времени
            request_time = string_from_file[11:11+8] 
            print (request_time)
            match = re.search(r'\d\d\:\d\d\:\d\d', request_time)
            if match:
                print ("Время запроса: " + match[0])
            else:
                print ("Время запроса не соответствует шаблону")

            #Проверяем корректность IP-адреса
            #match = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', string_from_file[20:])
            request_ip_address = string_from_file[20:].split(',')
            print ("Подстрока для поиска IP-адреса " + request_ip_address[0])
            match_ip_address = ip_address_validator (request_ip_address[0])
            if match_ip_address:
                print ("IP-адрес валидный: " + match[0])
                
