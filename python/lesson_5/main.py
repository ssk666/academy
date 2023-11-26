# string = 'Hello'
# encoded_string = string.encode(encoding='utf8') - закодировали строку .encode
# print(encoded_string)
# decoded_string = encoded_string.decode(encoding='utf8') - раскодировали строку .decode
# print(decoded_string)



# string = 'abcdefg'
# print(len(string)) - длинна строки
# print(string[0]) - получили символ из строки по идексу (ответ: a)

# 2 cпособа найти конечный символ
# print(string[-1])
# print(string[len(string) -1])

# print(string[0:3]) - с 0 до 2 , тк 0 включительно, а 3 - нет
# print(string[:3]) - то же самое
# print(string[3:]) - с 3 до конца (defg)

# print(string[0:5:2]) - от 0 до 4, но с шагом в 2 (на каждый второй / через один)
# print(string[-4:-1]) - наоборот с конца считаем, ответ - def
# print(string[-1:-4:-1]) - ответ gfe (с шагом в один = отрицательный шаг)
# print(string[::-1]) - строка задом наперед - gfedcba



# example = '0123456789'
#
# print(example[0:3]) - 012
# print(example[3:6]) - 345
# print(example[-1:-4:-1]) - 987
# print(example[0:9:2]) - 02468
# print(example[::-1]) - 9876543210
# print(example[-5:-8:-1]) - 543
# print(example[-2:-7:-2]) - 864
# print(example[-6:-10:-1]) - 4321



# text = 'python is a programming language'

# print(text.capitalize()) - первый символ строки делает с заглавной буквы
# print(text.title()) - каждое новое слово с заглавной буквы
# print(text.count('p')) - сколько раз встречается буква P в этой строчке; ('py') - сколько раз встречается 'py'
# print(text.lower()) - делает всю строку с нижней буквы (нижний регистр)
# print(text.upper()) - КАПСОМ (большими буквами)
# print(text.replace(' ', '-')) - изменить что-то на что-то, в данном случае все пробелы на тире
# print(text.index('n')) - нашли по индексу, то есть 012345 [0:6]
# print(text.index('lang')) - с 24 индекса начинается строка
# print(len(text)) - считает все вместе с пробелами
# print(text.rstrip()) - если бы был пробел справа, то этот метод убирает его
# print(text.strip()) - убирает пробел в начале и в конце строки
# print(text.swapcase()) - все маленькие буквы станут большими, а все большие - маленькими



# string_2 = 'python123 ruby78'

# print(string_2.isalnum()) - состоит ли вся строка из цифр?
# print(string_2.isalpha()) - состоит ли вся строка из букв?
# print(string_2.isdigit()) - состоит ли ТОЛЬКО ИЗ цифр?
# print(string_2.islower()) - состоит ли строка только из нижнего регистра?
# print(string_2.isupper()) - состоит ли строка только из верхнего регистра?
# print(string_2.isascii()) - проверка символа в таблице ascii
# print('100'.isdecimal()) - проверка на целое число
# print(string_2.isspace()) - есть ли пробел вместо слова какго-нибудь



# string_3 = 'Python'

# print(string_3.startswith('P')) - начинается ли именно с этой буквы (можно сделать в виде номера телефона)




# string_4 = 'mara@mail.ru'

# print(string_4.endswith('ru')) - заканчивается ли эта строка именно на эти буквы
# print('@' in string_4) - входит ли @ в строку
# print(string_4.count('@') == 1) - если собака встретилась один раз, то же самое что и выше



# string_5 = 'Python ruby js'
# print(string_5.split('r')) -делит строку по конкретному символу (['Python ', 'uby js'])



# Задача 9

# text = str(input('Введите текст: '))
#
# print('Больших букв: ', text.count('Ы'), '\nМаленьких букв: ', text.count('ы'))



# Регистрация
# Email содержит (@, .ru, .com)
# Password содержит 8 символов, буквы и цифры, без спец символов

# registration = False
#
# while not registration: #- тк. во флаге False , пишем это, чтобы программа работала корректно
#     email = str(input('Введите Email: '))
#     password1 = str(input('Введите пароль: '))
#     password2 = str(input('Подтвердите пароль: '))
#     if ('@' in email) and (email.endswith('.ru') or email.endswith('.com')):
#         if password1 == password2:
#             if len(password1) == 8 and password1.isalnum() and not password1.isalpha() and not password1.isdigit():
#                 print('Вы зарегистрированы! ')
#                 registration = True
#             else:
#                 print('Password must be with len 8...')
#
#         else:
#             print('Passwords must be match')
#     else:
#         print('Email must consist "@" and ending ".ru / .com"')



# Авторизация по номеру телефона

# registration = False
#
# while not registration:
#     tel = input('Введите телефон в формате +79XXXXXXXXXX: ')
#     name = input('Введите имя: ')
#     surname = input('Введите фамилию: ')
#
#     if tel.startswith('+79') and len(tel) == 12 and tel[1:].isdigit():
#         if name.isalpha() and surname.isalpha():
#             print(f'Your name: {name.capitalize()}\n'
#                   f'Your surname: {surname.capitalize()}\n'
#                   f'Phone number: {tel}')
#             registration = True
#         else:
#             print('Invalid name+surname')
#     else:
#         print('Invalid number')



# Задание 1

# text = input('Введи текст: ')
# print(text[::-1])



# Задание 2
# Это через генератор подсчета
# text = input('Введи текст: ')
#
# print('Кол-во букв: ', len([i for i in text if i.isalpha()]))
# print('Кол-во цифр: ', len([i for i in text if i.isdigit()]))


# 2 решение
# string = input('Введи строку: ')
#
# digit = 0
# letter = 0
#
# for i in string:
#     if i.isalpha():
#         letter += 1
#     elif i.isdigit():
#         digit += 1
#
# print(f'Букв: {letter}\t'
#       f'Цифр: {digit}')


# Задание 3
# text = input('Введи текст: ')
# sym = input('Введи символ: ')

# print('Символ встречается столько раз: ', text.count(sym))



# Задание 4

# string = input('Введи строку: ')
# word = input('Введи слово: ')

# print('Слово в Вашей строке встречается столько раз: ', string.count(word))



# Задание 5
# string = input('Введи строку: ')
# word = input('Введи слово: ')
#
# old_word = input('Какое хотите заменить слово: ')
# new_word = input('Слово для замены: ')
#
#
# print(string.replace(old_word, new_word))
# print(string.find(word))



# Задание 11

# str_1 = input('Введи первую строку: ').lower()
# str_2 = input('Введи вторую строку: ').lower()
#
# if str_2 in str_1:
#     print('Есть контакт')
# if str_2 not in str_1:
#     print('Мимо')























































