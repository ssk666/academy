#Найти сводный индекс
# nums = [2, 1, -1]
# pivot = -1
#
# for i in range(len(nums)):
#     if sum(nums[:i]) == sum(nums[i + 1:]):
#         pivot = i
#         break
# print(pivot)



#Регулярные выражения

import re
# text = 'milk how python and Mara'

# match = re.search(r'\w{4}', text) #.search - выполняет поиск, первый аргумент - шаблон, второй аргумент - где искать
#\w{4} - найти слово из 4 букв
#нашел только первое вхождение (слово)
# print(match.group()) #.group выдает сразу слово без лишнего

# match = re.findall(r'\b\w{4}\b', text) # \b = отвечает за границу слова, чтобы задать диапазон с какой-то стороны - надо ограничить путем \b
# {4,} - если поставить так запятую, то будет искать от 4 букв до бесконечности
# print(match)


# text = '1234 124 748 78 5 147'
# match = re.findall(r'\b\d{3}\b', text)
# print(match)


# dates = '10.12.2001 15/07/2002 14.02.14 18-05-2024'
#
# match = re.findall(r'\d\d\.\d\d\.\d\d\d\d', dates)
# match_sub = re.sub(r'\d{2}/\d\d/\d{4}', r'dd.mm.yyyy', dates) # смена паттерна, то есть из / в .
#
# print(match_sub)


# text = 'Ivan, Bob; Mara, Step'

# names = re.split(r'[,;]', ''.join(text.split())) # пишем какие есть символы, чтобы нормально разделить имена
# вторым аргументом убрали пробелы

# print(names)


# tels = '+79222059292 +7 (922)2059292 +7(922)-205-92-92 +7 (922)-20-592-92'
#
# correct_num = re.findall(r'\+7\s\(\d\d\d\)-\d\d-\d\d\d-\d\d', tels)
# print(correct_num)


# emails = 'testmail.ru test@mail.ru test123@mail.com test@mail!com'
#
# correct_emails = re.findall(r'\w+@\w{2,20}\.[a-z]{2,3}', emails)
# print(correct_emails)


# lorem = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

# match = re.findall(r'\b\w{4}\b', lorem)
# match = re.findall(r'\w+\,', lorem)
# print(match)


# nomer = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'
#
# match_private = re.findall(r'[АВЕКМНОРСТУХ]{1}\d\d\d[АВЕКМНОРСТУХ]{2}\d{2,3}', nomer)
# match_taxi = re.findall(r'[АВЕКМНОРСТУХ]{2}\d\d\d\d{2,3}', nomer)
#
# print(f'Номера частников: {match_private}')
# print(f'Номера такси: {match_taxi}')


import requests
url = 'http://www.columbia.edu/~fdc/sample.html'
response = requests.get(url)
text = response.text

headers = re.findall(r'<h3 id="\w*">(.*)</h3>', text)

print(headers)













